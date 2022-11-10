-- DROP SCHEM IF EXIST OTHERWISE CREATE SCHEMA
DROP SCHEMA IF EXISTS Music;
CREATE SCHEMA Music;
USE Music;

-- DROP TABLE IF EXISTS OTHERWISE CREATE TABLE
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists (
	name VARCHAR(50) PRIMARY KEY
);

CREATE TABLE albums (
	name VARCHAR(100) PRIMARY KEY,
    artist VARCHAR(50),
    FOREIGN KEY (artist)
		REFERENCES artists(name)
);

CREATE TABLE songs (
	name VARCHAR(100),
    album VARCHAR(50),
    track_num INT,
    length_sec FLOAT,
    PRIMARY KEY (album, track_num),
    FOREIGN KEY (album)
		REFERENCES albums(name)
);

-- INSERTING DATA
INSERT INTO 
	artists(name)
VALUES
	("Panic! At the Disco"),
    ("Ava Max"),
    ("Lizzo"),
    ("ILLENIUM");

INSERT INTO 
	albums(name, artist)
VALUES
	("Death of a Bachelor", "Panic! At the Disco"),
    ("Pray for the Wicked", "Panic! At the Disco"),
    ("Heaven & Hell", "Ava Max"),
    ("Cuz I Love You", "Lizzo"),
    ("Ascend", "ILLENIUM");
    
INSERT INTO 
	songs(name, album, track_num, length_sec)
VALUES
	("Victorious", "Death of a Bachelor", 1, 155.4),
    ("Don't Threaten Me with a Good Time", "Death of a Bachelor", 2, 199.8),
    ("Hallelujah", "Death of a Bachelor", 3, 180.6),
    ("Emperor's New Clothes", "Death of a Bachelor", 4, 143.4),
    ("(F**k A) Silver Lining", "Pray for the Wicked", 1, 149.4),
    ("Say Amen (Saturday Night)", "Pray for the Wicked", 2, 185.4),
    ("Hey Look Ma, I Made It", "Pray for the Wicked", 3, 150.0),
    ("My Head & My Heart", "Heaven & Hell", 1, 153),
    ("H.E.A.V.E.N", "Heaven & Hell", 2, 87.6),
    ("Kings & Queens", "Heaven & Hell", 3, 145.20),
    ("Cuz I Love You", "Cuz I Love You", 1, 180.0),
    ("Like A Girl", "Cuz I Love You", 2, 183.0),
    ("Juice", "Cuz I Love You", 3, 189.0),
    ("I Care (Intro)","Ascend", 1, 19.8),
    ("Hold on","Ascend", 2, 213.0),
    ("Good Things Fall Apart","Ascend", 3, 202.2),
    ("That's Why","Ascend", 4, 247.8);

-- SELECT Query 
SELECT s.track_num as 'Track #', s.name as 'Song',
s.length_sec as 'Length', al.name as 'Album', ar.name as 'Artist' 
FROM artists ar 
JOIN albums al ON ar.name = al.artist 
JOIN songs s ON al.name = s.album;