from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

app = FastAPI()

class Campaign(BaseModel):
    product_name: str = "My product"
    short_description: str = "lorem"
    long_description: str = "ipsum"

@app.post("/cluster")
async def root(c: Campaign):
    embed: list = model.encode(c.short_description).tolist()
    
    return {"cluster": 0, "description": "a desc"}
