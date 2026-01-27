class ConfigError(Exception):
    pass
def load_config(filepath):
    try:
        with open(filepath,"r") as file:
            load=file.read()
            return load
    except FileNotFoundError:
        raise ConfigError(f"file not found:{filepath}")