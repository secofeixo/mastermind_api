from shared.base_controller import BaseController
from shared.base_exception import BaseException
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from context.mastermind.queries.get_game import GetGameQuery
from context.mastermind.queries.get_game_dto import ResponseGetGame
from context.mastermind.infrastructure.game_repository import IGameRepository
from shared.dependencies import gameRepo
from shared.base_message import Message

router = APIRouter(tags=["Game"], prefix="")


@cbv(router)
class GetGameController(BaseController):
    def initialize(self, app):
        super().initialize(app)
        self.fastapi_app.include_router(router=router)

    @router.get(
        "/game/{game_id}",
        summary="Get details of the game",
        response_model=ResponseGetGame,
        responses={
            200: {
                "description": "Return the details of the game",
            },
            400: {"model": Message, "description": "Bad request. There are any error in parameters"},
            500: {"model": Message, "description": "IInternal server error."}
        }
    )
    async def create_game(self,
                          game_id: str,
                          getGameRepo: IGameRepository = Depends(gameRepo)) -> JSONResponse:
        get_game_query = GetGameQuery(game_repository=getGameRepo)
        try:
            new_game = get_game_query.run(game_id)
            response = ResponseGetGame.fromEntity(new_game)
            return JSONResponse(content=response.dict())
        except BaseException as e:
            return JSONResponse(content={"message": e.message}, status_code=e.status)
        except Exception as exception:
            print("get_game", exception)
            return JSONResponse(content={"message": "Internal error"}, status_code=500)
