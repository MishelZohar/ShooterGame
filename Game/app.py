import pygame

pygame.init()

# Set up the display
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(RESOLUTION)

# Initialize constants
FPS = 144
WHITE = (255, 255, 255) 
UPDATE_TIME = 90 # in miliseconds 

PLAYER_WIDTH = 70
PLAYER_HEIGHT = 60
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_HEIGHT)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        img = pygame.image.load(r"images\\_Mode-Gun\\01-Idle\\E_E_Gun__Idle_000.png").convert_alpha()
        self.image = pygame.transform.scale(img, PLAYER_SIZE)

        # Set the player's rect attributes
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.last_image_change = pygame.time.get_ticks()
        
        self.animation_state = "idle"
        self.image_index = 0


    def update(self):
        current_time = pygame.time.get_ticks()
        
        # Initialize all the keys that makes the player exit from idle mode
        active_keys = [keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN]]
        
        
        if current_time - self.last_image_change >= UPDATE_TIME:
            self.last_image_change = current_time
            self.image_index = (self.image_index + 1) % 10
            
            match self.animation_state:
                case "shot":
                    self.image = pygame.transform.scale(shot_images[self.image_index], PLAYER_SIZE)
                
                case "run":
                    self.image = pygame.transform.scale(run_images[self.image_index], PLAYER_SIZE)
                
                case _:
                    self.image = pygame.transform.scale(idle_images[self.image_index], PLAYER_SIZE)


        if keys[pygame.K_LEFT]:
            self.rect.x -= 1 
            self.animation_state = "run"
                    
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 1
            self.animation_state = "run"
            
        if keys[pygame.K_UP]:
            self.rect.y -= 2
            
        elif keys[pygame.K_DOWN]:
            self.rect.y += 2
            
        if not any(active_keys):
            self.animation_state = "idle"

def initialize_images():
    IMAGES_NUMBER = 10
    
    idle = [pygame.image.load(fr"images\\_Mode-Gun\\01-Idle\\E_E_Gun__Idle_00{index}.png") for index in range(IMAGES_NUMBER)]
    run = [pygame.image.load(fr"images\\_Mode-Gun\\02-Run\\E_E_Gun__Run_000_00{index}.png") for index in range(IMAGES_NUMBER)]
    shot =  [pygame.image.load(fr"images\\_Mode-Gun\\03-Shot\\E_E_Gun__Attack_00{index}.png") for index in range(IMAGES_NUMBER)]
    
    return idle, run, shot



player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Create a sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create a clock object to control the FPS
clock = pygame.time.Clock()

idle_images, run_images, shot_images = initialize_images()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()