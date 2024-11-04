from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Policyholder(Base):
    __tablename__ = 'policyholders'
    __table_args__ = {'schema': 'auto_policies'}

    policyholder_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    email = Column(String(100))
    phone = Column(String(15))
    address = Column(String(255))

class Policy(Base):
    __tablename__ = 'policies'
    __table_args__ = {'schema': 'auto_policies'}

    policy_id = Column(Integer, primary_key=True)
    policy_number = Column(String(20), unique=True)
    policyholder_id = Column(Integer, ForeignKey('auto_policies.policyholders.policyholder_id'))
    policy_type = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    premium_amount = Column(Numeric(10, 2))

    policyholder = relationship("Policyholder", back_populates="policies")

class Claim(Base):
    __tablename__ = 'claims'
    __table_args__ = {'schema': 'auto_policies'}

    claim_id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('auto_policies.policies.policy_id'))
    claim_date = Column(Date)
    claim_amount = Column(Numeric(10, 2))
    status = Column(String(20))

    policy = relationship("Policy", back_populates="claims")