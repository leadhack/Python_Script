import os
import shutil

def copier_fichiers_par_extension(dossier_source, dossier_destination, extension):
    try:
        # Créer le dossier de destination s'il n'existe pas
        if not os.path.exists(dossier_destination):
            os.makedirs(dossier_destination)

        # Parcourir tous les fichiers du dossier source
        for fichier in os.listdir(dossier_source):
            if fichier.endswith(extension):
                chemin_source = os.path.join(dossier_source, fichier)
                chemin_destination = os.path.join(dossier_destination, fichier)
                shutil.copy(chemin_source, chemin_destination)
        
        print(f"Fichiers avec l'extension '{extension}' copiés avec succès dans '{dossier_destination}'.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation
dossier_source = 'chemin/vers/votre/dossier/source'
dossier_destination = 'chemin/vers/votre/dossier/destination'
extension_recherchee = '.txt'

copier_fichiers_par_extension(dossier_source, dossier_destination, extension_recherchee)

