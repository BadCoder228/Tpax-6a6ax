from car_hood.spam.tg_spam import services as urls_tg
from car_hood.spam.sms_spam import service as urls_sms
from aiohttp import ClientSession
import asyncio

''' запросы к сервисам '''
async def req(session, url):
    try:
        async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
            return await response.text()
    except:
        pass

''' сортировка запросов '''
async def starting(number, tg):
    async with ClientSession() as session:
        services = (urls_sms(number) + urls_tg(number)) if tg else (urls_sms(number))
        tasks = [asyncio.ensure_future(req(session, service)) for service in services]
        await asyncio.gather(*tasks)
