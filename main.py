#datenbankübungen

import sqlite3

#verbindung aufbauen
conn = sqlite3.connect("test.db")
c = conn.cursor()

# Tabelle erstellen                             #c.execute=Abfrage ausführen
c.execute("""                                       
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL)
""")

#user erstellen
users = [("Nico",),("Timo",),("Thomas",)]
c.executemany("INSERT INTO users (name) VALUES (?)",users)   #executemany für jeden Tupel ein insert
                                                             #?= platzhalter
#speichern
conn.commit()    #Speichert (bestätigt) alle Änderungen dauerhaft in der Datenbank

#überprüfen ob user da ist
c.execute("SELECT * FROM users")        #c.execute = Befehl, um einen neuen Datensatz in die Tabelle einzufügen
print(c.fetchall())        #c.fetchall=alle Ergebnisse abrufen

# schließen
conn.close()      #schließen