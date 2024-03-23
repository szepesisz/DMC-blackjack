from fastapi import (
    FastAPI
)
import uvicorn

from blackjack.apis.deck import router as deck_router

app = FastAPI(
    title=__name__,
    version='0.1.0'
)

app.include_router(deck_router)


def main():
    uvicorn.run(app)


if __name__ == '__main__':
    main()
