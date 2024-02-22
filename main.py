from fastapi import FastAPI

from app.api.routes import load_data, preprocessing, analysis, app_output
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version=settings.api_version,
    root_prefix=settings.api_prefix
)


app.include_router(load_data.router, prefix='/load_data', tags=["load_data"])
app.include_router(preprocessing.router, prefix='/preprocessing', tags=["preprocessing"])
app.include_router(analysis.router, prefix='/analysis', tags=["analysis"])
app.include_router(app_output.router, prefix='/app_output', tags=["app_output"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)