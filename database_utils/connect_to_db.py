import asyncpg

async def connect_to_local_db():
    """
    this function is to connect to local database
    """   
    # Connect to the PostgreSQL database
    connection = await asyncpg.connect(
        user='postgres',        
        password='buddy2701',      
        database='auto_insurance',      
        host='localhost',           
        port='5432'                    
    )
    return connection
