from main import *

class PlatMovingCastle(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/spikes/Individual Spike.png"),(32, 32)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.speed = 7
        self.vel = pygame.Vector2((-2000, 0))
        self.onGround = False
        self.count = 0

    def update(self):
        self.vel.x += 1 * self.speed
        super().update(x=self.vel.x)



    def collide(self, platforms, xvel, yvel):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.vel.x *= -1
                super().update(x=self.vel.x)



class PlatLevelEnd(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)

class PlatFreeStick(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel2(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel3(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel4(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel5(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel6(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatLevel7(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)


class PlatBasic(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)

class PlatCoinsNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)



class PlatBasicFree(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/Background_images/wall_basic.png"), (32, 32)).convert_alpha()

class PlatCoins(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/Background_images/wall_basic.png"), (32, 32)).convert_alpha()






class PlatExit(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)


class PlatExitNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)



class PlatExitFreeUp(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/spikes/Individual Spike.png"), (32, 32)).convert_alpha()

class PlatExitFreeLeft(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/spikes/Individual Spike.png"), (32, 32)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)

class PlatExitFreeRight(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/spikes/Individual Spike.png"), (32, 32)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)

class PlatExitFreeDown(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/spikes/Individual Spike.png"), (32, 32)).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)


class PlatSpeedF(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatSpeedH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatSpeedM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatSpeedL(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)
        self.image = pygame.transform.scale(pygame.image.load("Images/Background_images/wall_basic.png"), (32, 32)).convert_alpha()

class PlatNormNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)



class PlatJumpH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatJumpM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatImmune(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatNext(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)