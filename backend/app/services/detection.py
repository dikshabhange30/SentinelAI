



from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models import SecurityEvent


FAILED_LOGIN_THRESHOLD = 5
FAILED_LOGIN_WINDOW_MINUTES = 10


def detect_repeated_failed_logins(
    db: Session,
    source_ip: str,
) -> bool:
    """Return True when an IP has reached the failed-login threshold."""

    cutoff_time = datetime.now(timezone.utc) - timedelta(
        minutes=FAILED_LOGIN_WINDOW_MINUTES
    )

    failed_attempts = (
        db.query(SecurityEvent)
        .filter(
            SecurityEvent.event_type.ilike("login"),
            SecurityEvent.status.ilike("failure"),
            SecurityEvent.source_ip == source_ip,
            SecurityEvent.timestamp >= cutoff_time,
        )
        .count()
    )

    return failed_attempts >= FAILED_LOGIN_THRESHOLD - 1
