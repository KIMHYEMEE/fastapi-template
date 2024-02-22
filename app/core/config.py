from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App settings
    app_name: str = "Project Name"
    debug: bool = True # debug mode

    # FastAPI settings
    api_version: str = "v1"
    api_prefix: str = "/api"

settings = Settings()