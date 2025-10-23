import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	running = True

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)


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

		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print('Game over!')
				sys.exit(0)

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.is_colliding(shot):
					asteroid.split()
					shot.kill()

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == '__main__':
	main()

