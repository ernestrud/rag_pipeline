import os

from dotenv import load_dotenv
from dynaconf import Dynaconf

load_dotenv(override=True)


settings = Dynaconf(
    envvar_prefix="RAG",
    settings_files=[
        os.environ["SETTINGS_FILE"],  # List of configuration files (order matters)
    ],
    environments=True,
    env_switcher="ENV",
    load_dotenv=True,
    dotenv_path=".env",
    default_env="development",
)
