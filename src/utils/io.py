import yaml
from utils.paths import get_base_path

def load_config():
    base_path = get_base_path()
    path = base_path / "configs" / "config.yml"

    with open(path, "r") as f:
        return yaml.safe_load(f)