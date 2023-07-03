import sqlite3
from data.database import Database

class TechniqueDatabase(Database):

    def __init__(self):
        super().__init__()

    def get_id(self, cursor):
        cursor.execute('SELECT id FROM Techniques ORDER BY id DESC LIMIT 1')
        id = cursor.fetchone()[0]
        return id

    def create(self, object):
        name, explanation = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'INSERT INTO Techniques (name, explanation) VALUES (?, ?)'
            values = (name, explanation)
            cursor.execute(query, values)
            self.conn.commit()
            id = self.get_id(cursor)
            cursor.close()
            return id
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()

    def update(self, object):
        id, name, explanation, _ = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'UPDATE Techniques SET name = ?, explanation = ? WHERE id = ?'
            values = (name, explanation, id)
            cursor.execute(query, values)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()

    def delete(self, id):
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'DELETE FROM Techniques WHERE id = ?'
            value = str(id)
            cursor.execute(query, value)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()
