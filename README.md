# fastapi-exception-test

SentryAsgiMiddleware does not capture HTTPException

### Run
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Result 
$ curl -s http://0.0.0.0:8000/
{"message":"Hello World"}

$ curl -s http://0.0.0.0:8000/error/1            # sentry captures
Internal Server Error

$ curl -s http://0.0.0.0:8000/error/2            # sentry does NOT capture
{"detail":"starlette exception test"}

$ curl -s http://0.0.0.0:8000/error/3            # sentry does NOT capture
{"detail":"fastapi execption"}
```
