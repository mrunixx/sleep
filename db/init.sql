drop schema if exists auth;
drop schema if exists sleep;

create schema if not exists auth;
create schema if not exists sleep;


-- authentication relations
create table if not exists auth.users (
    id serial primary key,
    firstname text not null,
    lastname text not null,
    email text unique not null,
    hpassword text not null
);

create table if not exists auth.sessions (
    token text primary key,
    user_id int not null references auth.users(id) on delete cascade,
    user_firstname text not null,
    user_lastname text not null,
    user_email text not null
);

-- sleep tracking related relations
create table if not exists sleep.entry (
    id serial primary key,
    user_id int not null references auth.users(id) on delete cascade,
    start_dt_utc timestamptz not null,
    end_dt_utc timestamptz not null,
    tz_name text not null,
    sleep_time_s numeric not null
);