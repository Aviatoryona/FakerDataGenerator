from fastapi import FastAPI

from generator.name_generator import NameGenerator

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/generate-names/{count}")
async def generateNames(count: int):
    nmg = NameGenerator()
    return nmg.generate_names(count)
