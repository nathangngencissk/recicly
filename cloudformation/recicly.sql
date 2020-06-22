create schema recicly;

alter schema recicly owner to recicly;

create table if not exists collectors
(
	id serial not null
		constraint collectors_pk
			primary key,
	name varchar,
	email varchar not null,
	password varchar not null,
	points integer default 0
);

alter table collectors owner to recicly;

create unique index if not exists collectors_id_uindex
	on collectors (id);

create table if not exists users
(
	id serial not null
		constraint users_pk
			primary key,
	name varchar(255),
	cpf varchar(11) not null,
	email varchar(255) not null,
	password varchar(255) not null,
	admin boolean default false,
	profile_picture varchar(255),
	points integer default 0 not null
);

alter table users owner to recicly;

create unique index if not exists users_cpf_uindex
	on users (cpf);

create unique index if not exists users_email_uindex
	on users (email);

create unique index if not exists users_id_uindex
	on users (id);

create table if not exists drivers
(
	id serial not null
		constraint drivers_pk
			primary key,
	name varchar(255),
	cpf varchar(11) not null,
	drivers_license varchar(50) not null,
	profile_picture varchar(255),
	email varchar(255) not null,
	password varchar(255) not null,
	points integer default 0 not null
);

alter table drivers owner to recicly;

create unique index if not exists drivers_cpf_uindex
	on drivers (cpf);

create unique index if not exists drivers_drivers_license_uindex
	on drivers (drivers_license);

create unique index if not exists drivers_email_uindex
	on drivers (email);

create unique index if not exists drivers_id_uindex
	on drivers (id);

create table if not exists adresses
(
	id serial not null
		constraint adresses_pk
			primary key,
	id_user integer
		constraint adresses_users_id_fk
			references users,
	id_collector integer
		constraint adresses_collectors_id_fk
			references collectors,
	street varchar(255) not null,
	number integer not null,
	cep varchar(8) not null,
	district varchar(255),
	city varchar(255) not null,
	country varchar(255) not null,
	state varchar(255)
);

alter table adresses owner to recicly;

create unique index if not exists adresses_id_uindex
	on adresses (id);

create table if not exists cars
(
	id serial not null
		constraint cars_pk
			primary key,
	id_driver integer
		constraint cars_drivers_id_fk
			references drivers,
	brand varchar(255) not null,
	model varchar(255) not null,
	color varchar(50)
);

alter table cars owner to recicly;

create unique index if not exists cars_id_uindex
	on cars (id);

create table if not exists requests
(
	id serial not null
		constraint requests_pk
			primary key,
	id_user integer not null
		constraint requests_users_id_fk
			references users,
	id_driver integer
		constraint requests_drivers_id_fk
			references drivers,
	id_collector integer
		constraint requests_collectors_id_fk
			references collectors,
	status varchar(50),
	points integer,
	weight integer
);

alter table requests owner to recicly;

create unique index if not exists requests_id_uindex
	on requests (id);

create table if not exists history
(
	id serial not null
		constraint history_pk
			primary key,
	id_request integer
		constraint history_requests_id_fk
			references requests,
	old_status varchar(50),
	new_status varchar(50),
	timestamp varchar(50) not null
);

alter table history owner to recicly;

create unique index if not exists history_id_uindex
	on history (id);

create table if not exists partners
(
	id serial not null
		constraint partners_pk
			primary key,
	cnpj varchar(14) not null,
	name varchar(255),
	points integer default 0
);

alter table partners owner to recicly;

create unique index if not exists partners_id_uindex
	on partners (id);

create table if not exists products
(
	id serial not null
		constraint products_pk
			primary key,
	id_partner integer
		constraint products_partners_id_fk
			references partners,
	name varchar(255) not null,
	price integer not null,
	product_picture varchar(255)
);

alter table products owner to recicly;

create unique index if not exists products_id_uindex
	on products (id);

create table if not exists orders
(
	id serial not null
		constraint orders_pk
			primary key,
	id_user integer not null
		constraint orders_users_id_fk
			references users,
	id_product integer not null
		constraint orders_products_id_fk
			references products,
	timestamp varchar(50) not null
);

alter table orders owner to recicly;

create unique index if not exists orders_id_uindex
	on orders (id);

