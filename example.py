import os

from constants import DEFAULT_CONFIG_DIR

def example():
    """
    Run the example scenario which will process sentences from the
    example input `./data/input.txt` and create an example output: 
    `./data/input.txt.processed`.
    """
    config_file = os.path.join(DEFAULT_CONFIG_DIR, 'config.json')
    run(config_file)

if __name__ == '__main__':
    example()