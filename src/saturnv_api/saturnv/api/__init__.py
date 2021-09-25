from saturnv.api import configuration

if configuration.Defaults.model == configuration.Engines.postgres:
    from saturnv.api.models import postgresql as model

if configuration.Defaults.repository == configuration.Engines.postgres:
    from saturnv.api.repositories import postgresql as repository
