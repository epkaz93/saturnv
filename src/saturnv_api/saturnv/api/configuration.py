class DatabaseConfiguration:

    hostname = 'deepthought.local'
    database = 'saturnv'
    username = 'saturnv'
    password = 'saturnv'
    port = '5432'

    @staticmethod
    def get_engine_url(username=username, password=password, hostname=hostname, port=port, database=database):
        return f'postgresql://{username}:{password}@{hostname}:{port}/{database}'
