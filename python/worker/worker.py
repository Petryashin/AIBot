from temporalio.client import Client
from temporalio.worker import Worker
from python.activity.activity import GetAIAnswer
import logging

logging.basicConfig(level=logging.INFO)

async def start_worker():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="AI-message-python",
        activities=[GetAIAnswer],
    )

    logging.info("Worker started and waiting for activities...")

    await worker.run()