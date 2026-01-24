from fastapi import FastAPI

from api.v1.router import router as v1_router

app = FastAPI(version="1.0.0", title="Gerenciador de Links API")

app.include_router(v1_router)


@app.get("/status/")
def status():
    return {"msg": "Aqui tá rodando"}
