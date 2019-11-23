import os
import json

from constants import DEFAULT_CONFIG_DIR
from decorators import PLUGINS

class ConfigParseError(BaseException):
    """Raise for errors parsing the user's config file."""

def process_sentence(sentence, plugin_names=[]):
    """
    Process a sentence using the requested plugins.

    >>> process_sentence("replace <xml> tags", ["replace_tags"])
    'replace <TAG> tags'
    """
    new_sentence = sentence
    for name in plugin_names:
        new_sentence = PLUGINS[name](new_sentence)
    return new_sentence

def _process_file(instream, outstream, processors):
    """Process items in the instream into the outstream."""
    for i, line in enumerate(instream):
        sentence = line.strip()
        new_sentence = process_sentence(sentence, processors)
        outstream.write(new_sentence + os.linesep)

def process_file(infile, outfile, processors):
    """Process the infile of one sentence per line into an outfile."""
    with open(infile, 'r', encoding='utf-8', newline=os.linesep) as instream, \
         open(outfile, 'w', encoding='utf-8', newline=os.linesep) as outstream:
        return _process_file(instream, outstream, processors)

def parse_config(config):
    """
    Return a config dictionary with updated values, or raise an error.

    >>> config = {"input": "./data/input.txt"}
    >>> parse_config(config)
    {'input': './data/input.txt', 'processors': []}
    """
    if 'input' not in config:
           raise ConfigParseError("config missing input file")
    if not os.path.exists(config['input']):
           raise FileNotFoundError(f"input file not found: {config['input']}")
    if "processors" not in config:
        config["processors"] = []
    for name in config['processors']:
        if name not in PLUGINS:
            raise ConfigParseError(f"unrecognized plugin: '{name}'." \
                  f" Expected one of: {list(PLUGINS.keys())}")
    return config

def run():
    """
    Run the example scenario which will process sentences from the
    example input `./data/input.txt` and create an example output: 
    `./data/input.txt.processed`.
    """
    config_file = os.path.join(DEFAULT_CONFIG_DIR, 'config.json')
    with open(config_file, 'r', encoding='utf-8') as instream:
        config = json.load(instream)
        
    config = parse_config(config)
    processors = config["processors"]

    infile = config["input"]
    outfile = infile + '.processed'
    process_file(infile, outfile, processors)


if __name__ == '__main__':
    run()