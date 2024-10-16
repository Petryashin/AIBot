import asyncio
from worker.worker import start_worker
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting main.go")
    asyncio.run(start_worker())