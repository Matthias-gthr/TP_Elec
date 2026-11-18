import evdev
from evdev import ecodes
import config

class ManetteXbox:
    def __init__(self, chemin=config.CHEMIN_MANETTE):
        self.device = evdev.InputDevice(chemin)
        print(f"Manette connectée : {self.device.name} sur {chemin}")
        
        # États courants des commandes
        self.vitesse_avant = 0
        self.vitesse_arriere = 0
        self.direction = 0  # -100 (gauche) à +100 (droite), 0 = tout droit
        self.arret_urgence = False

    def lire_evenements(self):
        """Lit tous les événements en attente sans bloquer l'exécution."""
        try:
            for event in self.device.read():
                if event.type == ecodes.EV_ABS:
                    # Gâchette droite (RT) : Accélération
                    if event.code == config.AXE_ACCELERATEUR:
                        self.vitesse_avant = int((event.value / config.VALEUR_MAX_GACHETTE) * config.VITESSE_MANUELLE_MAX)
                    
                    # Gâchette gauche (LT) : Marche arrière
                    elif event.code == config.AXE_FREIN_RECUL:
                        self.vitesse_arriere = int((event.value / config.VALEUR_MAX_GACHETTE) * config.VITESSE_MANUELLE_MAX)
                    
                    # Joystick gauche (Axe X) : Direction
                    elif event.code == config.AXE_DIRECTION:
                        if abs(event.value) < config.DEADZONE_JOYSTICK:
                            self.direction = 0
                        else:
                            self.direction = int((event.value / config.VALEUR_MAX_JOYSTICK) * config.VITESSE_MANUELLE_MAX)

                # Gestion des boutons (appui = 1)
                elif event.type == ecodes.EV_KEY and event.value == 1:
                    if event.code == config.BTN_ARRET_URGENCE:
                        self.arret_urgence = not self.arret_urgence
                        print(f"Arrêt d'urgence : {'ACTIVÉ' if self.arret_urgence else 'DÉSACTIVÉ'}")

        except BlockingIOError:
            # Aucun nouvel événement à lire pour le moment, on continue normalement
            pass