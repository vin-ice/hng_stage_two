#!/usr/bin/python
from models.store import Store, DBStore
from os import getenv

host =  getenv('HNG_HOST')
user =  getenv('HNG_USER')
password = getenv("HNG_PWD")
db = getenv("HNG_DB")
port = getenv("HNG_PORT")


store: Store = DBStore(host=host, user=user,
                       pwd=password, db=db)
