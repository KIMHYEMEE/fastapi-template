from pydantic_settings import BaseSettings

class Parameters(BaseSettings):
    param: int


parameters = Parameters()