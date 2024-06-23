import psutil
import datetime

def afficher_informations_processus_par_pid(pid):
    try:
        processus = psutil.Process(pid)
        infos_processus = processus.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_info', 'create_time'])

        # Calculer le temps d'exécution
        temps_exec = datetime.datetime.now() - datetime.datetime.fromtimestamp(infos_processus['create_time'])

        # Afficher les informations détaillées
        print(f"Informations détaillées pour le processus avec PID {infos_processus['pid']} :")
        print(f"Nom du processus : {infos_processus['name']}")
        print(f"Utilisateur : {infos_processus['username']}")
        print(f"Utilisation CPU (%) : {infos_processus['cpu_percent']}%")
        print(f"Consommation mémoire : {infos_processus['memory_info'].rss / (1024 ** 2):.2f} Mo")
        print(f"Temps d'exécution : {temps_exec}")

    except psutil.NoSuchProcess:
        print(f"Aucun processus trouvé avec le PID {pid}.")
    except psutil.AccessDenied:
        print(f"Accès refusé pour accéder aux informations du processus avec PID {pid}.")

# Demander à l'utilisateur d'entrer le PID du processus à inspecter
pid_a_inspecter = int(input("Entrez le PID du processus à inspecter : "))

# Appeler la fonction pour afficher les informations détaillées
afficher_informations_processus_par_pid(pid_a_inspecter)
