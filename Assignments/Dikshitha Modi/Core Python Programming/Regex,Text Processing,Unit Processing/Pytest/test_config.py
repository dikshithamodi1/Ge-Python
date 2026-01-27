import pytest
from config_loader import load_config,ConfigError
def test_config_loader():
    assert load_config("config.txt")== "hi hello"
def test_load_config_missing_file():
    # Act + Assert
    with pytest.raises(ConfigError):
        load_config("missing_config.txt")