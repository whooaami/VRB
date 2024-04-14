import pathlib
import tomli

from fastapi import (
    FastAPI,
)
from fastapi.responses import (
    RedirectResponse,
)
from app.config import (
    get_settings,
)
from app.routes import (
    router,
)

project_toml_path = pathlib.Path("pyproject.toml")


project_toml = tomli.loads(project_toml_path.read_text())

CFG = get_settings()
API_VERSION = project_toml["tool"]["poetry"]["version"]
app = FastAPI(version=API_VERSION)
app.include_router(router)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
