import pkgutil, importlib
from .base import BasePlugin

def load_plugins():
    plugins = []
    for _, name, _ in pkgutil.iter_modules(__path__):
        if name != 'base':
            module = importlib.import_module(f'.{name}', package=__name__)
            class_name = "".join(p.capitalize() for p in name.split('_')) + "Plugin"
            plugins.append(getattr(module, class_name)())
    return plugins
