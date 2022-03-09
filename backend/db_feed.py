from os import environ
from psycopg2 import connect

class PostGreSQL:
    def __init__(self) -> None:
        self.connection = connect(dbname=environ['DB_NAME'], user=environ['DB_USER'], password=environ['DB_PASS'])

    def insert(self, proc_name: str, date: int, result: str, link: str) -> int:
        with self.connection:
            with self.connection.cursor() as curs:
                curs.execute(f"INSERT INTO {environ['TABLE_NAME']} ({proc_name}, {date}, {result}, {link});")

    def fetch(self):
        with self.connection:
            with self.connection.cursor() as curs:
                return [
                    {"proc_name": proc_name, "date": date, "result": result, "link": link}
                    for (proc_name, date, result, link)
                    in curs.execute(f"SELECT * FROM {environ['TABLE_NAME']};")
                ]
