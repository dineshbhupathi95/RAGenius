from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging
from app.api.router import chat


def create_app() -> FastAPI:
     # Setup logging
    setup_logging()

    app = FastAPI(
        title="RAGenius",
        description="A Retrieval-Augmented Generation (RAG) system built with FastAPI and LangChain.",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(chat.router, prefix="/api/v1",tags=["Chat"])


    return app


app = create_app()


@app.on_event("startup")
async def startup_event():
    print("Starting up RAGenius...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down RAGenius...")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8092,
        reload=True,
    )