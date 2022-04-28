from __future__ import annotations

import abc

import typing
if typing.TYPE_CHECKING:
    from ..model.base import ModelBase
    from .operators import OperatorComparisonBase
    from ..repository.base import RepositoryBase

    FT = typing.Union[OperatorComparisonBase, bool]


class QueryBase(object, metaclass=abc.ABCMeta):

    def __init__(self, type_: typing.Type[ModelBase], repository: RepositoryBase):
        self.type = type_
        self.repository = repository
        self.operators = []

    def filter(self, *operators: FT):
        self.operators = operators
        return self

    def fetch(self):
        """"""
