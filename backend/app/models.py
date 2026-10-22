
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import declarative_base, mapped_column

Base = declarative_base()


class SecurityEvent(Base):
    __tablename__ = "security_events"

    id = mapped_column(Integer, primary_key=True, index=True)
    timestamp = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    username = mapped_column(String(100), nullable=True)
    source_ip = mapped_column(String(45), nullable=True)
    event_type = mapped_column(String(50), nullable=False)
    status = mapped_column(String(20), nullable=False)
    is_suspicious = mapped_column(Boolean, default=False, nullable=False)
    risk_score = mapped_column(Integer, default=0, nullable=False)
