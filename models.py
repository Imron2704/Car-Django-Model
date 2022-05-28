from abc import ABC, abstractmethod

import sqlite3
from website.settings import BASE_DIR

db_name = BASE_DIR / 'website' / "db" / "cars.db"

class BaseModel(ABC):
    table = ''

    def __init__(self, id) -> None:
        self.id = id
        self.created_date = None
        self.updated_date = None
        self.__isValid = True

    @abstractmethod
    def save(self):
        pass

    def delete(self):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute(f"Delete From {self.table} Where Id='{self.id}'")
        conn.commit()
        conn.close()

    @property
    def isValid(self):
        return self.__isValid

    @isValid.setter
    def isValid(self, isValid):
        self.__isValid = isValid
        pass

    @abstractmethod
    def print():
        pass

    @abstractmethod
    def get_by_id(id):
        pass


class Region(BaseModel):
    table = "Cars"

    def __init__(self, name, id=None) -> None:
        super().__init__(id)
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ''

    def save(self):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(f"INSERT INTO Cars (NAME) VALUES ('{self.name}')")
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                f"UPDATE Cars set NAME = '{self.name}' where ID = {self.id}")
        conn.commit()
        conn.close()

    def get_by_id(id):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor = conn.execute(f"SELECT * from {Region.table} Where ID={id}")

        sql_row = list(cursor)[0]
        sel_region = Region(sql_row[1], sql_row[0])

        conn.commit()
        conn.close()

        return sel_region

    def print():
        for item in BaseModel.objects(Region.table):
            print(item)

    def __str__(self) -> str:
        return f'{self.id} {self.name}'

    def objects():
        conn = sqlite3.connect(db_name)
        cursor = conn.execute(f"SELECT * from {Region.table}")
        for row in cursor:
            yield Region(row[1], row[0])
        conn.close()

    def rows():
        conn = sqlite3.connect(db_name)
        cursor = conn.execute(f"SELECT * from {Region.table}")
        row_s = cursor.fetchall()
        conn.close()

        return row_s

