import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key=True, nullable=False)
    firstName= Column(String(250), nullable=False)
    secondName= Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    password= Column(String(50), nullable=False)

class Character(Base):
    __tablename__= 'character'
    id=Column(Integer, primary_key=True, nullable=False)
    name= Column(String(250), nullable=False)
    gender = Column(String(50))
    birth_date = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    skin_color = Column(String(100))
    eye_color = Column(String(100))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    
class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
