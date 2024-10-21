from temporalio import activity
import logging
from python.activity.dto import AIResponse, AIRequest


@activity.defn
async def GetAIAnswer(data: AIRequest) -> AIResponse:
    message = data.text

    logging.info(f"Execute activity GetAIAnswer for Text {message}")

    return AIResponse(message)