#app/main.py
from fastapi import FastAPI
from app.api.v1.api import api_router
# from fastapi import FastAPI, HTTPException,status,Response
# from enum import Enum
# from typing import Optional
from app.core.database import engine,Base
# from .models import user

Base.metadata.create_all(bind=engine)
app = FastAPI(title="User Registration API")

# # Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Registration API"}

# import MySQLdb


# @app.get("/")
# def read_root():
#     try:
#         conn = MySQLdb.connect(
#             host="srv1273.hstgr.io",
#             user="u272046168_rpsingh1421",
#             passwd="Monu@1857",
#             db="u272046168_pms"
#         )
#         print("Connected successfully!")
#         conn.close()
#     except MySQLdb.Error as e:
#         print(f"Error connecting to MySQL Platform: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)