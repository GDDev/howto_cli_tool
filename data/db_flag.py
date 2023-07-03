import sqlite3
from data.database import Database

class FlagDatabase(Database):

    def __init__(self):
        super().__init__()

    def get_id(self, cursor):
        cursor.execute('SELECT id FROM Flags ORDER BY id DESC LIMIT 1')
        id = cursor.fetchone()[0]
        return id

    def create(self, object):
        flag, description, explanation, tool_id = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'INSERT INTO Flags (flag, description, explanation, tool_id) VALUES (?, ?, ?, ?)'
            values = (flag, description, explanation, tool_id)
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
        id, flag, description, explanation, tool_id = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'UPDATE Flags SET flag = ?, description = ?, explanation = ?, tool_id = ? WHERE id = ?'
            values = (flag, description, explanation, tool_id, id)
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
            query = 'DELETE FROM Flags WHERE id = ?'
            value = str(id)
            cursor.execute(query, value)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()
                