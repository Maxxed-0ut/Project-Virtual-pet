import sys;
import pygame;
import json;
import os;


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Virtual Pet")


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

 

def save_data(hunger, happiness):
    with open("pet_data.json", "w") as f:
        json.dump({"hunger": hunger, "happiness": happiness}, f)

def load_data():
    if os.path.exists("pet_data.json"):
        with open("pet_data.json", "r") as f:
            data = json.load(f)
            return data.get("hunger", 100), data.get("happiness", 100)
    return 100, 100  # default values

hunger, happiness = load_data()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PET_COLOR = (255, 200, 200)
HAPPY_COLOR = (100, 255, 100)
SAD_COLOR = (255, 100, 100)


feed_button = pygame.Rect(100, 300, 150, 50)
play_button = pygame.Rect(350, 300, 150, 50)

image = pygame.image.load("Pet.png")  
image = pygame.transform.scale(image, (50, 50))  # Resize the image to fit the pet size


image_rect = image.get_rect(center=(800//2, 600//2 - 50))
screen.blit(image, image_rect)


running = True
while running:
    screen.fill(WHITE)

    
    pet_color = HAPPY_COLOR if happiness >= 7 else SAD_COLOR if happiness <= 3 else PET_COLOR

    # Draw pet
    screen.blit(image, (800//2, 600//2 - 50))

    # Draw hunger and happiness bars
    hunger_text = font.render(f"Hunger: {hunger}/100", True, BLACK)
    happiness_text = font.render(f"Happiness: {happiness}/100", True, BLACK)
    screen.blit(hunger_text, (20, 20))
    screen.blit(happiness_text, (20, 60))

    # Draw buttons
    pygame.draw.rect(screen, (100, 200, 255), feed_button)
    pygame.draw.rect(screen, (255, 200, 100), play_button)
    screen.blit(font.render("Feed", True, BLACK), (feed_button.x + 40, feed_button.y + 10))
    screen.blit(font.render("Play", True, BLACK), (play_button.x + 40, play_button.y + 10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if feed_button.collidepoint(event.pos):
                hunger = max(0, hunger + 2)
            elif play_button.collidepoint(event.pos):
                happiness = min(100, happiness + 2)
                hunger = min(100, hunger - 1)  # playing makes them hungry

    # Auto tick: pet gets hungrier and sadder over time
    if pygame.time.get_ticks() % 1000 < 20:  # once per second-ish
        hunger = max(0, hunger - 1)
        happiness = max(0, happiness - 1)

    pygame.display.flip()
    clock.tick(60)

if event.type == pygame.QUIT:
    save_data(hunger, happiness)
    running = False


pygame.quit()
sys.exit()

    

    