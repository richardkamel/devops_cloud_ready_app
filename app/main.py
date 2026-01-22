from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
import time

app = FastAPI(title="DevOps Cloud Ready App", version="1.0.0")

# --- Prometheus metrics ---
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests",
    ["endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

USERS = [
    {"id": 1, "name": "Alice", "role": "Dev"},
    {"id": 2, "name": "Bob", "role": "DevOps"},
    {"id": 3, "name": "Charlie", "role": "Recruiter"},
]


@app.get("/health")
def health():
    endpoint = "/health"
    start = time.time()
    try:
        return {"status": "ok"}
    finally:
        REQUEST_COUNT.labels(endpoint=endpoint).inc()
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start)


@app.get("/users")
def users():
    endpoint = "/users"
    start = time.time()
    try:
        return {"count": len(USERS), "users": USERS}
    finally:
        REQUEST_COUNT.labels(endpoint=endpoint).inc()
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start)


@app.get("/metrics")
def metrics():
    endpoint = "/metrics"
    start = time.time()
    try:
        data = generate_latest()
        return Response(content=data, media_type=CONTENT_TYPE_LATEST)
    finally:
        REQUEST_COUNT.labels(endpoint=endpoint).inc()
        REQUEST_LATENCY.labels(endpoint=endpoint).observe(time.time() - start)
