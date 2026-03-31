#datenbank übung

import sqlite3

#verbindung aufbauen
conn = sqlite3.connect("test.db")
c = conn.cursor()

#tabelle erstellen
c.execute("""
create table if not exists users (
    id integer primary key autoincrement,   
    name text not null """)               #id integer primary key autoincrement =wird automatisch hochgezählt
                                          #name text not null = Name, darf nicht leer sein
#speichern/schließen
conn.commit()    #Speichert (bestätigt) alle Änderungen dauerhaft in der Datenbank
conn.close()      #schließen