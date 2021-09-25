import enum


class Engines(enum.Enum):
    postgres = 'postgresql'


class Defaults:
    engine = Engines.postgres
    model = Engines.postgres
    repository = Engines.postgres


class DatabaseConfiguration:

    hostname = 'hactar.local'
    database = 'saturnv'
    username = 'saturnv'
    password = 'saturnv'
    port = '5432'
    engine = Defaults.engine

    @staticmethod
    def get_engine_url(username=username, password=password, hostname=hostname,
                       port=port, database=database, engine=engine):
        return f'{engine.value}://{username}:{password}@{hostname}:{port}/{database}'
