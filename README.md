# `sleep`: a gamified sleep-tracking experience

## How to run

### Backend + DB
- `docker compose up --build`

## Environment variables

### Database

I don't think these users actually have to exist before you run the container.

- `POSTGRES_USER`: your desired postgres username
- `POSTGRES_PASSWORD`: your desired postgres password
- `POSTGRES_DB`: your desired database name

### Backend



- `DATABASE_URL`: database url, which should be composed of the above postgres username and password (e.g `postgresql://devuser:devpassword@db:5432/sleep_db`)
- `SECRET_KEY`: a secret key of your choosing
- `ALGORITHM`: just use `HS256`