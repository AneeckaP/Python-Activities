import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT=500,500
display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Adding Image and background image")

background_image=pygame.transform.scale(
    pygame.image.load('image.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

text=pygame.font.Font(None,36).render("Hello Aneecka",
                                      True, pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            display_surface.blit(background_image, (0,0))
            display_surface.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(30)

game_loop()
