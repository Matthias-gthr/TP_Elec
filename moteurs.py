import picar_4wd as fc

def avancer(vitesse):
    """Fait avancer le robot à la vitesse donnée (0 à 100)."""
    vitesse = max(0, min(100, int(vitesse)))
    fc.forward(vitesse)

def reculer(vitesse):
    """Fait reculer le robot à la vitesse donnée (0 à 100)."""
    vitesse = max(0, min(100, int(vitesse)))
    fc.backward(vitesse)

def tourner_gauche(vitesse):
    """Fait pivoter le robot vers la gauche."""
    vitesse = max(0, min(100, int(vitesse)))
    fc.turn_left(vitesse)

def tourner_droite(vitesse):
    """Fait pivoter le robot vers la droite."""
    vitesse = max(0, min(100, int(vitesse)))
    fc.turn_right(vitesse)

def arreter():
    """Stoppe immédiatement les 4 moteurs."""
    fc.stop()