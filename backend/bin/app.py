from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bin.routers.bin import router as bin_router

app = FastAPI(root_path="/api")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=bin_router
)