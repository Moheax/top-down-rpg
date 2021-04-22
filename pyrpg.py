import  pygame

pygame.init()
pygame.display.set_caption('Rpg thingy ig ?~?')
screen = pygame.display.set_mode((1920, 1080))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()

pygame.QUIT()
quit()