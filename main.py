import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	running = True

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)

	player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
	field = AsteroidField()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		for member in drawable:
			member.draw(screen)
		updatable.update(dt)

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == '__main__':
	main()

