CREATE DATABASE codePlusPlus;

USE codePlusPlus;

GRANT ALL on codePlusPlus.* TO 'code'@'localhost' IDENTIFIED BY '56Y6t656ghnhbhgh';

CREATE TABLE goal(
	deadline VARCHAR(8),
	parther VARCHAR(128),
	datecreated VARCHAR(8),
	diary VHARCHAR(500),
	goalcomplete CHAR(1),
	INDEX(diary(500))
) ENGINE MyISAM;

CREATE TABLE challenges(
	challenges VARCHAR(500),
	suggestionBox VARCHAR(500),
	INDEX(suggestionBox(500))
) ENGINE MyISAM;

CREATE TABLE profile(
	name VARCHAR(128),
	email VARCHAR(128),
/*	diary VARCHAR(500), */
	usersfriends VARCHAR(128),
	goals VARCHAR(500)
) ENGINE MyISAM;

CREATE TABLE diaryEntries(
	dateCreated VARCHAR(8),
	goalLink VARCHAR(128),
	success CHAR(1),
	challenges VARCHAR(500),
	tags VARCHAR(128),
	INDEX(challenges(500))
) ENGINE MyISAM;

CREATE TABLE success(
	success CHAR(1)
) ENGINE MyISAM;

