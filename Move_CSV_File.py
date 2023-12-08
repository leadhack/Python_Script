import os,shutil

def deplacer_fichier_csv(rep1, rep2, nom_fichier):
    # Chemin complet du fichier source
    chemin_source = os.path.join(rep1, nom_fichier)
    # Chemin complet du fichier de destination
    chemin_destination = os.path.join(rep2, nom_fichier)
    try:
        # Déplacer le fichier
        shutil.move(chemin_source, chemin_destination)
        print(f'Le fichier {nom_fichier} a été déplacé avec succès de {rep1} vers {rep2}.')
    except FileNotFoundError:
        print(f'Erreur: Le fichier {nom_fichier} n\'existe pas dans {rep1}.')
    except PermissionError:
        print(f'Erreur: Permission refusée pour déplacer le fichier {nom_fichier}.')
    except Exception as e:
        print(f'Erreur inattendue: {e}')

# Exemple d'utilisation
repertoire_source = '/Dossier_Fichiers_Sources/'
repertoire_destination = 'Dossier_Fichiers_Destination/'
nom_du_fichier = 'mon_fichier.csv'

deplacer_fichier_csv(repertoire_source, repertoire_destination, nom_du_fichier)

