--
-- File generated with SQLiteStudio v3.3.3 on sáb jun 26 18:55:11 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: comandos
CREATE TABLE comandos (id_comando INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, texto_comando VARCHAR (250) NOT NULL, data_hora_comando DATETIME NOT NULL DEFAULT (DATETIME()));

-- Table: erros
CREATE TABLE erros (id_erro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, desc_erro VARCHAR NOT NULL, data_hora_erro DATETIME DEFAULT (DATETIME()) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
