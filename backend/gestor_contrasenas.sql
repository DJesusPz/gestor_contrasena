-- Active: 1709250852898@@127.0.0.1@3306@gestor_contrasena
CREATE DATABASE IF NOT EXISTS gestor_contrasena;
use gestor_contrasena;
CREATE TABLE `baul` (
`id_baul` int NOT NULL AUTO_INCREMENT,
`plataforma` varchar(80) NOT NULL,
`usuario` varchar(80) NOT NULL,
`clave` varchar(80) NOT NULL,
PRIMARY KEY (`id_baul`),
UNIQUE KEY `plataforma` (`plataforma`,`usuario`)
)
ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Modificar la estructura de la tabla para aumentar la longitud del campo `clave`
ALTER TABLE baul MODIFY clave VARCHAR(255);

-- Crear una función para encriptar contraseñas utilizando SHA-256
DELIMITER //
CREATE FUNCTION hash_password(input_password VARCHAR(255)) RETURNS VARCHAR(64)
BEGIN
    DECLARE hashed_password VARCHAR(64);
    SET hashed_password = SHA2(input_password, 256);
    RETURN hashed_password;
END;
//