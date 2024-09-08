-- Task 8
CREATE INDEX idx_name_first
USING BTREE
ON names (
    name(1)
);
