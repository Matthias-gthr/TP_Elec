# === CONFIGURATION MATÉRIELLE ===
CHEMIN_MANETTE = "/dev/input/event6"  

SEUIL_NOIR = 375
SEUIL_BLANC = 775

# === RÉGLAGES DES VITESSES (0 à 100)
VITESSE_MANUELLE_MAX = 60
VITESSE_AUTO_DROIT = 25
VITESSE_AUTO_VIRAGE = 25

# === MAPPING MANETTE XBOX SERIES X (CODES EVDEV)
# Axes analogiques
AXE_DIRECTION = 0      # ABS_X  (-32768 à 32767)
AXE_FREIN_RECUL = 2    # ABS_Z  (Gâchette LT : 0 à 1023)
AXE_ACCELERATEUR = 5   # ABS_RZ (Gâchette RT : 0 à 1023)

# Boutons d'action (codes standards evdev)
BTN_MODE_MANUEL = 308  # BTN_SOUTH (Bouton A)
BTN_MODE_NOIR = 305   # BTN_EAST  (Bouton B)
BTN_MODE_BLANC = 307   # BTN_NORTH (Bouton X ou Y selon pilote)
BTN_ARRET_URGENCE = 304 # BTN_WEST (Bouton Y ou X selon pilote)

# === PARAMÈTRES DE CONDUITE 
DEADZONE_JOYSTICK = 4000  # Ignore les micro-mouvements au repos (-4000 à +4000)
VALEUR_MAX_JOYSTICK = 32767
VALEUR_MAX_GACHETTE = 1023