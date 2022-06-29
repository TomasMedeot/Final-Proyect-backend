DROP DATABASE IF EXISTS api_base;
CREATE DATABASE api_base;

USE api_base;

CREATE TABLE PERSON (
	ID_P int not null auto_increment,
	NAME varchar(20)NOT NULL,
	MAIL varchar(30) NOT NULL UNIQUE,
	TYPE BOOLEAN NOT NULL,
	primary key (ID_P));


CREATE TABLE STUDENT(
	ID_S int not null auto_increment,
	ID_T int not null,
    C_ABSCENSE float not null,
	`YEAR` varchar(30) not null,
	GRADE varchar(30) not null,
    primary key (ID_S));


CREATE TABLE STORAGE (
	ID_ST int not null auto_increment,
    DATE_ST varchar(10) NOT NULL, 
	TEXT_ST varchar(400),
	TYPE_ST BOOLEAN NOT NULL,
    primary key (ID_ST));

CREATE TABLE PDF_STORAGE(
	ID_PDF_ST int NOT NULL auto_increment,
	NAME_PDF varchar(30) NOT NULL,
	TYPE_PDF_ST BOOLEAN NOT NULL,
	primary key (ID_PDF_ST));