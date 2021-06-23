import uvicorn
import os
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

SENTRY_DSN=os.getenv('SENDRY_DSN')

sentry_sdk.init(dsn=SENTRY_DSN, environment='local')
app.add_middleware(SentryAsgiMiddleware)

@app.get("/error/1")
async def e1():
    1/0
    
@app.get("/error/2")
async def e2():
    raise StarletteHTTPException(500, 'starlette exception test')

@app.get("/error/3")
async def e3():
    raise HTTPException(500, 'fastapi execption')

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("debug:app", host="0.0.0.0", port=8000, reload=True)
