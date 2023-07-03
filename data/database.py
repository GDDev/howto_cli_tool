import data.connection as conn
from abc import ABC, abstractmethod

DB_NAME = 'howto.db'

class Database(ABC):

    def __init__(self) -> None:
        self.db_name = DB_NAME
        self.conn = None

    def connect(self):
        self.conn = conn.create_connection(self.db_name)

    def disconnect(self):
        self.conn = conn.terminate_connection(self.conn)

    def create_tables(self):
        conn.create_tables(self.conn)

    def initialize(self):
        try:
            self.connect()
            self.create_tables(self.conn)
        except Exception as e:
            print(e)
        finally:
            if self.conn:
                self.disconnect()

    @abstractmethod
    def get_id(self, cursor):
        pass

    @abstractmethod    
    def create(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, id):
        pass
