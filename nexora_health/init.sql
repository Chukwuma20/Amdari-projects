

-- 01_init.sql: Role & Database Initialization

-- Create the project role if it does not exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'nexora_admin') THEN
        CREATE ROLE nexora_admin WITH LOGIN PASSWORD 'password1234';
    END IF;
END
$$;

-- Create project database owned by the project role
CREATE DATABASE nexora_health
    WITH 
    OWNER = nexora_admin
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE nexora_health TO nexora_admin;