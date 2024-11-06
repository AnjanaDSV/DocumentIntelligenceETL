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


#  Example usage: Update the email of a policyholder
def update_policyholder_email(first_name, new_email):
    policyholder = session.query(Policyholder).filter_by(first_name=first_name).first()
    if policyholder:
        policyholder.email = new_email
        session.commit()
        print(f"Email updated for Policyholder ID {first_name}")
    else:
        print(f"Policyholder with ID {first_name} not found")

# Example usage: Update a policy amount
def update_policy_amount(policy_number, new_amount):
    policy = session.query(Policy).filter_by(policy_number=policy_number).first()
    if policy:
        policy.premium_amount = new_amount
        session.commit()
        print(f"Policy amount updated for Policy ID {policy_number}")
    else:
        print(f"Policy with ID {policy_number} not found")

# Example usage: Update a claim status
def update_claim_status(policy_id, new_status):
    claim = session.query(Claim).filter_by(policy_id=policy_id).first()
    if claim:
        claim.status = new_status
        session.commit()
        print(f"Claim status updated for Claim ID {policy_id}")

update_policyholder_email(first_name ='Alice', new_email="newemail@example.com") #update email
update_policy_amount(policy_number='POL1004', new_amount=1700.0) #update policy amount
update_claim_status(policy_id='4', new_status='Pending') #update claim status

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

# Commit the changes and close the session
print("Data updated successfully!")

# Close the session when done
session.close()
