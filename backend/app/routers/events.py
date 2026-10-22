


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import SecurityEvent
from app.schemas import SecurityEventCreate, SecurityEventResponse


from sqlalchemy import func


router = APIRouter(prefix="/events", tags=["Security Events"])



@router.post(
    "/",
    response_model=SecurityEventResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_event(
    event_data: SecurityEventCreate,
    db: Session = Depends(get_db),
):
    try:
        event_status = event_data.status.strip().lower()
        event_type = event_data.event_type.strip().lower()

        is_suspicious = False

        if (
            event_type == "login"
            and event_status == "failure"
            and event_data.source_ip
        ):
            from datetime import datetime, timedelta, timezone
            from sqlalchemy import func

            cutoff_time = datetime.now(timezone.utc) - timedelta(minutes=10)

            failed_attempts = (
                db.query(func.count(SecurityEvent.id))
                .filter(
                    SecurityEvent.event_type.ilike("login"),
                    SecurityEvent.status.ilike("failure"),
                    SecurityEvent.source_ip == event_data.source_ip.strip(),
                    SecurityEvent.timestamp >= cutoff_time,
                )
                .scalar()
            )

            is_suspicious = failed_attempts + 1 >= 5

        event = SecurityEvent(
            username=event_data.username,
            source_ip=event_data.source_ip.strip() if event_data.source_ip else None,
            event_type=event_type,
            status=event_status,
            timestamp=event_data.timestamp,
            is_suspicious=is_suspicious,
        )

        db.add(event)
        db.commit()
        db.refresh(event)

        return event

    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to save security event.",
        ) from exc




@router.get("/", response_model=list[SecurityEventResponse])
def list_events(
    skip: int = 0,
    limit: int = 50,
    status_filter: str | None = None,
    db: Session = Depends(get_db),
):
    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip cannot be negative.",
        )

    if not 1 <= limit <= 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100.",
        )

    query = db.query(SecurityEvent)

    if status_filter:
        status_filter = status_filter.strip().lower()

        if status_filter not in ["success", "failure"]:
            raise HTTPException(
                status_code=400,
                detail="status_filter must be 'success' or 'failure'.",
            )

        query = query.filter(
            SecurityEvent.status.ilike(status_filter)
        )

    return (
        query
        .order_by(SecurityEvent.timestamp.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )



@router.get("/suspicious", response_model=list[SecurityEventResponse])
def list_suspicious_events(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
):
    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip cannot be negative.",
        )

    if not 1 <= limit <= 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100.",
        )

    return (
        db.query(SecurityEvent)
        .filter(SecurityEvent.is_suspicious.is_(True))
        .order_by(SecurityEvent.timestamp.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )



@router.get("/stats/summary")
def get_event_statistics(
    db: Session = Depends(get_db),
):
    total_events = db.query(func.count(SecurityEvent.id)).scalar() or 0

    suspicious_events = (
        db.query(func.count(SecurityEvent.id))
        .filter(SecurityEvent.is_suspicious.is_(True))
        .scalar()
        or 0
    )

    failed_logins = (
        db.query(func.count(SecurityEvent.id))
        .filter(
            SecurityEvent.event_type.ilike("login"),
            SecurityEvent.status.ilike("failure"),
        )
        .scalar()
        or 0
    )

    successful_logins = (
        db.query(func.count(SecurityEvent.id))
        .filter(
            SecurityEvent.event_type.ilike("login"),
            SecurityEvent.status.ilike("success"),
        )
        .scalar()
        or 0
    )

    return {
        "total_events": total_events,
        "suspicious_events": suspicious_events,
        "failed_logins": failed_logins,
        "successful_logins": successful_logins,
    }

