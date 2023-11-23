import pygame as pg
import random

LARGURA_JANELA = 500
ALTURA_JANELA = 500
class Alien():
  def __init__(self):
    self.imgAlien = pg.image.load('imgs/alien_1_1.png').convert_alpha()
    self.imgAlien = pg.transform.scale(self.imgAlien, (50,50))
    self.areaAlien = self.imgAlien.get_rect()
    self.pos_alien_x = 400
    self.pos_alien_y = random.randint(10,450)
    self.velocidade = .070

  def colocarAlienNaTela(self, item):    
    hit_box_alien = self.areaAlien
    hit_box_alien.y = self.pos_alien_y
    hit_box_alien.x = self.pos_alien_x
    pg.draw.rect(item,(56,66,55),hit_box_alien,4)
    item.blit(self.imgAlien,(self.pos_alien_x, self.pos_alien_y))
  
  def movimentarAlien(self):
    self.pos_alien_x -= self.velocidade

class Bala():
  def __init__(self,x,y):
    self.imgProjetil = pg.image.load('imgs/d.png').convert_alpha()
    self.imgProjetil = pg.transform.scale(self.imgProjetil, (8,8))
    self.areaProjetil = self.imgProjetil.get_rect()
    self.pos_projetil_x = x 
    self.pos_projetil_y = y 
    self.velocidade = .2

  def trajetoria(self):
    self.pos_projetil_x += self.velocidade 
  
  def colocarProjetilNaTela(self, item):      
    hit_box_projetil = self.areaProjetil
    hit_box_projetil.y = self.pos_projetil_y
    hit_box_projetil.x = self.pos_projetil_x
    pg.draw.rect(item,(56,66,55),hit_box_projetil,4)
    item.blit(self.imgProjetil,(self.pos_projetil_x, self.pos_projetil_y))
    
class nave():
  def __init__(self):
    self.imgNave = pg.image.load('imgs/ship_1.png').convert_alpha()
    self.imgNave = pg.transform.scale(self.imgNave, (50,50))
    self.areaNave = self.imgNave.get_rect()
    self.pos_nave_x = 50
    self.pos_nave_y = 250

    self.disparos = []
    self.vida = True
    self.velocidade = .1
    
  def disparar(self,x,y):
    bala = Bala(x,y)
    self.disparos.append(bala)

  def movimentarParaCima(self):       
      if self.pos_nave_y > 10:
        self.pos_nave_y -= 50

  def movimentarParaDireita(self):
    if self.pos_nave_x < 450:
      self.pos_nave_x += 50

  def movimentarParaBaixo(self):
    if self.pos_nave_y < 450:
        self.pos_nave_y += 50

  def movimentarParaEsquerda(self):
     if self.pos_nave_x > 1:
        self.pos_nave_x -= 50

  def colocarNaveNaTela(self, item):
    hit_box_nave = self.areaNave
    hit_box_nave.y = self.pos_nave_y
    hit_box_nave.x = self.pos_nave_x
    pg.draw.rect(item,(56,66,55),hit_box_nave,4)
    item.blit(self.imgNave,(self.pos_nave_x, self.pos_nave_y))

  # def colisao(self):
  #   alien = Alien()
  #   bala = Bala(self.areaNave.x,self.areaNave.y)
  #   if self.areaNave.colliderect(alien.areaAlien):
  #     print('ss')
  #     return True
  #   # if bala.areaProjetil.colliderect(alien.areaAlien):
  #   #   return True
  #   else:
  #     print('nn')
  #     False
    
def spaceImpact():
  pg.init()
  tela = pg.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
  pg.display.set_caption('Space Impact')
  jogador = nave()
  plano_fundo = pg.image.load('imgs/background_1.png').convert_alpha()
  plano_fundo = pg.transform.scale(plano_fundo, (LARGURA_JANELA, ALTURA_JANELA))
  x_nave,y_nave = jogador.areaNave.center
  projetil = Bala(x_nave,y_nave)
  alien = Alien()
  while True:
    tecla = pg.key.get_pressed()
    alien.movimentarAlien()
    for evento in pg.event.get():
      if evento.type == pg.QUIT:
        pg.quit()        
      if tecla[pg.K_UP]:
        jogador.movimentarParaCima()
      elif tecla[pg.K_RIGHT]:
        jogador.movimentarParaDireita()
      elif tecla[pg.K_DOWN]:
        jogador.movimentarParaBaixo()
      elif tecla[pg.K_LEFT]:
        jogador.movimentarParaEsquerda()
      elif tecla[pg.K_SPACE]:
        x,y = jogador.areaNave.center
        jogador.disparar(x,y)
    tela.blit(plano_fundo,(0,0))
    if len(jogador.disparos) > 0:
      for disparo in jogador.disparos:
        disparo.colocarProjetilNaTela(tela)
        disparo.trajetoria()
        if disparo.pos_projetil_x > 500:
          jogador.disparos.remove(disparo)
    jogador.colocarNaveNaTela(tela)
    projetil.colocarProjetilNaTela(tela)
    alien.colocarAlienNaTela(tela)
    if alien.areaAlien.x <= 0 or jogador.areaNave.colliderect(alien.areaAlien) or projetil.areaProjetil.colliderect(alien.areaAlien):
      alien.pos_alien_x = 400
      alien.pos_alien_y = random.randint(10,450)
      alien.colocarAlienNaTela(tela)
      alien.movimentarAlien()
    pg.display.update()
spaceImpact()