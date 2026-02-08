from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

MODEL_NAME = "Mirikram/bert-ticket-classifier"  

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

id2label = model.config.id2label


class Ticket(BaseModel):
    text: str


@app.post("/predict")
def predict(ticket: Ticket):
    inputs = tokenizer(ticket.text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred_class = torch.argmax(probs, dim=1).item()
    confidence = probs[0][pred_class].item()

    return {
        "department": id2label[pred_class],
        "confidence": round(confidence, 3)
    }