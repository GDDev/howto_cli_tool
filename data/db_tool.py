import sqlite3
from data.database import Database

class ToolDatabase(Database):
    
    def __init__(self):
        super().__init__()

    def get_id(self, cursor):
        cursor.execute('SELECT id FROM Tools ORDER BY id DESC LIMIT 1')
        id = cursor.fetchone()[0]
        return id

    def create(self, object):
        name, title, usage, category, description = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'INSERT INTO Tools (name, title, usage, category, description) VALUES (?, ?, ?, ?, ?)'
            values = (name, title, usage, category, description)
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
        id, name, title, usage, category, description, _ = object
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = 'UPDATE Tools SET name = ?, title = ?, usage = ?, category = ?, description = ? WHERE id = ?'
            values = (name, title, usage, category, description, id)
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
            query = 'DELETE FROM Tools WHERE id = ?'
            value = str(id)
            cursor.execute(query, value)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()
