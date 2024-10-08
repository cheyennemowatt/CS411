from typing import Optional

from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat

class AnimalManager:

    def __init__(self, animals: dict[int, Animal] = {},
        age: Optional[int] = None, status: str = "Scheduled",
        health_status: Optional[str] = None) -> None:
        pass
        

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(self, Animal) -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass
    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

