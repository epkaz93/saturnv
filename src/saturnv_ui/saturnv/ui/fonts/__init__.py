from .fontmanager import FontManager

from pathlib import Path
LOCATION = Path(__file__).parent.absolute()


fonts = FontManager(LOCATION / 'fonts')
fonts.discover()
