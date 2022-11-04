import time
import pygame

## Show some text fade in/out
def moving_screen():
    FADE_IN_TIME = 3
    FADE_OUT_TIME = 1
    FADE_IN_EASING = lambda x: x  # Linear



    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = 1280, 736
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Comic Sans MS', 160, True)
    background2 = pygame.transform.scale(pygame.image.load("Images/download.jpg"), (1280, 736))
    rendered_text2 = pygame.transform.scale(pygame.image.load("screenshot2.jpg"), (1280, 736))
    death_screen = (pygame.image.load("screenshot.jpg"))
    mid_screen = pygame.transform.scale(pygame.image.load("Images/download.jpg"), (1280, 736))
    rendered_text1 = font.render("", True, (255, 0, 0))

    text_rect = rendered_text1.get_rect(center=(width / 2, height / 2))
    ST_FADEIN = 0
    ST_FADEOUT = 1


    state = ST_FADEIN
    last_state_change = time.time()

    count = 0
    while count == 0:

        screen.blit(death_screen, (0, 0))
        state_time = time.time() - last_state_change

        if state == ST_FADEIN:
            if state_time >= FADE_IN_TIME:
                state = ST_FADEOUT
                state_time -= FADE_IN_TIME
                last_state_change = time.time() - state_time

        elif state == ST_FADEOUT:
            if state_time >= FADE_OUT_TIME:
                count = 1


        if state == ST_FADEIN:
            alpha = FADE_IN_EASING(1.0 * state_time / FADE_IN_TIME)
            rt = rendered_text1
        elif state == ST_FADEOUT:
            alpha = FADE_IN_EASING(1.0 * state_time / FADE_IN_TIME)

        surf2 = pygame.surface.Surface((text_rect.width, text_rect.height))



        if state == ST_FADEIN:
            surf2.blit(rt, (0, 0))
            screen.blit(background2, (0, 0))
            surf2.set_alpha(255 * alpha)
            background2.set_alpha((400 * alpha))
            screen.blit(surf2, text_rect)

        if state == ST_FADEOUT:
            screen.blit(mid_screen, (0, 0))
            rendered_text2.set_alpha(1200 * alpha)
            screen.blit(rendered_text2, (0, 0))




        pygame.display.flip()
        clock.tick(60)