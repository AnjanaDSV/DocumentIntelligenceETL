import asyncio
from connect_to_db import connect_to_local_db
from models import get_policyholders, get_policies, get_claims

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
        # Fetch policyholders data from the database
        policyholders = await get_policyholders()
        
        # Print each policyholder's data in a concise format
        if policyholders:
            for policyholder in policyholders:
                print(policyholder)  
        else:
            print("No policyholders found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await etl.close_connection()
    try:
        # Fetch policyholders data from the database
        policies = await get_policies()
        
        # Print each policyholder's data in a concise format
        if policies:
            for policy in policies:
                print(policy)  
        else:
            print("No policies found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await etl.close_connection()
    try:
        # Fetch policyholders data from the database
        claims = await get_claims()
        
        # Print each policyholder's data in a concise format
        if claims:
            for claim in claims:
                print(claim)  
        else:
            print("No policies found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await etl.close_connection()

if __name__ == "__main__":
    asyncio.run(main())