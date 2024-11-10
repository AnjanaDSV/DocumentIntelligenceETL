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

async def get_policies():
    """
    Retrieve policyholder data from the database.
    """
    connection = await connect_to_local_db()
    query = """
        SELECT policy_number, policyholder_id, policy_type, start_date, end_date, premium_amount
        FROM auto_policies.policies
    """
    try:
        if connection:
            policies = await connection.fetch(query)
            return policies
        return None
    finally:
        if connection:
            await connection.close()
async def get_claims():
    """
    Retrieve policyholder data from the database.
    """
    connection = await connect_to_local_db()
    query = """
        SELECT policy_id, claim_date, claim_amount, status
        FROM auto_policies.claims
    """
    try:
        if connection:
            claims = await connection.fetch(query)
            return claims
        return None
    finally:
        if connection:
            await connection.close()