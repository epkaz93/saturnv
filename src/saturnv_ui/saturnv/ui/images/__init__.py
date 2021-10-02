from .imagemanager import ScreenshotManager

from pathlib import Path
LOCATION = Path(__file__).parent.absolute()

screenshots = ScreenshotManager(LOCATION / 'screenshots')
screenshots.discover()
