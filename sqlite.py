import sqlite3
# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect(':memory:')  # Utilise une base de données en mémoire

# Création d'un curseur
cursor = conn.cursor()

# Création d'une table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        age INTEGER
    )
''')

# Insertion de données
cursor.execute('INSERT INTO utilisateurs (prenom, age) VALUES (?, ?)', ('Mehdi', 34))
cursor.execute('INSERT INTO utilisateurs (prenom, age) VALUES (?, ?)', ('Anass', 33))

# Sélection de données
cursor.execute('SELECT * FROM utilisateurs')
rows = cursor.fetchall()

# Affichage des résultats
print("Liste des utilisateurs:")
for row in rows:
    print(row)

# Fermeture de la connexion
conn.close()
