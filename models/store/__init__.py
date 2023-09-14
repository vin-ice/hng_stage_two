#!/usr/bin/python3
"""store Model/interface"""
from abc import ABC, abstractmethod
from logging import getLogger
import models.user as model
from mysql.connector import connect, Error
from typing import Dict, Union, Sequence

logger = getLogger('store.py')


class Store(ABC):
    """store interface"""
    @abstractmethod
    def all(self, table):
        pass

    @abstractmethod
    def delete(self, table: str, obj: model.User):
        pass

    @abstractmethod
    def get(self, table: str, user_id):
        pass

    @abstractmethod
    def new(self, table: str, obj: model.User):
        pass

    @abstractmethod
    def update(self, table: str, obj: model.User):
        pass


class DBStore(Store):
    def __init__(self, host, user, pwd, db):
        """connects to an existing db"""
        try:
            self.conn = connect(
                host=host,
                user=user,
                password=pwd,
                database=db
            )
        except Error as e:
            print("store failed to initialize: %s"
                  % (e))

    def all(self, table) -> Union[Sequence, None]:
        """retrieves all entries of the table"""
        stmnt = f"SELECT * FROM {table}"
        with self.conn.cursor(buffered=True) as cursor:
            cursor.execute(stmnt)
            self.conn.commit()
            records: Sequence = cursor.fetchall()
            if len(records) > 0:
                return records
        return None

    def delete(self, table, obj: model.User):
        """deletes a user"""
        stmnt = f"DELETE FROM {table} WHERE user_id = %s"
        values = (obj.user_id,)
        with self.conn.cursor() as cursor:
            cursor.execute(stmnt, values)
            self.conn.commit()

    def get(self, table, user_id: str):
        """retieves an item using name"""
        records: Union[None, Sequence] = self.all(table)
        if records:
            for record in records:
                if user_id in record:
                    return record
        return None

    def new(self, table, obj: model.User):
        """creates a new entry"""
        stmnt = f"INSERT INTO {table} VALUES (NULL, %s, %s, %s)"
        values = (obj.user_id, obj.name, obj.value)
        with self.conn.cursor() as cursor:
            cursor.execute(stmnt, values)
            self.conn.commit()

    def update(self, table, obj: model.User):
        """updates object"""
        stmnt = f"UPDATE {table} SET name = %s, value = %s WHERE user_id = %s"
        values = (obj.name, obj.value, obj.user_id)
        with self.conn.cursor() as cursor:
            cursor.execute(stmnt, values)
            self.conn.commit()
