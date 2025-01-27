import uvicorn
from fastapi import FastAPI
from decouple import config
from data import ContentsServiceAPI

app = FastAPI()


@app.get("/")
def read_root():
    app_env = config("APP_ENV", default="development")
    return {"message": f"Current environment: {app_env}"}


@app.get("/announcement")
def get_announcement():
    api = ContentsServiceAPI()
    return api.getAnnouncementList()


@app.get("/notice")
def get_notice():
    api = ContentsServiceAPI()
    return api.getNoticeList()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
