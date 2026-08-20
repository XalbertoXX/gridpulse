CREATE TABLE IF NOT EXISTS assets (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active'
);


INSERT INTO assets (name, type, location, status)
VALUES (
    'testingname',
    'testingtype',
    'testinglocation',
    'testingstatus'
);