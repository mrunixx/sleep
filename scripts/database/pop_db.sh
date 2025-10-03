#!/bin/bash

# Usage: ./run_sql.sh <username> <password>
# Example: ./run_sql.sh postgres mysecretpassword postgres init.sql

# Read arguments
USERNAME=$1
PASSWORD=$2

# Export password so psql can use it
export PGPASSWORD=$PASSWORD

# Run the SQL script
psql -U "$USERNAME" -d postgres -f db.sql

# Unset password afterwards for safety
unset PGPASSWORD