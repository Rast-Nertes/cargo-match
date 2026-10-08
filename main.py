"""Точка входа: запуск ASGI-сервера FastAPI."""

from pathlib import Path

import uvicorn

BACKEND_DIR = Path(__file__).resolve().parent / "backend"


def main() -> None:
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        app_dir=str(BACKEND_DIR),
    )


if __name__ == "__main__":
    main()
