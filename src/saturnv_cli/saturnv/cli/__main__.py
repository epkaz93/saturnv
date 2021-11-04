import argparse
import enum
import getpass

import tabulate

import saturnv.api
session = saturnv.api.database.Session()
repo = saturnv.api.repository.Repository(session)
model = saturnv.api.model


class Objects(enum.Enum):

    shelf = model.ShelfModel
    preset = model.PresetModel
    shelflink = model.ShelfModel
    version = model.VersionModel

    def __eq__(self, other):
        return self.value == other or self.value.__name__ == other.__name__ or self.name == other


class Commands(enum.Enum):

    list = 'list'
    create = 'create'
    launch = 'launch'

    def __eq__(self, other):
        if isinstance(self.value, list):
            return other in self.value
        return self.value == other


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('object')
    parser.add_argument('command')

    return parser.parse_args()


def list_command(object: Objects, repository: saturnv.api.repository.Repository):
    data = []
    if object == Objects.shelf:
        for shelf in repository.all_shelves():
            print(shelf.name, shelf.uuid)
            print(shelf.versions)
    if object == Objects.preset:
        for preset in repository.all_presets():
            preset.fetch_versions()
            if preset.latest:
                data.append([preset.latest.name, preset.uuid, preset.latest.description])
            else:
                data.append(['N/A', preset.uuid, 'N/A'])

    print(tabulate.tabulate(data, headers=['Name', 'UUID', 'Descriptions']))


def create_shelf_interactive(repository: saturnv.api.repository.Repository):
    name = input('Name: ')
    path = input('Path: ')
    shelf = Shelf(name=name, path=path, author=getpass.getuser())
    repository.add_shelf(shelf)


def create_version_link_interactive(repository: saturnv.api.repository.Repository):
    pass


def launch(repository, shelf, preset, launch_command = None):
    repository.query_shelves(preset=preset)


if __name__ == '__main__':
    args = parse_args()

    repository = SqlAlchemyRepository.create_repository()

    if args.command == Commands.list:
        list_command(args.object, repository)

    if args.command == Commands.create:
        if args.object == Objects.shelf:
            create_shelf_interactive(repository)
