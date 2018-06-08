CREATE TABLE type
	(id integer,
	nom varchar(30),
	primary key(id))
;

CREATE TABLE pokemon 
	(id integer,
	nom varchar(30),
	nom_ang varchar(30),
	type1 integer Not Null,
	type2 integer,
	base_stat_pv integer Not Null,
	base_stat_att integer Not Null,
	base_stat_def integer Not Null,
	base_stat_spe integer Not Null,
	base_stat_vts integer Not Null,
	primary key(id),
	foreign key(type1) references type,
	foreign key(type2) references type
	)
;

CREATE TABLE capacite(
	id integer,
	nom Varchar(30),
	type integer not null,
	PP integer,
	Puissance integer,
	Precision integer,
	Description Varchar(200),
	primary key(id),
	foreign key(type) references type)
;

CREATE TABLE atqspe(
	id integer,
	effet Varchar(100)
	)
;

CREATE TABLE evolution (
	id_bebe integer,
	id_evolution integer,
	condition varchar(20),
	foreign key(id_bebe) references pokemon,
	foreign key(id_evolution) references pokemon
	)
;


.mode csv

.import atqspe.csv atqspe
.import tablecap.csv capacite
.import pokemon.csv pokemon
.import types.csv type
.import evolution.csv evolution
