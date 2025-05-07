import os
import yaml
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {"num_times": 1}

def load_config():
    # 1. Try current directory
    local_config = Path("_config.yaml")
    if local_config.exists():
        logger.info("Loaded config from current directory")
        return yaml.safe_load(local_config.read_text())

    # 2. Try CONFIG_PATH env variable
    config_paths = os.getenv("CONFIG_PATH", "")
    for path in config_paths.split(":"):
        if not path.strip():
            continue
        config_file = Path(path) / "_config.yaml"
        if config_file.exists():
            logger.info(f"Loaded config from {config_file}")
            return yaml.safe_load(config_file.read_text())

    # 3. Fallback: bundled config inside the package
    default_path = Path(__file__).parent / "_config.yaml"
    if default_path.exists():
        logger.info("Loaded default config bundled with the package")
        return yaml.safe_load(default_path.read_text())

    logger.warning("No config found. Using default.")
    return DEFAULT_CONFIG
