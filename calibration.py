import picar_4wd as fc
import time

print("=== CALIBRATION DES CAPTEURS DE LIGNE ===")
print("Posez la voiture sur le sol neutre, la ligne noire, puis la ligne blanche.")
print("Appuyez sur Ctrl+C pour quitter.\n")

try:
    while True:
        valeurs = fc.get_grayscale_list()
        moyenne = sum(valeurs) / len(valeurs)
        
        print(f"Gauche: {valeurs[0]:4d} | Milieu: {valeurs[1]:4d} | Droite: {valeurs[2]:4d}  --> Moyenne: {moyenne:.0f}")
        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nCalibration terminée.")