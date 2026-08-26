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

ALTER TABLE assets ADD CONSTRAINT idFOREIGN KEY (asset)

CREATE TABLE measurements (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    asset_id INTEGER  NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    timestamp TIMESTAMP NOT NULL,
    temperature DECIMAL(5,2),
    voltage DECIMAL(6,2),
    current DECIMAL(7,3),
    load_percentage DECIMAL(5,2),
    frequency DECIMAL(5,2)
);