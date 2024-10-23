from temporalio import activity
import logging
from python.activity.dto import AIResponse, AIRequest
from python.factory.response_generator_factory import ResponseGeneratorFactory

@activity.defn
async def GetAIAnswer(data: AIRequest) -> AIResponse:
    message = data.text

    logging.info(f"Execute activity GetAIAnswer for Text {message}")

    response_generator = ResponseGeneratorFactory.create_response_generator()

    ai_answer = response_generator.generate_response(message)

    return AIResponse(ai_answer)