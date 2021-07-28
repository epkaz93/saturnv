# Saturnv
_Saturnv_ is an environment manager and executor (some would say "launcher") for VFX. The core implementation is written
to sit on top of the package and environment manager [Rez](www.github.com/nerdVegas/rez), but you can write your own Launcher
commands to take advantage of other systems. Using Saturnv, you define, manage and launch presets.

## Components / Sub packages
### Saturnv API
The API is the core underlying implementation of Saturnv that all other components are built on top of. It contains the 
domain, and the python interface for managing the Saturnv repository.

### Saturnv CLI
The CLI interface for managing and launching presets.

### Saturnv UI
The Qt UI for managing and launching presets.

## Database
  * TBC