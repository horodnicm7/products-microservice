CREATE ROLE dev_user SUPERUSER;
ALTER USER dev_user PASSWORD 'password';
ALTER ROLE dev_user WITH login;
CREATE DATABASE online_store WITH OWNER dev_user;
GRANT ALL PRIVILEGES ON DATABASE online_store TO dev_user;