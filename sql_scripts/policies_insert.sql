
-- Insert mock data into auto_policies.policies
INSERT INTO auto_policies.policies (policy_number, policyholder_id, policy_type, start_date, end_date, premium_amount) VALUES
('POL1001', 1, 'Comprehensive', '2023-01-01', '2024-01-01', 1200.00),
('POL1002', 2, 'Liability', '2022-06-15', '2023-06-15', 800.00),
('POL1003', 3, 'Collision', '2021-08-10', '2022-08-10', 950.00),
('POL1004', 4, 'Comprehensive', '2020-10-05', '2021-10-05', 1300.00),
('POL1005', 5, 'Comprehensive', '2023-03-20', '2024-03-20', 1250.00),
('POL1006', 6, 'Liability', '2023-01-01', '2024-01-01', 750.00),
('POL1007', 7, 'Collision', '2022-09-10', '2023-09-10', 1050.00),
('POL1008', 8, 'Comprehensive', '2021-07-12', '2022-07-12', 1150.00),
('POL1009', 9, 'Liability', '2023-04-10', '2024-04-10', 850.00),
('POL1010', 10, 'Collision', '2023-05-15', '2024-05-15', 950.00),
-- (Add 90 more policies in similar format to reach 100 entries)
('POL1100', 100, 'Liability', '2023-09-15', '2024-09-15', 750.00);
