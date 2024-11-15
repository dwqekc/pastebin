import aioredis
import os

class interface:

    @classmethod
    def redis(cls):
        return aioredis.from_url(os.getenv("Redis_Url"))