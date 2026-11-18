import evdev
from evdev import ecodes
import config

# Ouverture de la manette
device = evdev.InputDevice(config.CHEMIN_MANETTE)

def lire_commande():
    event = device.read_one()
    
    if event is None:
        return None

    if event.type == ecodes.EV_ABS:
        
        if event.code == config.AXE_ACCELERATEUR:
            if event.value > 100:
                return "AVANCER"
            else:
                return "STOP"

        elif event.code == config.AXE_FREIN_RECUL:
            if event.value > 100:
                return "RECULER"
            else:
                return "STOP"

        elif event.code == config.AXE_DIRECTION:
            if event.value < -config.DEADZONE_JOYSTICK:
                return "GAUCHE"
            elif event.value > config.DEADZONE_JOYSTICK:
                return "DROITE"
            else:
                return "STOP"
        elif event.type == config.BTN_ARRET_URGENCE:
            return "STOP"

    return None
