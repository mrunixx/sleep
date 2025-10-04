# `sleep`: a gamified sleep-tracking experience

## Overview

We wanted to gamify the experience of sleeping to encourage individuals to sleep more. We take an approach similar to YPT, and provide functionalities like leaderboards, metrics, and more.

## Deployment

### Environment variables
We need to set up some environment variables so the system can run.
#### Database
- `POSTGRES_USER`: your desired postgres username
- `POSTGRES_PASSWORD`: your desired postgres password
- `POSTGRES_DB`: your desired database name

#### Backend
- `DATABASE_URL`: database url, which should be composed of the above postgres username and password (e.g `postgresql://devuser:devpassword@db:5432/sleep_db`)
- `SECRET_KEY`: a secret key of your choosing
- `ALGORITHM`: just use `HS256`


### Running the backend and database
- `docker compose up --build`
