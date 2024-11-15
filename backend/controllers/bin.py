from models.core import interface


class binquery:
    r = interface.redis()

    @classmethod
    async def get_bin(cls, bin:str):
        bin = await cls.r.get(bin)
        if bin:
            return bin
        else:
            raise Exception("no such bin")