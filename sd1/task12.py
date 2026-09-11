import psycopg2

CONNECT_DICT = {
    "dbname": "db",
    "host": "172.0.0.1",
    "port": "5432",
    "user": "adm",
    "password": "p",
}

class DatabaseStorage:
    """Using duck-like typing"""

    def __init__(self):
        self.connection_dict = CONNECT_DICT

    def save(self, data: str) -> None:
        with psycopg2.connect(**CONNECT_DICT) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("INSERT INTO table (text_field) VALUES (%s)", (data))
                    conn.commit()
                except Exception:
                    conn.rollback()
                    raise

    def retrieve(self, _id: int) -> str:
        with psycopg2.connect(**CONNECT_DICT) as conn:
            with conn.cursor() as cur:
                res = cur.fetchone(f"select text_field from table where id = {_id}")
                if res > 0:
                    return res[0]
                else:
                    raise Exception


class LocalStorage:
    """Using duck-like typing too"""
    def __init__(self):
        self.data = []

    def save(self, data):
        self.data.append(data)

    def retrieve(self, _id) -> str:
        return self.data[_id]

if __name__ == "__main__":
    storage = DatabaseStorage()
    storage.save("Data in database")
    res = storage.retrieve(0)


