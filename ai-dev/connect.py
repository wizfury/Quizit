import psycopg2
from config import login_config

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print("Connected to PostgresSql server")
            return conn
    except(psycopg2.DatabaseError,Exception) as error:
        print(error)

if __name__ == "__main__":
    config = login_config()
    connect(config)
    
    