from src.ui import BasePresenter

from saturnv.api.database.core import Session
from saturnv.api.repository import SqlAlchemyRepository


class MainPresenter(BasePresenter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self._configuration = configuration

        self._repository = SqlAlchemyRepository(Session())

    def repository(self):
        return self._repository

    @property
    def configuration(self):
        return self._configuration