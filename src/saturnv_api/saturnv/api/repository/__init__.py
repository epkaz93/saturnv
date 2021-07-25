from . import repositories
from . abstractrepository import AbstractRepository

default_repository_cls = repositories.SqlAlchemyRepository


def set_default_repository_cls(repository: AbstractRepository):
    global default_repository_cls
    default_repository_cls = repository


def create_repository() -> AbstractRepository:
    return default_repository_cls.create_repository()
