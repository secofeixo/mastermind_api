from context.mastermind.infrastructure.game_repository_in_memory import GameRepositoryInMemory

# Dependency injection
dependencies = {
    "gameRepo": GameRepositoryInMemory(),
}


def gameRepo():
    return dependencies["gameRepo"]
