import paramiko

def ssh_execute_command(hostname, username, private_key_path, command):
    # Créer un client SSH
    ssh_client = paramiko.SSHClient()
    try:
        # Charger les clés publiques du fichier ~/.ssh/known_hosts
        ssh_client.load_system_host_keys()
        # Ignorer les vérifications d'authenticité de l'hôte
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Charger la clé privée
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        # Connexion au serveur distant
        ssh_client.connect(hostname=hostname, username=username, pkey=private_key)
        # Exécution de la commande
        stdin, stdout, stderr = ssh_client.exec_command(command)
        # Lecture de la sortie de la commande
        output = stdout.read().decode('utf-8')
        # Fermer la connexion SSH
        ssh_client.close()
        return output
    except Exception as e:
        return f"Erreur lors de la connexion SSH : {str(e)}"

# Exemple d'utilisation
if __name__ == "__main__":
    hostname = "10.118.21.22"
    username = "osadmin"
    private_key_path = "id_rsa"
    command = "ls -l /tmp"

    output = ssh_execute_command(hostname, username, private_key_path, command)
    print(output)
