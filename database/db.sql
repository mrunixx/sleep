create database sleep_db;

\c sleep_db;

create table auth.users (
    id serial primary key,
    firstname text not null,
    lastname text not null,
    email text not null,
    hpassword text not null
);