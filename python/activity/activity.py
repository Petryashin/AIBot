from temporalio import activity
import logging

@activity.defn
async def GetAIAnswer(data: dict) -> dict:
    message = data.get("Text", "")

    logging.info(f"Execute activity GetAIAnswer for Text {message}")

    return {"Response": f"Processed message: {message}"}