import env_file_reader
from fastapi import FastAPI
from routes.firmeneintrag import router as firmeneintrag_router
import uvicorn

app = FastAPI()


app.include_router(firmeneintrag_router)
# app.include_router(rego_router)
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
