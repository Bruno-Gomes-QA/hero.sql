create = """
CREATE DATABASE castelo;
USE castelo;

CREATE TABLE tbl_titulos (
	id_titulo INT PRIMARY KEY AUTO_INCREMENT,
	nome_titulo VARCHAR(255) NOT NULL,
	patente_titulo VARCHAR(255) NOT NULL
);

CREATE TABLE tbl_soldados (
	id_soldado INT PRIMARY KEY AUTO_INCREMENT,
	nome_soldado VARCHAR(255) NOT NULL,
	altura_soldado DECIMAL(10,2) NOT NULL,
	nascimento_soldado DATE NOT NULL,
	fk_titulo INT
);

ALTER TABLE tbl_soldados
ADD CONSTRAINT
FOREIGN KEY (fk_titulo) 
REFERENCES tbl_titulos (id_titulo) 
;
"""

insert = """
-- Títulos
INSERT INTO tbl_titulos (nome_titulo, patente_titulo)
VALUES
('Ferreiro', 'Trabalhador'),
('Soldado', 'Real'),
('Arqueiro', 'Real'),
('Médico', 'Trabalhador');

-- Soldados
INSERT INTO tbl_soldados (nome_soldado, altura_soldado, nascimento_soldado, fk_titulo)
VALUES
('Arthur Pendragon', 1.80, '1150-05-14', 2),
('Lancelot du Lac', 1.75, '1165-08-22', 3),
('Gawain de Orkney', 1.78, '1172-01-30', 2),
('Merlin Ambrosius', 1.70, '1130-04-18', 4),
('Gareth de Orkney', 1.82, '1155-11-11', 1),
('Robin Hood', 1.76, '1185-02-27', 3),
('Percival de Galles', 1.79, '1160-06-15', 2),
('Tristan de Lyonesse', 1.73, '1175-09-09', 4),
('Galahad de Corbenic', 1.85, '1141-12-21', 2),
('Bors de Ganis', 1.77, '1125-03-05', 1);
"""
