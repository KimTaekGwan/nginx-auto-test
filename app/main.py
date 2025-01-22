from fastapi import FastAPI
from decouple import config

app = FastAPI()


@app.get("/")
def read_root():
    app_env = config("APP_ENV", default="development")
    return {"message": f"Current environment: {app_env}"}
