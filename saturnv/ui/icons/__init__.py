from .iconmanager import IconManager

from pathlib import Path
LOCATION = Path(__file__).parent.absolute()


icons = IconManager(LOCATION / 'img')
icons.discover()
