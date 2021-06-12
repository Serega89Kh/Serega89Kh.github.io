import datetime

from flask import Markup
from peewee import *

from app import db

class Blog(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
