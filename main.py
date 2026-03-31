#datenbank übung

import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()

conn.commit()    #Speichert (bestätigt) alle Änderungen dauerhaft in der Datenbank
conn.close()      #schließen