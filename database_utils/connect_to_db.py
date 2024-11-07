import asyncpg
import os
from dotenv import load_dotenv
#Load .env if it exists
load_dotenv()  # Load environment variables from .env file

async def connect_to_local_db():
    """
    This function is to connect to the local database using environment variables.
    """
    try:
        connection = await asyncpg.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
