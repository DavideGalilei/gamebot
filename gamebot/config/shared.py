from threading import local

from gamebot.config import Settings


class Shared(local):
    settings: Settings


shared = Shared()
