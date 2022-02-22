import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import trialroute
# app object for permission
from utils.app_exceptions import AppExceptionCase, app_exception_handler

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(trialroute.router)


# decorator
@app.get("/")
async def root():
    return {"Ping": "Pong"}


if __name__ == "__main__":
    uvicorn.run("server.app:app",  reload=True)
