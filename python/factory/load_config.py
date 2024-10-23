import json
import os

def load_config() -> dict:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_directory, 'config.json')

    with open(config_path, 'r') as f:
        return json.load(f)