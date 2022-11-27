from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from context.mastermind.command.add_guess.add_guess_controller import AddGuessController
from context.mastermind.command.create_game.create_game_controller import CreateGameController
from context.mastermind.queries.get_game_controller import GetGameController

description = """
MasterMind API give you the basic endpoint for creating this game

## Overview

You will be able to:

* **Create a new game**
* **Adding guess and getting the response**
* **Getting the current state of a game**

"""

app = FastAPI(
    root_path="/",
    title="MasterMind API",
    description=description,
    version="0.0.1",
    docs_url="/openapi",
    redoc_url="/redoc",
    contact={
        "name": "Alberto Seco",
        "email": "alberto.seco@gmail.com",
    },
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    expose_headers=["*"],
)


@app.on_event('startup')
def on_startup():
    # create routes reading from controller
    add_guess_controller = AddGuessController()
    add_guess_controller.initialize(app)
    create_game_controller = CreateGameController()
    create_game_controller.initialize(app)
    get_game_controller = GetGameController()
    get_game_controller.initialize(app)


@app.get('/server-status')
def get_status():
    return JSONResponse(content={'time': str(datetime.utcnow())})

