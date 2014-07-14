__author__ = 'george'

from sqlalchemy import Column, Integer, String
from database import Base

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    likes = Column(String)
    num_likes = Column(Integer)

    def __init__(self, title="Flask-Admin is an A*hole", likes=None, num_likes=0):
        self.title = title
        self.likes = likes
        self.num_likes = num_likes

    def __repr__(self):
        return "<Game %r>" % self.title


class Cookie(Base):
    __tablename__ = "cookies"
    id = Column(Integer, primary_key=True)
    uuid = Column(Integer, nullable=False)
    likes = Column(String)

    def __init__(self, uuid, likes=None):
        self.uuid = uuid
        self.likes = likes

    def __repr__(self):
        return "<Cookie %r>" % self.uuid
