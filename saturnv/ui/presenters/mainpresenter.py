from saturnv.ui.presenters import BasePresenter

from saturnv.database.core import Session
from saturnv.repository.postgresql.repository import SqlAlchemyRepository


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