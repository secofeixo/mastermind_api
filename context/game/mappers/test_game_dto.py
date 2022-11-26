from context.game.mappers.gameDTO import GameDTO
import uuid


def test_creating_dto():
    game_dto = GameDTO(game_id=str(uuid.uuid4()))
    game = game_dto.toEntity()
    assert game.game_id == game_dto.game_id
    assert game.num_guesses == game_dto.num_guesses == 10


def test_creating_dto_num_guesses():
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=5)
    game = game_dto.toEntity()
    assert game.game_id == game_dto.game_id
    assert game.num_guesses == game_dto.num_guesses == 5


def test_adding_guess():
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=5)
    game = game_dto.toEntity()
    for i in range(3):
        game.add_guess('AAAA')
    game_dto.fromEntity(game=game)
    assert game.game_id == game_dto.game_id
    assert game.num_guesses == game_dto.num_guesses == 5
    assert len(game.guesses) == len(game_dto.guesses) == 3
