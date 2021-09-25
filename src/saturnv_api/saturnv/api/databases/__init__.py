from saturnv.api import configuration

if configuration.Defaults.engine == configuration.Engines.postgres:
    from .postgresql import Session
