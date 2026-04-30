from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from src.infrastructure.database import Base

# Link-Table für Spiellinie und Lernziele (Many-to-Many)
spiellinie_lernziele = Table(
    'spiellinie_lernziele',
    Base.metadata,
    Column('spiellinie_id', String, ForeignKey('spiellinien.id')),
    Column('lernziel_id', String, ForeignKey('lernziele.id'))
)

class UserModel(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String)
    schule = Column(String)
    spiellinien = relationship("SpiellinieModel", back_populates="user")

class ZielgruppeModel(Base):
    __tablename__ = "zielgruppen"
    id = Column(String, primary_key=True)
    name = Column(String)
    beschreibung = Column(String)

class ThemaModel(Base):
    __tablename__ = "themen"
    id = Column(String, primary_key=True)
    titel = Column(String)
    beschreibung = Column(String)

class SpiellinieModel(Base):
    __tablename__ = "spiellinien"
    id = Column(String, primary_key=True)
    inhalt = Column(String)
    user_id = Column(String, ForeignKey("users.id"))
    zielgruppe_id = Column(String, ForeignKey("zielgruppen.id"))
    thema_id = Column(String, ForeignKey("themen.id"))
    
    user = relationship("UserModel", back_populates="spiellinien")
    zielgruppe = relationship("ZielgruppeModel")
    thema = relationship("ThemaModel")
    stationen = relationship("StationModel", back_populates="spiellinie")
    lernziele = relationship("LernzielModel", secondary=spiellinie_lernziele)

class StationModel(Base):
    __tablename__ = "stationen"
    id = Column(String, primary_key=True)
    name = Column(String)
    ort = Column(String)
    reihenfolge = Column(Integer)
    spiellinie_id = Column(String, ForeignKey("spiellinien.id"))
    spiellinie = relationship("SpiellinieModel", back_populates="stationen")
    aufgabe = relationship("AufgabeModel", uselist=False, back_populates="station")

class AufgabeModel(Base):
    __tablename__ = "aufgaben"
    id = Column(String, primary_key=True)
    beschreibung = Column(String)
    material = Column(String)
    station_id = Column(String, ForeignKey("stationen.id"))
    station = relationship("StationModel", back_populates="aufgabe")

class LernzielModel(Base):
    __tablename__ = "lernziele"
    id = Column(String, primary_key=True)
    beschreibung = Column(String)
