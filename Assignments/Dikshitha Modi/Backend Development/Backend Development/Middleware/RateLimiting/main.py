# redis_rate_limiter.py

import redis
from fastapi import Request
from fastapi.responses import JSONResponse

redis_client = redis.Redis(host="localhost", port=6379, db=0)

def register_rate_limit_middleware(app):

    @app.middleware("http")
    async def rate_limit_middleware(request: Request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"

        LIMIT = 5
        WINDOW = 60  # seconds

        current = redis_client.get(key)

        if current and int(current) >= LIMIT:
            return JSONResponse(
                status_code=429,
                content={"error": "Too Many Requests"}
            )

        pipe = redis_client.pipeline()
        pipe.incr(key, 1)
        pipe.expire(key, WINDOW)
        pipe.execute()

        response = await call_next(request)
        return response
