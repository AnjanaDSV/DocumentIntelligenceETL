from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, relationship
from models import Policyholder, Policy, Claim

#define the database connection
DATABASE_URL = "postgresql://postgres:buddy2701@localhost:5432/auto_insurance"

# Create an engine instance
engine = create_engine(DATABASE_URL)



Policyholder.policies = relationship("Policy", order_by=Policy.policy_id, back_populates="policyholder")



Policy.claims = relationship("Claim", order_by=Claim.claim_id, back_populates="policy")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query the data
def get_all_policyholders():
    return session.query(Policyholder).all()

def get_all_policies():
    return session.query(Policy).all()

def get_all_claims():
    return session.query(Claim).all()

# Example usage: Fetch and print all data from the policyholders, policies, and claims tables
policyholders = get_all_policyholders()
for policyholder in policyholders:
    print(f"Policyholder: {policyholder.first_name} {policyholder.last_name}, Email: {policyholder.email}")

policies = get_all_policies()
for policy in policies:
    print(f"Policy: {policy.policy_number}, Type: {policy.policy_type}, Premium: {policy.premium_amount}")

claims = get_all_claims()
for claim in claims:
    print(f"Claim ID: {claim.claim_id}, Date: {claim.claim_date}, Amount: {claim.claim_amount}, Status: {claim.status}")

# Close the session when done
session.close()
