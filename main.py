import time
from modules import moteurs, manette

moteurs.stop()
print("Prêt !")

try:
    while True:
        ordre = manette.lire_commande()

        if ordre == "AVANCER":
            moteurs.avancer()
        elif ordre == "RECULER":
            moteurs.reculer()
        elif ordre == "GAUCHE":
            moteurs.gauche()
        elif ordre == "DROITE":
            moteurs.droite()
        elif ordre == "STOP":
            moteurs.stop()

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nArrêt du programme.")
finally:
    moteurs.stop()