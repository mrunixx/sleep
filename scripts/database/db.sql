drop database if exists sleep_db;
create database sleep_db;

\c sleep_db;

create schema if not exists auth;
create schema if not exists sleep;

create table if not exists auth.users (
    id serial primary key,
    firstname text not null,
    lastname text not null,
    email text not null,
    hpassword text not null
);