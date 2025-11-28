from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My FastAPI App", version="1.0.0")


# ----- Request/Response Model -----
class Item(BaseModel):
    name: str
    price: float


# ----- Routes -----
@app.get("/")
def root():
    return {"message": "Hello from FastAPI inside Docker!"}


@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item received",
        "item": item
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


# ----- Local Development Entry -----
# ※ 本段不會被 Docker CMD 使用，但你在本機可以直接 `python main.py` 執行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
