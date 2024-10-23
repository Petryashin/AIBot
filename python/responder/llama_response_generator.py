import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from python.responder.response_generator import ResponseGenerator


class LlamaResponseGenerator(ResponseGenerator):
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            token=True,
        )
        quantization_config = BitsAndBytesConfig(
            load_in_8bit=True,
            llm_int8_enable_fp32_cpu_offload=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            token=True,
            quantization_config=quantization_config,
            torch_dtype=torch.float16
        )

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def generate_response(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(self.device)

        outputs = self.model.generate(
            **inputs,
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.eos_token_id
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == '__main__':
    m = "Vikhrmodels/Vikhr-Llama-3.2-1B-Instruct"
    g = LlamaResponseGenerator(m)
    print(g.generate_response("кто такой ленин"))
