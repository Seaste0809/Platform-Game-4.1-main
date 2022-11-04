import pygame
import pygame.freetype

music = ["Music/typrewriter.mp3"]
pygame.mixer.pre_init()
pygame.mixer.init()

def display_text_animation():


    WINDOW_WIDTH = 1280
    SCREEN = pygame.display.set_mode((1280, 736))
    pygame.init()
    count = 0


    font_color = "#b68f40"
    font = pygame.font.Font("Fonts/font.ttf", 28)
    background = pygame.image.load("screenshot.jpg")

    font_render = font.render('Urgent Transmission', False, (font_color))



    text = ''
    string = "An explosion at the lab has set u free"
    for i in range(len(string)):


        if count == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(music[0]), maxtime=1000)
            count = 0
        count += 1
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(font_render, (420, 50))
        text += string[i]
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH/2, 150)
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(75)

    pygame.image.save(SCREEN, "screenshot.jpg")
    text = ''
    string = "This is your time to escape"
    background = pygame.transform.scale(pygame.image.load("screenshot.jpg"),
                                        (1280, 736)).convert_alpha()
    for i in range(len(string)):
        if count == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(music[0]), maxtime=1000)
            count = 0
        count += 1
        SCREEN.blit(background, (0, 0))
        text += string[i]
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH/2, 250)
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(75)

    pygame.image.save(SCREEN, "screenshot.jpg")
    text = ''
    string = "The explosion has damaged the labs core"
    background = pygame.transform.scale(pygame.image.load("screenshot.jpg"),
                                        (1280, 736)).convert_alpha()
    for i in range(len(string)):
        if count == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(music[0]), maxtime=1000)
            count = 0
        count += 1
        SCREEN.blit(background, (0, 0))
        text += string[i]
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 350)
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(75)

    pygame.image.save(SCREEN, "screenshot.jpg")
    text = ''
    string = "The core will detonate soon. RUN!"
    background = pygame.transform.scale(pygame.image.load("screenshot.jpg"),
                                        (1280, 736)).convert_alpha()
    for i in range(len(string)):
        if count == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(music[0]), maxtime=1000)
            count = 0
        count += 1
        SCREEN.blit(background, (0, 0))
        text += string[i]
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 450)
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(75)

    pygame.image.save(SCREEN, "screenshot.jpg")
    text = ''
    string = "Good Luck"
    background = pygame.transform.scale(pygame.image.load("screenshot.jpg"),
                                        (1280, 736)).convert_alpha()
    for i in range(len(string)):
        if count == 2:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound(music[0]), maxtime=300)
            count = 0
        count += 1
        SCREEN.blit(background, (0, 0))
        text += string[i]
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 550)
        SCREEN.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(75)

    pygame.image.save(SCREEN, "screenshot.jpg")




