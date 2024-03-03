# Database

## Installation
Visit https://www.postgresql.org/download/

## Setup 
Follow these steps to setup the database for the app. Note the names and password for environment variables.

1.  Open a postgres shell
       * `psql`
2.  Create a database
       * `CREATE DATABASE oire;`
3.  Create a database user
       * `CREATE USER oire WITH PASSWORD 'erio';`
4.  Prepare user for database
       * `ALTER ROLE oire SET client_encoding TO 'utf8';`
       * `ALTER ROLE oire SET default_transaction_isolation TO 'read committed';`
       * `ALTER ROLE oire SET timezone TO 'UTC';`
       * `GRANT ALL PRIVILEGES ON DATABASE oire TO oire;`
       * `ALTER DATABASE oire OWNER TO oire;`

That's all folks! :carrot: :tada: