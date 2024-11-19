import asyncio
from models import get_policyholders, get_policies, get_claims

async def main():
    try:
        print("Fetching policyholders...")
        policyholders = await get_policyholders()
        if policyholders:
            print("Policyholders:")
            for policyholder in policyholders:
                print(policyholder)
        else:
            print("No policyholders found.")   
        

        print("Fetching policies...")
        policies = await get_policies()
        if policies:
            print("Policies:")
            for policy in policies:
                print(policy)
        else:
            print("No policies found.")
       
    
        print("Fetching claims...")
        claims = await get_claims()
        if claims:
            print("Claims:")
            for claim in claims:
                print(claim)
        else:
            print("No claims found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    asyncio.run(main())
