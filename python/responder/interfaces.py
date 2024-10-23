from abc import ABC, abstractmethod

class ResponseGenerator(ABC):
    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        pass