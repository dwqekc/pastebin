from models.core import interface
import random

class pastecommand:
    r = interface.redis()

    @classmethod
    async def paste(cls, data):
        while True:
            link = random.randint(0,100000000000000)
            if not await cls.r.get(link):
                await cls.r.set(link,data)
                return {"bin":link,"data":data}