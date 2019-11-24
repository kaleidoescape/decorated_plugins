import os
import importlib

from constants import WORKING_DIR

PLUGINS = {}

class NameConflictError(BaseException):
    """Raise for errors in adding plugins due to the same name."""

def register_plugin(name):
    """Register an instantiated plugin to the PLUGINS dictionary."""
    if name in PLUGINS:
        raise NameConflictError(
            f"Plugin name conflict: '{name}'. Double check" \
             " that all plugins have unique names.")
    def wrapper_register_plugin(plugin_class):
        plugin = plugin_class() 
        PLUGINS[name] = plugin
        return plugin
    return wrapper_register_plugin

def import_modules(dir_name):
    """Import all decorated objects inside a directory."""
    direc = os.path.join(WORKING_DIR, dir_name)
    for f in os.listdir(direc):
        path = os.path.join(direc, f)
        if (
            not f.startswith('_') 
            and not f.startswith('.') 
            and f.endswith('.py')
        ):
            file_name = f[:f.find('.py')]
            module = importlib.import_module(f'{dir_name}.{file_name}')

import_modules("plugins")
