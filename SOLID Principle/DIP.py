from abc import ABC, abstractmethod

class Database(ABC):  # Abstraction
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):  # Low-level module
    def connect(self):
        print("Connecting to MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL")

class DataProcessor:  # High-level module
    def __init__(self, db: Database):
        self.db = db  # Depends on abstraction

    def process(self):
        self.db.connect()
