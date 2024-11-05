import asyncio
import asyncpg

async def connect_to_db():
    try:
        # Connect to the PostgreSQL database
        connection = await asyncpg.connect(
            user='postgres',          # replace with your database username
            password='buddy2701',      # replace with your database password
            database='auto_insurance',      # replace with your database name
            host='localhost',             # replace with your database host
            port='5432'                    # replace with your database port, default is 5432
        )
        
        print("Connected to the database!")
           # Example query
        schema_name = 'auto_policies'  # replace with your actual schema name
        rows = await connection.fetch(f'SELECT * FROM {schema_name}.policyholders')  # replace with your SQL query
        for row in rows:
            print(row)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the async function
asyncio.run(connect_to_db())