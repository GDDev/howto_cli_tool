import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    finally:
        return conn
    
def terminate_connection(conn):
    if conn:
        conn.close()
    return conn

def create_tables(conn):
    try:
        cursor = conn.cursor

        # Creating Tools table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tools(
                id INTEGER PRIMARY KEY,
                name TEXT,
                title TEXT,
                usage TEXT,
                category TEXT,
                description TEXT
            )
        ''')

        # Creating Flags table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Flags(
                id INTEGER PRIMARY KEY,
                flag TEXT,
                description TEXT,
                explanation TEXT,
                tool_id INTEGER,
                CONSTRAINT FOREIGN KEY (tool_id) REFERENCES Tools (id)
            )
        ''')

        # Creating Techniques table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Techniques(
                id INTEGER PRIMARY KEY,
                name TEXT,
                explanation TEXT
            )
        ''')

        # Creating a many-to-many table for the Tools and Techniques
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tool_Technique(
                id INTEGER PRIMARY KEY,
                tool_id INTEGER,
                technique_id INTEGER,
                CONSTRAINT FOREIGN KEY (tool_id) REFERENCES Tools (id),
                CONSTRAINT FOREIGN KEY (technique_id) REFERENCES Techniques (id)
            )
        ''')

        conn.commit()

        cursor.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
