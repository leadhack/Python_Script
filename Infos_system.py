import psutil
def afficher_informations_systeme():
    # Informations sur le processeur
    cpu_info = psutil.cpu_percent(interval=1, percpu=True)
    # Informations sur la mémoire
    memoire = psutil.virtual_memory()
    # Informations sur l'utilisation du disque
    disque = psutil.disk_usage('/')
    # Affichage des résultats
    print("Informations Système :")
    print(f"Utilisation du CPU : {cpu_info}%")
    print(f"Mémoire physique : Total {memoire.total / (1024 ** 3):.2f} Go, Utilisé {memoire.used / (1024 ** 3):.2f} Go")
    print(f"Espace disque disponible : {disque.free / (1024 ** 3):.2f} Go")

# Appeler la fonction pour afficher les informations système
afficher_informations_systeme()
