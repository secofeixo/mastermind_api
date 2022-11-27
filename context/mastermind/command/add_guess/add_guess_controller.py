from shared.base_controller import BaseController
from shared.base_exception import BaseException
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi_utils.cbv import cbv
from context.mastermind.command.add_guess.add_guess_dto import AddGuessDto, AddGuessBody, ResponseAddGuess
from context.mastermind.command.add_guess.add_guess import AddGuessCommand
from context.mastermind.infrastructure.game_repository import IGameRepository
from shared.base_message import Message
from shared.dependencies import gameRepo

router = APIRouter(tags=["Game"], prefix="")


@cbv(router)
class AddGuessController(BaseController):
    def initialize(self, app):
        super().initialize(app)
        self.fastapi_app.include_router(router=router)

    @router.post(
        "/game/{game_id}/guess",
        summary="Add a new guess to the game",
        response_model=ResponseAddGuess,
        responses={
            200: {
                "description": "Add and check if the guess is correct in the game.",
            },
            400: {"model": Message, "description": "Bad request. There are any error in parameters"},
            500: {"model": Message, "description": "Internal server error."}
        }
    )
    def add_guess(self,
                  game_id: str,
                  add_guess_body: AddGuessBody,
                  add_guess_repo: IGameRepository = Depends(gameRepo)) -> JSONResponse:
        add_guess_command = AddGuessCommand(game_repository=add_guess_repo)
        add_guess_dto = AddGuessDto(game_id=game_id, code=add_guess_body.code)
        try:
            guess_result = add_guess_command.run(add_guess_dto)
            response = ResponseAddGuess(black_pegs=guess_result.black_pegs,
                                        white_pegs=guess_result.white_pegs,
                                        correct=guess_result.correct,
                                        status=guess_result.current_status)
            return JSONResponse(content=response.dict())
        except BaseException as e:
            return JSONResponse(content={"message": e.message}, status_code=e.status)
        except Exception as exception:
            print("add_guess", exception)
            return JSONResponse(content={"message": "Internal error"}, status_code=500)
