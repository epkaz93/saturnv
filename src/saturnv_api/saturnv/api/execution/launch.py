from __future__ import annotations

from rez.resolved_context import ResolvedContext

from saturnv.api import model

import typing


Launchable = typing.Union[model.PresetModel, model.VersionModel, model.ShortcutModel]


def launch_artifact(artifact: Launchable, command=None, detached=False):
    if isinstance(artifact, model.PresetModel):
        return launch_preset(artifact, command, detached)
    if isinstance(artifact, model.VersionModel):
        return launch_version(artifact, command, detached)
    if isinstance(artifact, model.ShortcutModel):
        return launch_shortcut(artifact, command, detached)

    raise TypeError(artifact)


def launch_preset(preset: model.PresetModel, command=None, detached=None):
    return launch_version(preset.latest_version, command, detached)


def launch_version(version: model.VersionModel, command=None, detached=False):
    packages = []

    for setting in version.packages:
        package = setting.name
        version = '.'.join(setting.value.get('version'))
        packages.append(f'{package}=={version}' if version else package)

    context = ResolvedContext(
        package_requests=packages
    )

    return context.execute_shell(command=command, block=False, detached=detached)


def launch_shortcut(version: model.ShortcutModel, command=None, detached=False):
    raise NotImplementedError
