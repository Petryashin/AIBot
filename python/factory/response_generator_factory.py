from python.responder.llama_response_generator import LlamaResponseGenerator
from python.responder.mock_response_generator import MockResponseGenerator
from python.factory.load_config import load_config

class ResponseGeneratorFactory:
    @staticmethod
    def create_response_generator():
        config =load_config()
        model_name = config.get("model_name")
        use_mock = config.get("use_mock", False)

        if use_mock:
            return MockResponseGenerator()
        return LlamaResponseGenerator(model_name)