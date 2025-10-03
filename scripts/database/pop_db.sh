#!/bin/bash

# Usage: ./run_sql.sh <username> <password>
# Example: ./run_sql.sh postgres mysecretpassword postgres init.sql
# WARNING: This script will drop the database if it exists

USERNAME=$1
PASSWORD=$2

export PGPASSWORD=$PASSWORD
psql -U "$USERNAME" -d postgres -f db.sql
unset PGPASSWORD