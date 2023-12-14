import subprocess

def list_windows_services():
    try:
        # Exécute la commande 'sc query' pour obtenir la liste des services
        result = subprocess.run(['sc', 'query'], capture_output=True, text=True, check=True)
        # Affiche la sortie de la commande
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # En cas d'erreur, affiche le message d'erreur
        print(f"Erreur lors de l'exécution de la commande : {e.stderr}")

if __name__ == "__main__":
    list_windows_services()
