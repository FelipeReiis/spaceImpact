import pygame as pg
import random

pg.init()

LARGURA_JANELA = 500
ALTURA_JANELA = 500

tela = pg.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pg.display.set_caption('Space Impact')

plano_fundo = pg.image.load('imgs/background_1.png').convert_alpha()
plano_fundo = pg.transform.scale(plano_fundo, (LARGURA_JANELA, ALTURA_JANELA))

alien = pg.image.load('imgs/alien_1_1.png').convert_alpha()
alien = pg.transform.scale(alien, (50, 50))
pos_alien_x = 400
pos_alien_y = 300

nave = pg.image.load('imgs/ship_1.png').convert_alpha()
nave = pg.transform.scale(nave, (50,50))
# nave = pg.transform.rotate(nave, -90)
pos_nave_x = 100
pos_nave_y = 250

disparo = pg.image.load('imgs/d.png').convert_alpha()
disparo = pg.transform.scale(disparo,(8,8))
disparo = pg.transform.rotate(disparo, 90)

vel_disparo = 0
pos_disparo_x = 125
pos_disparo_y = 270

disparar = False
rodando = True

hit_box_nave = nave.get_rect()
hit_box_alien = alien.get_rect()
hit_box_disparo = disparo.get_rect()

def reviver_alien():
  x = 500
  y = random.randint(0,450)
  return [x,y]

def recarregar():
  disparar = False
  recarregar_missil_x= pos_nave_x + 25
  recarregar_missil_y = pos_nave_y + 20
  vel_disparo = 0
  return [recarregar_missil_x, recarregar_missil_y, disparar, vel_disparo]

def colisao():
  if hit_box_nave.colliderect(hit_box_alien):
    return True
  elif hit_box_disparo.colliderect(hit_box_alien):
    return True
  else:
    return False
  
while rodando:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      rodando = False
  tela.blit(plano_fundo,(0,0))
  resto_tela = LARGURA_JANELA % plano_fundo.get_rect().width
  tela.blit(plano_fundo,(resto_tela - plano_fundo.get_rect().width,0))
  if resto_tela < 500:
    tela.blit(plano_fundo,(resto_tela, 0))  

  tecla = pg.key.get_pressed()
  if tecla[pg.K_UP] and pos_nave_y > 1:
    pos_nave_y -=.1
    if not disparar:    
      pos_disparo_y -=.1
  if tecla[pg.K_DOWN] and pos_nave_y < 400:
    pos_nave_y +=.1
    if not disparar:
      pos_disparo_y +=.1
  if tecla[pg.K_SPACE]:
    disparar = True
    vel_disparo = .15
    
  if pos_alien_x <= 10 or colisao():
    # for i in range(10):
    pos_alien_x = reviver_alien()[0]
    pos_alien_y = reviver_alien()[1]
  if pos_disparo_x >= 500 or colisao():
    pos_disparo_x, pos_disparo_y, disparar, vel_disparo = recarregar()
  
  hit_box_nave.y = pos_nave_y
  hit_box_nave.x = pos_nave_x

  hit_box_alien.y = pos_alien_y
  hit_box_alien.x = pos_alien_x

  hit_box_disparo.y = pos_disparo_y
  hit_box_disparo.x = pos_disparo_x

  LARGURA_JANELA -=.1
  pos_alien_x -=.1
  pos_disparo_x += vel_disparo

  pg.draw.rect(tela,(56,66,55),hit_box_nave,4)
  pg.draw.rect(tela,(56,66,55),hit_box_alien,4)
  pg.draw.rect(tela,(56,66,55),hit_box_disparo,4)
  
  tela.blit(alien,(pos_alien_x, pos_alien_y)) 
  tela.blit(disparo,(pos_disparo_x, pos_disparo_y))
  tela.blit(nave,(pos_nave_x, pos_nave_y))
  pg.display.update()