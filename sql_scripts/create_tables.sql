-- Step 1: Create the policyholders table
CREATE TABLE IF NOT EXISTS auto_policies.policyholders (
    policyholder_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255)
);

-- Step 2: Create the policies table
CREATE TABLE IF NOT EXISTS auto_policies.policies (
    policy_id SERIAL PRIMARY KEY,
    policy_number VARCHAR(20) UNIQUE,
    policyholder_id INT ,
    policy_type VARCHAR(50),
    start_date DATE,
    end_date DATE,
    premium_amount NUMERIC(10, 2)
);
--
-- Step 3: Create the claims table
CREATE TABLE IF NOT EXISTS auto_policies.claims (
    claim_id SERIAL PRIMARY KEY,
    policy_id INT,
    claim_date DATE,
    claim_amount NUMERIC(10, 2),
    status VARCHAR(20)
);

