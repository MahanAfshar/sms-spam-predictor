from pathlib import Path

def get_base_path():
    try:
        return Path(__file__).resolve().parent.parent.parent
    except NameError:
        return Path.cwd().resolve().parent