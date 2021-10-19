import pygame

from class_background import Background
from class_dinosaur import Dinosaur
from class_tree import Tree

# tao man console rong 600 cao 300
pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("dinosaur")

# tao bien can dung trong truong trinh
endGame =  False
clock = pygame.time.Clock()

# khoi tao object mau
background1 = Background(0, 0, "background.jpg")
background2 = Background(0, 0, "background.jpg")
tree = Tree(550, 230, "tree.png")
dinosaur = Dinosaur(20, 230, "dinosaur.png")

# ham load anh
def LoadImage():
    background_load = screen.blit(background1.pic, (background1.x_pos, background1.y_pos))
    background2_load = screen.blit(background2.pic, (background1.x_pos + 600, background2.y_pos))
    tree_load = screen.blit(tree.pic, (tree.x_pos, tree.y_pos))
    dinosau_load = screen.blit(dinosaur.pic, (dinosaur.x_pos, dinosaur.y_pos))

# vong lap game
while endGame == False:
    clock.tick(120)                         # gioi han cho truong trinh chay 120f/s
    screen.fill((255, 255, 255))            # do mau cho man hinh thanh trang
    LoadImage()                             # load anh qua moi frame
    background1.Movement()

    # quit game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endGame = True
        pygame.display.flip()
pygame.quit                            