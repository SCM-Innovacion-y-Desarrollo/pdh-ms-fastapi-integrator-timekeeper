from fastapi import FastAPI

app = FastAPI(
    title="Timekeeper integrator",
    description="This is the integrator service for timekeeper db",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {'status': 'ok'}


    


