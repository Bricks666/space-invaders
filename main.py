import pygame
from consts.main import HEIGHT, WIDTH
from database.db import DB
from game import Game
from stores.level import LevelStore
from stores.lives import LivesStore
from stores.scores import ScoresStore


def main():
    pygame.init()
    db = DB()
    db.init()
    max_score = 0
    max_scores = db.scores_table.get_best_score()
    if len(max_scores) > 0:
        max_score = max_scores[0][0]

    ScoresStore(max_score)
    LevelStore()
    LivesStore()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
