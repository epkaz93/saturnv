from __future__ import annotations

import abc

import typing
if typing.TYPE_CHECKING:
    from .operators import OperatorComparisonBase
    from ..repository.base import RepositoryBase


class QueryBase(object, metaclass=abc.ABCMeta):

    def __init__(self, *operators, repository: RepositoryBase):
        self.operators = operators
        self.repository = repository

    def fetch(self):
        """"""
