from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn.functional as F

torch.set_default_device("mps")

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# res = classifier("We are very happy to show you the 🤗 Transformers library.")

# print(res)

# print("======================= Try tokenizer!!! =======================")
# sequence = "Try to use Transformers for NLP tasks, Is that simple?"
# res = tokenizer(sequence)

# print("--------- tokenizer(sequence) ---------")
# print(res)

# print("--------- tokenizer.tokenize(sequence) ---------")
# tokens = tokenizer.tokenize(sequence)
# print(f"tokens: {tokens}")

# print("--------- input_ids ---------")
# input_ids = tokenizer.convert_tokens_to_ids(tokens)
# print(input_ids)

# print("--------- decode: input_ids ---------")
# print(tokenizer.decode(input_ids))  # Decode back to string

# print("End  Try tokenizer!!! ")

# print("======================= Try pytorch!!! =======================")
# X_train = ["I just need to learn huggingface transformers", "I love you"]

# res = classifier(X_train)
# print(res)

# batch = tokenizer(X_train, padding=True, truncation=True, max_length=512, return_tensors="pt")

# with torch.no_grad():
#     outputs = model(**batch)
#     print(f"outputs: {outputs}")
#     predictions = F.softmax(outputs.logits, dim=1)
#     print(f"predictions: {predictions}")
#     labels = torch.argmax(predictions, dim=1)
#     print(f"labels: {labels}")

print("======================= Save model!!! =======================")
save_directory = "./sentiment_model"
# tokenizer.save_pretrained(save_directory)
# model.save_pretrained(save_directory)

print("======================= Load model!!! =======================")
tok = AutoTokenizer.from_pretrained(save_directory)
mod = AutoModelForSequenceClassification.from_pretrained(save_directory)

print(f"tok: {tok}")