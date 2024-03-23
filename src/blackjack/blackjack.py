from fastapi import (
    FastAPI,
)
from fastapi.responses import RedirectResponse
import uvicorn

from blackjack.apis.deck import router as deck_router
from blackjack.apis.player import router as player_router

app = FastAPI(
    title=__name__,
    version='0.1.0'
)

app.include_router(deck_router)
app.include_router(player_router)


@app.get(
    '/'
)
def hi():
    return RedirectResponse('/docs')


def main():
    uvicorn.run(
        'blackjack.blackjack:app',
        reload=True
    )


if __name__ == '__main__':
    main()
