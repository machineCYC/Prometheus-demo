import os

import prometheus_client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

total_requests = Counter('request_count', 'Total webapp request count')

@app.get('/metrics/request_count')
async def requests_count():
    return prometheus_client.generate_latest(total_requests)

@app.get("/")
async def root():
    total_requests.inc()
    return {'message':"This is api server"}
