import pygame
from consts.main import HEIGHT, WIDTH
from database.db import db
from game import Game
from stores.scores import scores


def main():
    pygame.init()
    db.init()
    max_scores = db.scores_table.get_best_score()
    if len(max_scores) > 0:
      scores.init(max_scores[0][0])
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(screen)
    game.init()
    game.start()


if __name__ == "__main__":
    main()
