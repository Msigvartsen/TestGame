#THE GAME

import pygame
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
pygame.key.set_repeat(1,10)
from random import randint
def ZEGAME():
	#Window
	pygame.mixer.music.load("ukuluul.wav")





	pygame.mixer.music.play(-1,0)
	FPS = 60
	ScreenW = 800
	ScreenH = 800
	Screen = pygame.display.set_mode((ScreenW,ScreenH))


	#Text
	f = pygame.font.Font(None, 32)
	FlowerCounter = 0
	surf = f.render("Flowers: " + str(FlowerCounter), 1, (255,0,255))
	Flowertext = Rect(350,0,100,100)
	a = pygame.font.Font(None, 32)
	AntHealth = 100
	AntText = a.render("AntHealth: " + str(AntHealth), 1, (250,250,250,250))
	antrect = (150,0,100,100)

	#Background
	Brown = (165,42,42)
	White = (255,255,255)
	GroundClass = Rect(0,700,800,100)
	Box = Rect(550,550,50,50)
	Box1 = Rect(450,450,50,50)
	Box2 = Rect(350,350,50,50)
	Box3 = Rect(0,250,800,40)
	Ceiling = Rect (0,0,0,0)
	BoxList = [Box, GroundClass,Box1,Box2,Box3]
	#DOODADS
	Flower1 = pygame.transform.scale(pygame.image.load("blomst1.png"), (200,200))

	FlowerClass1 = Rect(100,100,50,50)
	FlowerList = [pygame.transform.scale(pygame.image.load("blomst1.png"), (100,100)),
		pygame.transform.scale(pygame.image.load("blomst1.png"), (100,100)),
		pygame.transform.scale(pygame.image.load("blomst1.png"), (100,100))]
	FlowerPosList = [Rect(100,400,50,50),Rect(200,500,50,50),Rect(100,800,50,50)]
	#MOBS

	AntClass = Rect(100,180,100,100)
	AntHealth = 100
	Ant = pygame.transform.flip( pygame.transform.scale(pygame.image.load("ant.png"), (AntClass.w,AntClass.h)),True,False)

	#Player
	PlayerClass = Rect(0,600,100,100)

	Player = pygame.transform.scale(pygame.image.load("alien_standing1.png"), (PlayerClass.w, PlayerClass.h))
	PlayerSpeed = 5
	PlayerWalk = pygame.transform.scale(pygame.image.load("alien_walk1.png"), (PlayerClass.w, PlayerClass.h))
	PlayerIdle = pygame.transform.scale(pygame.image.load("alien_standing1.png"),(PlayerClass.w, PlayerClass.h))
	PlayerShoot = pygame.transform.scale(pygame.image.load("alien_shoot.png"),(PlayerClass.w, PlayerClass.h))
	PlayerBack = pygame.transform.flip(PlayerWalk, True, False)
	PlayerFlipIdle = pygame.transform.flip(PlayerIdle, True, False)
	PlayerFlipShoot = pygame.transform.flip(PlayerShoot, True, False)
	jump = False
	#Projectiles
	Projectiles = []

	class Pew(object):
		def __init__(self,rect,direction):
			self.rect = rect
			self.direction = direction
	maxjump = 500
	#GMAEPLAY
	def jump(self):
		if onTheGround(self):
			self.dy += 20
	antdead = False		
	while (True):

		
		keys = pygame.key.get_pressed()
		walk = False
		shoot = False
		
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				walk = True
				
		#Movement			
		if keys[K_RIGHT]: #or keys [ord('d')]:
		
			PlayerClass.move_ip(1*PlayerSpeed,0)
			
		if keys[K_LEFT]: #or event.key == ord('a'):
			PlayerClass.move_ip(-1*PlayerSpeed,0)
			
		"""if keys[K_UP]: #or event.key == ord('w'):
			PlayerClass.move_ip(0,-1*PlayerSpeed)
			#PlayerClass.move_ip(jump)"""
		"""if keys[K_DOWN]: # or event.key == ord('s'):
			PlayerClass.move_ip(0,1*PlayerSpeed)"""
		if keys[K_SPACE]:
			#PlayerClass.move_ip(0,-5*PlayerSpeed)
			if PlayerClass.collidelist(BoxList) >= 0:
				jump = True
				pygame.mixer.Sound("jump1.wav").play()
			
		if jump and PlayerClass.y >= maxjump:
			
			PlayerClass.move_ip(0,-1*PlayerSpeed)
			if PlayerClass.y == maxjump:
				
				jump = False
			
		elif not jump and not PlayerClass.bottom == BoxList[PlayerClass.collidelist(BoxList)].top+5: #and not PlayerClass.collidelist(BoxList) >= 0: 
			print (str(PlayerClass.bottom) + " " +str(BoxList[PlayerClass.collidelist(BoxList)].top ))#not PlayerClass.collidelist(BoxList) >= 0 :
			PlayerClass.move_ip(0,1*PlayerSpeed)
		elif PlayerClass.collidelist(BoxList) >= 0 :
			maxjump = PlayerClass.y -100
			
		#SHOOT	
		if keys[ord('g')]:
			shoot = True
			pygame.mixer.Sound("shoot.wav").play()
			
			
			if keys[K_LEFT]:
				direction = -1
			else:
			
				direction = 1
					
			Projectiles.append(Pew(pygame.Rect(PlayerClass.centerx+20, PlayerClass.centery+10,5,5), direction))			
		Screen.fill(Brown)
		#Ground = pygame.draw.rect(Screen, White, GroundClass)
		for box in BoxList:
			 pygame.draw.rect(Screen,White,box)
		
		for projectile in Projectiles:
			
			projectile.rect.move_ip(projectile.direction * randint(1,200),0 )
			pygame.draw.rect(Screen,White, projectile, 0)
			
		if AntClass.collidelist(Projectiles) >= 0:
			AntHealth -= 1
			
			print (AntHealth)
			
		if shoot:
			
			if keys[K_LEFT]:
				Player = PlayerFlipShoot
			else:		
				Player = PlayerShoot
			
		elif walk and int(pygame.time.get_ticks() / 200) %2 == 0:
			if keys[K_LEFT]:
				Player = PlayerBack
			else:		
				Player = PlayerWalk
			
		else:
			if keys[K_LEFT]:
				Player = PlayerFlipIdle
			else:		
				Player = PlayerIdle
			
		
		if AntHealth >= 0:
			Screen.blit(Ant,AntClass)
		
		
			
		else:
			AntClass = Rect(-10,-10,0,0)
			
		if not antdead and AntHealth <= 0:
			pygame.mixer.Sound("die.wav").play(loops = 0)
			antdead = True
		if PlayerClass.colliderect(AntClass):
			ZEGAME()
			
			
		if PlayerClass.y == Box3.y:
			pygame.mixer.music.load("bossmusic.wav")
			pygame.mixer.music.play(-1,0)
		
		Screen.blit(AntText,antrect)
		Screen.blit(surf,Flowertext)
		Screen.blit(Player, PlayerClass)
		if not PlayerClass.colliderect(FlowerClass1):
			Screen.blit(Flower1, Flower1.get_rect()) 
		index = 0
		"""for flower in FlowerList:
			Screen.blit(flower,flower.get_rect(center=(randint (0,800), randint (0,800))))"""
		AntText = a.render("AntHealth: " + str(AntHealth), 1, (250,250,250,250))
		for flower in FlowerList:
			Screen.blit(flower,FlowerPosList[index])
			index += 1
		if PlayerClass.collidelist(FlowerPosList) >= 0:
			FlowerPosList.pop(PlayerClass.collidelist(FlowerPosList))
			FlowerList.pop(PlayerClass.collidelist(FlowerPosList))
			FlowerCounter += 1
			surf = f.render("Flowers: "+ str(FlowerCounter), 1, (255,0,255))
		pygame.display.update()
		mainClock.tick(FPS)
		pygame.event.pump()
		
ZEGAME()
		
		




