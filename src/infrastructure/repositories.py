from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from src.domain.interfaces import ISpiellinieRepository
from src.domain.entities import Spiellinie, Station, Aufgabe, Lernziel, User, Thema, Zielgruppe
from src.infrastructure.models import (
    SpiellinieModel, StationModel, AufgabeModel, LernzielModel, UserModel, ThemaModel, ZielgruppeModel
)

class SqlAlchemySpiellinieRepository(ISpiellinieRepository):
    """
    Enterprise Repository Implementation using SQLAlchemy.
    Handles the persistence of the Spiellinie Aggregate Root.
    """
    def __init__(self, db: Session):
        self.db = db

    def save(self, spiellinie: Spiellinie) -> None:
        # We use an 'Aggregate Root' approach: Saving a Spiellinie saves its entire graph.
        
        # 1. Ensure shared entities exist (Idempotent / Upsert logic)
        user_model = self._get_or_create_user(spiellinie.user)
        zg_model = self._get_or_create_zielgruppe(spiellinie.zielgruppe)
        thema_model = self._get_or_create_thema(spiellinie.thema)

        # 2. Create the main Spiellinie Model
        sl_model = SpiellinieModel(
            id=str(spiellinie.id),
            inhalt=spiellinie.inhalt,
            user_id=user_model.id,
            zielgruppe_id=zg_model.id,
            thema_id=thema_model.id
        )
        self.db.add(sl_model)

        # 3. Handle Stationen and their Tasks (Composition)
        for station in spiellinie.stationen:
            st_model = StationModel(
                id=str(station.id),
                name=station.name,
                ort=station.ort,
                reihenfolge=station.reihenfolge,
                spiellinie_id=sl_model.id
            )
            self.db.add(st_model)
            
            if station.aufgabe:
                aufg_model = AufgabeModel(
                    id=str(station.aufgabe.id),
                    beschreibung=station.aufgabe.beschreibung,
                    material=station.aufgabe.material,
                    station_id=st_model.id
                )
                self.db.add(aufg_model)

        # 4. Handle Lernziele (Many-to-Many)
        for lz in spiellinie.lernziele:
            lz_model = self._get_or_create_lernziel(lz)
            sl_model.lernziele.append(lz_model)

        self.db.commit()

    def get_all(self) -> List[Spiellinie]:
        models = self.db.query(SpiellinieModel).all()
        return [self._map_to_entity(m) for m in models]

    def get_by_id(self, spiellinie_id: UUID) -> Optional[Spiellinie]:
        model = self.db.query(SpiellinieModel).filter(SpiellinieModel.id == str(spiellinie_id)).first()
        if not model:
            return None
        return self._map_to_entity(model)

    # --- Private Helper Methods (Mappers & Entity Logic) ---

    def _get_or_create_user(self, user: User) -> UserModel:
        model = self.db.query(UserModel).filter(UserModel.id == str(user.id)).first()
        if not model:
            model = UserModel(id=str(user.id), name=user.name, schule=user.schule)
            self.db.add(model)
        return model

    def _get_or_create_zielgruppe(self, zg: Zielgruppe) -> ZielgruppeModel:
        model = self.db.query(ZielgruppeModel).filter(ZielgruppeModel.name == zg.name).first()
        if not model:
            model = ZielgruppeModel(id=str(zg.id), name=zg.name, beschreibung=zg.beschreibung)
            self.db.add(model)
        return model

    def _get_or_create_thema(self, th: Thema) -> ThemaModel:
        model = self.db.query(ThemaModel).filter(ThemaModel.titel == th.titel).first()
        if not model:
            model = ThemaModel(id=str(th.id), titel=th.titel, beschreibung=th.beschreibung)
            self.db.add(model)
        return model

    def _get_or_create_lernziel(self, lz: Lernziel) -> LernzielModel:
        model = self.db.query(LernzielModel).filter(LernzielModel.beschreibung == lz.beschreibung).first()
        if not model:
            model = LernzielModel(id=str(lz.id), beschreibung=lz.beschreibung)
            self.db.add(model)
        return model

    @staticmethod
    def _map_to_entity(m: SpiellinieModel) -> Spiellinie:
        """Translates a Database Model back into a Clean Domain Entity."""
        sl = Spiellinie(
            id=UUID(m.id),
            inhalt=m.inhalt,
            user=User(id=UUID(m.user.id), name=m.user.name, schule=m.user.schule),
            zielgruppe=Zielgruppe(id=UUID(m.zielgruppe.id), name=m.zielgruppe.name, beschreibung=m.zielgruppe.beschreibung),
            thema=Thema(id=UUID(m.thema.id), titel=m.thema.titel, beschreibung=m.thema.beschreibung)
        )
        
        # Map Stationen
        for sm in m.stationen:
            st = Station(id=UUID(sm.id), name=sm.name, ort=sm.ort, reihenfolge=sm.reihenfolge)
            if sm.aufgabe:
                st.aufgabe = Aufgabe(
                    id=UUID(sm.aufgabe.id), 
                    beschreibung=sm.aufgabe.beschreibung, 
                    material=sm.aufgabe.material
                )
            sl.stationen.append(st)
            
        # Map Lernziele
        for lm in m.lernziele:
            sl.lernziele.append(Lernziel(id=UUID(lm.id), beschreibung=lm.beschreibung))
            
        return sl
