import os
import importlib

from constants import WORKING_DIR

PLUGINS = {}

class NameConflictError(BaseException):
    """Raise for errors in the releaser."""

def register_plugin(name):
    """Adds the decorated function to the PLUGINS dict."""
    if name in PLUGINS:
        raise NameConflictError(
            f"Config plugin name ({name}) conflict. Double check" \
             " that all plugins have unique names.")
    def decorator(function):
        PLUGINS[name] = function
        return function
    return decorator


#Here, we automatically import any Python files in this directory so that the
#register decorators above get applied. How this works:
#
#This import has to happen in the same file that the dicts and decorators
#are defined in, so that the import system uses those dicts/decorators on the
#imported objects.
#
#Also, we have to make sure we import this module before the scripts gets run.
#But this will happen if we import the constants first as well, because this
#module will get parsed first, with the import invokation.
#
#Note that it doesn't matter where we search for the decorated functions. We
#can search in the current directory or a subdirectory. But if we search in
#the current directory, we may accidentally end up with double imports. 
#It's not a huge deal, but it's nicer to separate it into its own dir anyway.
def collect_decorated(dir_name):
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

collect_decorated("plugins")