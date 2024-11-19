from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from connect_to_db import connect_to_local_db

# Database setup
Base = declarative_base()
connection_string = connect_to_local_db()
engine = create_async_engine(connection_string, echo=False, future=True)
AsyncSessionMaker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Model definitions
class Policyholder(Base):
    __tablename__ = 'policyholders'
    __table_args__ = {'schema': 'auto_policies'}

    policyholder_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String)
    phone = Column(String)
    address = Column(String)

    def __repr__(self):
        return f"<Policyholder(id={self.policyholder_id}, name={self.first_name} {self.last_name}, email={self.email})>"


class Policy(Base):
    __tablename__ = 'policies'
    __table_args__ = {'schema': 'auto_policies'}

    policy_number = Column(String, primary_key=True)
    policyholder_id = Column(Integer, ForeignKey('auto_policies.policyholders.policyholder_id'))  # Add schema
    policy_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    premium_amount = Column(Float)
    policyholder = relationship('Policyholder', back_populates='policies')

    def __repr__(self):
        return (f"<Policy(number={self.policy_number}, type={self.policy_type}, "
                f"premium={self.premium_amount}, start_date={self.start_date}, end_date={self.end_date})>")


class Claim(Base):
    __tablename__ = 'claims'
    __table_args__ = {'schema': 'auto_policies'}

    claim_id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('auto_policies.policies.policy_number'))  # Add schema
    claim_date = Column(Date)
    claim_amount = Column(Float)
    status = Column(String)
    policy = relationship('Policy', back_populates='claims')

    def __repr__(self):
        return (f"<Claim(id={self.claim_id}, policy_id={self.policy_id}, amount={self.claim_amount}, "
                f"status={self.status}, claim_date={self.claim_date})>")

Policyholder.policies = relationship('Policy', back_populates='policyholder')
Policy.claims = relationship('Claim', back_populates='policy')

# Async functions
async def get_policyholders():
    async with AsyncSessionMaker() as session:
        result = await session.execute(select(Policyholder))
        return result.scalars().all()

async def get_policies():
    async with AsyncSessionMaker() as session:
        result = await session.execute(select(Policy))
        return result.scalars().all()

async def get_claims():
    async with AsyncSessionMaker() as session:
        result = await session.execute(select(Claim))
        return result.scalars().all()
