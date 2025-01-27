import uvicorn
from fastapi import FastAPI
from decouple import config

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def read_root():
    app_env = config("APP_ENV", default="development")
    return {"message": f"Current environment: {app_env}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
