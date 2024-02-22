from pydantic_settings import BaseSettings

class Directories(BaseSettings):

    data: str = 'app/data'


dirs = Directories()