import asyncio
from connect_to_db import connect_to_local_db

class RetrieveData:
    def __init__(self):
        self.connection = None

    async def initialize_connection(self):
        self.connection = await connect_to_local_db()
          
    async def extract_documents(self, query):
        if not self.connection:
            await self.initialize_connection()
        # Use the connection's fetch method, not a cursor
        if self.connection:
            result = await self.connection.fetch(query)
        
        else:
            result = None
       
        return result
        
    async def close_connection(self):
        if self.connection:
            await self.connection.close()

# Usage example:
async def main():
    etl = RetrieveData()
    try:
        raw_docs = await etl.extract_documents(query="SELECT policyholder_id, first_name, last_name, date_of_birth, email, phone_number, address FROM auto_policies.policyholders;")
        print(raw_docs)
    finally:
        await etl.close_connection()

if __name__ == "__main__":
    asyncio.run(main())
