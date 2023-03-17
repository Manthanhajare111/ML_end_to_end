import os

def set_variables():
    os.environ["DB_USER"] = "postgres"
    os.environ["DB_PASS"] = "postgres"
    os.environ["DB_NAME"] = "DirectCost"
    os.environ["DB_HOST"] = "127.0.0.1"
    os.environ["DB_PORT"] = "5432"