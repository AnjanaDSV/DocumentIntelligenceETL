from connect_to_db import connect_to_local_db


async def get_policyholders():
    """
    Retrieve policyholder data from the database.
    """
    connection = await connect_to_local_db()
    query = """
        SELECT policyholder_id, first_name, last_name, date_of_birth, email, phone, address
        FROM auto_policies.policyholders
    """
    try:
        if connection:
            policyholders = await connection.fetch(query)
            return policyholders
        return None
    finally:
        if connection:
            await connection.close()