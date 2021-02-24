from .thememanager import Theme, ThemeManager

from pathlib import Path
LOCATION = Path(__file__).parent.absolute()


themes = ThemeManager(LOCATION / 'styles')
themes.discover()
