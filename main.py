from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://localhost:8000",
#     "http://localhost:8001",
#     "http://localhost:3000",
#     "http://localhost:3001",
#     "http://localhost:3002",
#     "http://localhost:3003",
#     "http://192.168.1.101:3000",
#     "*"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
def read_root():
    return {"Welcome": "Root"}

@app.get("/groups")
async def get_groups() -> dict:
    # groups = meta.GetGroups()
    groups = ['a', 'b', 'c']
    return {"data" : groups}
