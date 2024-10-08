from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
class MigrationPath:
    def __init__(self,
                current_date: str,
                 current_location: str,
                 start_location: Habitat, 
                 migration_path: MigrationPath, 
                 destination: Habitat, start_date: str, 
                 duration: Optional[int] = None
                 
                 ) -> None:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def get_migration_paths() -> list[MigrationPath]:
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass
    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass
    pass
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
