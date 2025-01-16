import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,ASTEROID_KINDS,ASTEROID_MAX_RADIUS,ASTEROID_MIN_RADIUS,ASTEROID_SPAWN_RATE
from player import Player 
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

	Asteroids.containers = (asteroids, updatable, drawable) 	

	AsteroidField.containers = (updatable)
	asteroidField = AsteroidField()	

	Shot.containers = (shots, updatable, drawable)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")
		for entity in updatable:
			entity.update(dt)
		for asteroid in asteroids:
			if asteroid.is_colliding(player):
				print("Game Over!")
				quit()
		for asteroid in asteroids:
			for bullet in shots:
				if asteroid.is_colliding(bullet):
					bullet.kill()
					asteroid.split()
		for entity in drawable:
			entity.draw(screen)
		
		pygame.display.flip()	
		dt = clock.tick(60) / 1000
		
		




















if __name__ == "__main__":
	main()