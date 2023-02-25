import asyncio

from functii.bazadedate import ConectareLaMySQL
from gui.login import *

async def main():
    await ConectareLaMySQL.mysql()
    await MeniuLogin()

asyncio.run(main())
