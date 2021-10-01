from saturnv.ui.presenters import BasePresenter

import saturnv.api
import saturnv.api.repositories.base


class MainPresenter(BasePresenter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self._configuration = configuration

        self._repository = saturnv.api.repository.Repository(saturnv.api.database.Session())

    def repository(self) -> saturnv.api.repositories.base.AbstractRepository:
        return self._repository

    @property
    def configuration(self):
        return self._configuration
