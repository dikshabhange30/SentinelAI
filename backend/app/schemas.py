


from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SecurityEventCreate(BaseModel):
    username: str | None = Field(default=None, max_length=100)
    source_ip: str | None = Field(default=None, max_length=45)
    event_type: str = Field(min_length=1, max_length=50)
    status: str = Field(min_length=1, max_length=20)
    timestamp: datetime | None = None


class SecurityEventResponse(BaseModel):
    id: int
    timestamp: datetime
    username: str | None
    source_ip: str | None
    event_type: str
    status: str
    is_suspicious: bool

    model_config = ConfigDict(from_attributes=True)
