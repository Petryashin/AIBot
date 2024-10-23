from python.responder.response_generator import ResponseGenerator

class MockResponseGenerator(ResponseGenerator):
    def generate_response(self, prompt: str) -> str:
        return "This is a mock response to the question: " + prompt