# add models for client (request / response)
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field
from typing_extensions import Literal


class ConversationCreate(BaseModel):
    first_message: str
    user_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source: Literal["TEST", "BINDER"]
    source_id: str


class ConversationResponse(BaseModel):
    conversation_id: str
    title: str
