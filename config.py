from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str
    database: str


def load_config() -> DatabaseConfig:
    """Load database configuration from environment variables."""
    load_dotenv()

    return DatabaseConfig(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "dat375"),
    )