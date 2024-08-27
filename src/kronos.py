import os, requests
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models.paycode import Paycode
from .schemas.paycode_schemas import PaycodeModel
from .repository import create

class KronosPaycodes():
    url = str(os.getenv('DOMAIN_URL'))
    company_slug = str(os.getenv('COMPANY_SLUG'))
    token_company = str(os.getenv('TOKEN_COMPANY'))

    async def get_paycodes_concepts(self, db: AsyncSession):
        result = requests.get(
            url = f'{self.url}/api/v1/kronos_wfc/paycode',
            headers = {
                'Authorization': f'Bearer {self.token_company}',
                'company': self.company_slug,
                'Content-Type': 'application/json'
            }
        )

        paycodes_list = await self.casting(result.json()['data'], db)

        if not isinstance(paycodes_list, list):
            return paycodes_list
        
        return await create(db, Paycode, paycodes_list)
    
    async def casting(self, paycodes: list, db: AsyncSession):
        paycodes_list = []
        paycodes_db = await db.execute(select(Paycode.name))
        paycodes_db = paycodes_db.scalars().all()

        paycodes = [p for p in paycodes if p['name'] not in paycodes_db]
        if paycodes:
            for p in paycodes:
                paycode_structure = {
                    'name': p['name'],
                    'type': '',
                    'unit': 'days' if p['is_days'] == 'true' else 'hours',
                    'enable': True
                }

                paycode_structure['type'] = 'duration' if paycode_structure['unit'] == 'hours' else 'standard'
                paycode = PaycodeModel(**paycode_structure)
                paycodes_list.append(paycode)
            return paycodes_list
        
        return 'paycodes up to date'


        
