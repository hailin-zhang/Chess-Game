import pygame
from classes.board.chessBoard import ChessBoard
pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

x = ChessBoard()
x.print_board()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        clock.tick(60)