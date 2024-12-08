import numpy
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')
clusters = numpy.load('notebooks/vectors.npy')
descriptions  = ["Shopping", "Others", "CashBack", "Gaming", "Experience", "Marketing", "Camera/Photo", "Learning/Wellness", "Social/Dating", "Learning/Music", "Creativity", "Brief", "Fitness/Wellness/Healthy", "Photo/Content creation", "Others", "Singing/Voice", "Walking", "Audio", "Fashion", "Blissim"]

app = FastAPI()

class Campaign(BaseModel):
    product_name: str = "My product"
    short_description: str = "lorem"
    long_description: str = "ipsum"

@app.post("/cluster")
async def root(c: Campaign):
    embed: list = model.encode(c.short_description).tolist()
    dist: list[float] = [numpy.linalg.norm(numpy.array(embed)-c) for c in clusters]
    cluster: int = dist.index(min(dist))
    return {"cluster": cluster, "description": descriptions[cluster]}
