import psycopg2
from alembic import command
from alembic.config import Config


def run_alembic_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


def create_database():
    conn = psycopg2.connect(
        database="hackathon",
        user="postgres",
        password="sd565211",
        host="db",
        port="5432",
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = """CREATE database hackathon_test"""

    # Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    # Closing the connection
    conn.close()


def remove_database():
    conn = psycopg2.connect(
        database="hackathon",
        user="postgres",
        password="sd565211",
        host="db",
        port="5432",
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = """DROP database hackathon_test"""

    # Creating a database
    cursor.execute(sql)
    print("Database deleted successfully........")

    # Closing the connection
    conn.close()


if __name__ == "__main__":
    import pytest

    remove_database()
    create_database()
    run_alembic_migrations()
    pytest.main(["-s", "-v"])
