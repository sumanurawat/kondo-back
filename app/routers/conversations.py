from fastapi import APIRouter, Depends, HTTPException, status
from google.cloud.firestore_v1 import Client
from loguru import logger
from app.database import firestore_db
from app.models import ConversationCreate, ConversationResponse
from app.routers.openai_utils import generate_title

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
    responses={404: {"description": "Not found"}},
)

conversations_collection = firestore_db.collection("conversations")


@router.post("/", response_model=ConversationResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(conversation: ConversationCreate):
    """
    Create a new conversation.
    """
    new_conversation_ref = conversations_collection.document()
    new_conversation = conversation.dict()
    title = generate_title(new_conversation.get('first_message'))
    new_conversation["title"] = title
    # save new conversation
    new_conversation_ref.set(new_conversation)
    response = {
        "conversation_id": new_conversation_ref.id,
        "title": title
    }
    return response
