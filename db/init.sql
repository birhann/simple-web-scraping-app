CREATE DATABASE coolscraperapp;
use coolscraperapp;

CREATE TABLE products( 
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(500) NOT NULL, 
  image VARCHAR(500) NOT NULL,
  price FLOAT(20) NOT NULL,
  price_symbol VARCHAR(10) NOT NULL, 
  description VARCHAR(500) NOT NULL,
  PRIMARY KEY (id)) 
  CHARSET=utf8 COLLATE utf8_general_ci;