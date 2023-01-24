from fastapi import FastAPI
from routes import productRoute, usersRoute, comprasRoute

app = FastAPI()

app.include_router(usersRoute.users)
app.include_router(productRoute.product)
app.include_router(comprasRoute.compra)

@app.get("/")
async def root():
    return {"message": "Hi, I'm the root of the API"}