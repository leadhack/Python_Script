import subprocess

def stop_service(service_name):
    try:
        # Exécute la commande pour arrêter le service
        subprocess.run(['sc', 'stop', service_name], check=True)
        print(f"Le service {service_name} a été arrêté avec succès.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'arrêt du service {service_name}: {e.stderr}")

def start_service(service_name):
    try:
        # Exécute la commande pour démarrer le service
        subprocess.run(['sc', 'start', service_name], check=True)
        print(f"Le service {service_name} a été démarré avec succès.")

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du démarrage du service {service_name}: {e.stderr}")

if __name__ == "__main__":
    # Exemple d'utilisation : remplacez 'NomDuService' par le nom réel du service que vous souhaitez arrêter/démarrer
    service_name = 'NomDuService'
    stop_service(service_name)
    start_service(service_name)
