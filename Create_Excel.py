import openpyxl

def creer_fichier_excel(nom_fichier):
    # Créer un nouveau classeur Excel
    classeur = openpyxl.Workbook()

    # Sélectionner la feuille active
    feuille = classeur.active

    # Ajouter des données de démonstration (vous pouvez personnaliser cela selon vos besoins)
    feuille['A1'] = 'Id Employe'
    feuille['B1'] = 'Prenom'
    feuille['C1'] = 'Nom'
    feuille['D1'] = 'Poste'

    # Sauvegarder le fichier Excel avec le nom spécifié
    classeur.save(nom_fichier)

    print(f'Le fichier Excel "{nom_fichier}" a été créé avec succès.')

# Exemple d'utilisation de la fonction
nom_du_fichier = 'Employe.xlsx'
creer_fichier_excel(nom_du_fichier)
