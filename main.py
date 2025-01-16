import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
	running = True
	while running:
		for event in pygame.event.get():
			print(event.type)
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		pygame.display.flip()	





















if __name__ == "__main__":
	main()