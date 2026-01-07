from fastapi import FastAPI, HTTPException
from app.schemas import IntegrationInput, ProductOutput
from app.router import route_product

app = FastAPI()

@app.post("/integrate/product", response_model=ProductOutput)
@app.post("/sync/product", response_model=ProductOutput)  # 👈 alias
async def integrate_product(data: IntegrationInput):
    try:
        return route_product(data.source, data.payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
