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

#alle löschen (sauberer start)
c.execute("DELETE FROM users")
conn.commit()

#user erstellen
users = [("Nico",),("Timo",),("Thomas",)]
c.executemany("INSERT INTO users (name) VALUES (?)",users)   #executemany für jeden Tupel ein insert
                                                             #?= platzhalter für parameter
#speichern
conn.commit()    #Speichert (bestätigt) alle Änderungen dauerhaft in der Datenbank

#namen ändern
c.execute("UPDATE users SET name = ? WHERE name = ?", ("Niklas", "Nico"))    #ohne where werden alle user geändert
conn.commit()

#daten gezielt abfragen
print("Filter: Namen mit 'i'")
c.execute("SELECT * FROM users WHERE name LIKE ?", ("%i%",))    #% Platzhalter für abfragen(beliebige Zeichen 0 oder mehr)
print(c.fetchall())                                                           #_ Platzhalter für ein einzelnes Zeichen

# Daten sortieren
print("\nAlle User alphabetisch sortiert")
c.execute("SELECT * FROM users ORDER BY name")
print(c.fetchall())

#user löschen
c.execute("DELETE FROM users WHERE name = ?", ("Thomas",))

#überprüfen ob user da ist
c.execute("SELECT * FROM users")        #c.execute = Befehl, um einen neuen Datensatz in die Tabelle einzufügen
print(c.fetchall())        #c.fetchall=alle Ergebnisse abrufen


# schließen
conn.close()      #schließen