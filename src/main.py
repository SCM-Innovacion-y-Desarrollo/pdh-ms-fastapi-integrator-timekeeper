from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .kronos import KronosPaycodes
from .databases import get_db
from .models.paycode import Paycode

app = FastAPI(
    title="Timekeeper integrator",
    description="This is the integrator service for timekeeper db",
    version="0.0.1"
)

@app.get("/")
async def root():
    return {'status': 'ok'}

@app.post('/loading_paycodes_concepts', tags=['Paycodes'])
async def loading_paycodes_concepts(db: AsyncSession = Depends(get_db)):
    kronos = KronosPaycodes()
    paycodes = await kronos.get_paycodes_concepts(db)
    return paycodes

@app.get('/paycodes_ids', tags=['Paycodes'])
async def get_paycodes(db: AsyncSession = Depends(get_db)):
    paycodes = await db.execute(select(Paycode))
    paycodes = paycodes.scalars().all()

    return {f'{p.name}': p.paycode_id for p in paycodes}


    


