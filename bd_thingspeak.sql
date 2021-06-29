--
-- File generated with SQLiteStudio v3.3.3 on ter jun 29 18:54:07 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: eventos
CREATE TABLE eventos (sequencia INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, evento VARCHAR (7) NOT NULL, descricao VARCHAR (250) NOT NULL, data_e_hora DATETIME DEFAULT (DATETIME()) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
