-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- placed task such as Drop Tables, Drop vies,Drop Database, create database, connect to database to automate.
DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\connect tournament;



--This creates the table for players with columns for id and name
CREATE TABLE players
(
id SERIAL primary key,
name TEXT
);

--This creates a table for matching players together and shows the winner
--Use foreign keys on child tables. winner and loser reference the ID colum in Players table

CREATE TABLE matches
(
match_id serial primary key,
winner INTEGER references players(id),
loser INTEGER references players(id)


);


--VIEWS
--Finding the number of matches each player has played.
CREATE VIEW matches_played AS
  SELECT id, 
      COUNT(winner) AS matches
    FROM players
    LEFT JOIN matches ON winner = id
    GROUP BY id;


--The number of wins for each player.
CREATE VIEW number_of_wins AS
  SELECT id, 
    COUNT(winner) AS wins
  FROM players
  LEFT JOIN matches ON winner = id
  GROUP BY id;

--The player standings view that shows a table of player id, name, wins (in descending order), and matches played
CREATE VIEW playerStandings AS
  select 
		players.id, 
		players.name, 
		count(matches.winner) as wins, 
		(select count(*) from matches where players.id = matches.winner or players.id = matches.loser) as matches
	from 
		players
	left join
		matches on
	 		players.id = matches.winner
	group by players.id
	order by wins desc;