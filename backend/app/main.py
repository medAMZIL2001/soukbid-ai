from typing import Literal

from fastapi import FastAPI

app = FastAPI(title="SoukBid AI", version="0.1.0")


@app.get("/health", tags=["system"])
async def health() -> dict[str, Literal["ok"]]:
    """Report that the HTTP process is responding."""
    return {"status": "ok"}
