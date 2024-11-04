
-- Insert mock data into auto_policies.claims
INSERT INTO auto_policies.claims (policy_id, claim_date, claim_amount, status) VALUES
(1, '2023-02-15', 500.00, 'Paid'),
(2, '2022-07-01', 250.00, 'Pending'),
(3, '2022-01-22', 1000.00, 'Rejected'),
(4, '2021-12-12', 800.00, 'Paid'),
(5, '2023-04-05', 450.00, 'Paid'),
(6, '2023-06-18', 620.00, 'Pending'),
(7, '2023-02-19', 700.00, 'Paid'),
(8, '2022-11-25', 530.00, 'Rejected'),
(9, '2023-03-12', 400.00, 'Pending'),
(10, '2023-05-20', 350.00, 'Paid'),
-- (Add 90 more claims in similar format to reach 100 entries)
(100, '2024-01-10', 300.00, 'Pending');
