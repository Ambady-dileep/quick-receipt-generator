List of sql commands which i've use in the sql shell for this project

\c receipt_db;
CREATE DATABASE receipt_db;
CREATE USER ambady_user WITH PASSWORD 'Ambady@17';
ALTER ROLE ambady_user SET client_encoding TO 'utf8';
ALTER ROLE ambady_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ambady_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE receipt_db TO ambady_user;


