# pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = "cuda"

model_name = "yentinglin/Taiwan-LLM-7B-v2.0.1-chat"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, device_map="auto").to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print()

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {"role": "system", "content": "你是一個人工智慧助理",},
    {"role": "user",   "content": "東北季風如何影響台灣氣候？"},
]
inputs_ids = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)

generated_ids = model.generate(inputs_ids, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])