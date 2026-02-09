@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = SessionLocal()
    try:
        response = await call_next(request)
        request.state.db.commit()
    except Exception as e:
        request.state.db.rollback()
        raise e
    finally:
        request.state.db.close()
    return response
