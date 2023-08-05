from alembic import command
from alembic.config import Config


def run_alembic_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    import pytest

    run_alembic_migrations()
    pytest.main(["-s", "-v"])
