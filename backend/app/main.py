from fastapi import FastAPI
from .routers import clusters

app = FastAPI(title="Dashboard API")

app.include_router(clusters.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Dashboard API"}
