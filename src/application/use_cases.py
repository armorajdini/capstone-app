from src.domain.entities import Spiellinie, Station, Aufgabe, Lernziel, User, Thema, Zielgruppe
from src.domain.value_objects import Prompt
from src.domain.interfaces import ISpiellinienGenerator, IGuardrailService, ISpiellinieRepository
from src.domain.value_objects import Zielgruppe as ZielgruppeVO, Thema as ThemaVO
from typing import List, Optional
from uuid import UUID

class GenerateSpiellinie:
    def __init__(self, generator: ISpiellinienGenerator, guardrail: IGuardrailService, repository: ISpiellinieRepository):
        self.generator = generator
        self.guardrail = guardrail
        self.repository = repository

    def execute(self, 
                zielgruppe_name: str, 
                thema_titel: str, 
                user_name: str, 
                schule: str = "3Land-Schule",
                lernziele_list: List[str] = [],
                stationen_plan: Optional[List] = None) -> Spiellinie:
        
        # Value Objects für die Guardrails
        zg_vo = ZielgruppeVO(name=zielgruppe_name)
        th_vo = ThemaVO(titel=thema_titel)

        # 1. Guardrail Check (Input)
        if not self.guardrail.validate_input(zg_vo, th_vo):
            raise ValueError(f"Input validation failed for topic: {thema_titel}")

        # 2. KI-Generierung
        enriched_prompt = self.guardrail.enrich_prompt(zg_vo, th_vo)
        raw_content = self.generator.generate(enriched_prompt)

        # 3. Guardrail Check (Output)
        if not self.guardrail.verify_output(raw_content):
            raise ValueError("Generated content is unsafe.")

        # 4. Entitäten-Mapping (7 Entitäten)
        
        # Entity 1: User
        user_entity = User(name=user_name, schule=schule)
        
        # Entity 2: Zielgruppe
        zg_entity = Zielgruppe(name=zielgruppe_name, beschreibung=f"Zielgruppe für {zielgruppe_name}")
        
        # Entity 3: Thema
        th_entity = Thema(titel=thema_titel, beschreibung=f"Fokus auf {thema_titel}")
        
        # Entity 4: Spiellinie
        spiellinie = Spiellinie(
            inhalt=raw_content,
            user=user_entity,
            zielgruppe=zg_entity,
            thema=th_entity
        )
        
        # Entity 5 & 6: Stationen & Aufgaben
        if stationen_plan:
            for i, s_req in enumerate(stationen_plan):
                aufgabe = Aufgabe(beschreibung=s_req.aufgabe, material="Wird vor Ort bereitgestellt")
                station = Station(
                    name=s_req.name, 
                    ort=s_req.ort, 
                    reihenfolge=i+1, 
                    aufgabe=aufgabe
                )
                spiellinie.stationen.append(station)
        else:
            aufg = Aufgabe(beschreibung="Den Rhein beobachten", material="Fernglas")
            stat = Station(name="Rhein-Aussicht", ort="Uferpromenade", reihenfolge=1, aufgabe=aufg)
            spiellinie.stationen.append(stat)

        # Entity 7: Lernziele
        for lz_text in lernziele_list:
            spiellinie.lernziele.append(Lernziel(beschreibung=lz_text))

        # 5. Speichern
        self.repository.save(spiellinie)

        return spiellinie

class GetSpiellinieLibrary:
    def __init__(self, repository: ISpiellinieRepository):
        self.repository = repository

    def execute(self, zielgruppe_filter: Optional[str] = None) -> List[Spiellinie]:
        all_lines = self.repository.get_all()
        if zielgruppe_filter:
            return [sl for sl in all_lines if sl.zielgruppe.name.lower() == zielgruppe_filter.lower()]
        return all_lines

class GetSpiellinieDetail:
    def __init__(self, repository: ISpiellinieRepository):
        self.repository = repository

    def execute(self, spiellinie_id: str) -> Optional[Spiellinie]:
        try:
            uid = UUID(spiellinie_id)
            return self.repository.get_by_id(uid)
        except ValueError:
            return None
