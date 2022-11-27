from shared.base_controller import BaseController
from shared.base_exception import BaseException
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from context.mastermind.command.create_game.create_game_dto import CreateGameDTO, CreateGameBody, ResponseCreateGame
from context.mastermind.command.create_game.create_game import CreateGameCommand
from context.mastermind.infrastructure.game_repository import IGameRepository
from shared.dependencies import gameRepo
from shared.base_message import Message

router = APIRouter(tags=["Game"], prefix="")


@cbv(router)
class CreateGameController(BaseController):
    def initialize(self, app):
        super().initialize(app)
        self.fastapi_app.include_router(router=router)

    @router.post(
        "/game",
        summary="Create new game",
        response_model=ResponseCreateGame,
        responses={
            200: {
                "description": "Create a new game with a random code, or the code set in the body, and the num of guesses set or 10 by default",
            },
            400: {"model": Message, "description": "Bad request. There are any error in parameters"},
            500: {"model": Message, "description": "IInternal server error."}
        }
    )
    async def create_game(self,
                          create_game_body: CreateGameBody,
                          createGameRepo: IGameRepository = Depends(gameRepo)) -> JSONResponse:
        print(createGameRepo)
        create_game_command = CreateGameCommand(game_repository=createGameRepo)
        create_game_dto = CreateGameDTO(num_max_guesses=create_game_body.num_guesses,
                                        secret_code=create_game_body.code)
        try:
            new_game = create_game_command.run(create_game_dto)
            response = ResponseCreateGame(game_id=new_game.game_id)
            return JSONResponse(content=response.dict())
        except BaseException as e:
            return JSONResponse(content={"message": e.message}, status_code=e.status)
        except Exception as exception:
            print("create_game", exception)
            return JSONResponse(content={"message": "Internal error"}, status_code=500)
