import picar_4wd as fc
import config

VITESSE = config.VITESSE_MANUELLE_MAX

def avancer():
    fc.forward(VITESSE)

def reculer():
    fc.backward(VITESSE)

def gauche():
    fc.turn_left(VITESSE)

def droite():
    fc.turn_right(VITESSE)

def stop():
    fc.stop()
