from fastapi import FastAPI, APIRouter
from routers import (
    auth_router,
    transaction_router,
    work_router,
    block_router,
    performance_router,
    reward_router,
    miner_router
)

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    app = FastAPI(
        title="Mining Pool API",
        description="API for managing mining pool operations",
        version="1.0.0"
    )

    api_router = APIRouter(prefix="/api")

    api_router.include_router(auth_router.router, prefix="/auth")
    api_router.include_router(transaction_router.router, prefix="/transactions")
    api_router.include_router(work_router.router, prefix="/work")
    api_router.include_router(block_router.router, prefix="/block")
    api_router.include_router(performance_router.router, prefix="/performance")
    api_router.include_router(reward_router.router, prefix="/rewards")
    api_router.include_router(miner_router.router, prefix="/miners")

    app.include_router(api_router)

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
