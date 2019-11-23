import doctest
import run
import plugins.plugins

if __name__ == '__main__':
    doctest.testmod(run)
    doctest.testmod(plugins.plugins)