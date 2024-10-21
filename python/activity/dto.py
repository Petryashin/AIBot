from dataclasses import dataclass

@dataclass
class AIRequest:
    text: str

@dataclass
class AIResponse:
    response: str