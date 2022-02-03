# BaseGD

## Código Query para crear base de datos phytonlogin

CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pythonlogin`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'test', 'test', 'test@test.com');




CREATE TABLE IF NOT EXISTS `payrolls` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`status` varchar(255) NOT NULL,
  	`employee_number` varchar(255) NOT NULL,
  	`name` varchar(255) NOT NULL,
  	`last_name` varchar(255) NOT NULL,
  	`second_lastname` varchar(255) NOT NULL,
  	`phone` varchar(255) NOT NULL,
  	`email` varchar(255) NOT NULL,
  	`business` varchar(50) NOT NULL,
  	`client` varchar(255) NOT NULL,
  	`service` varchar(255) NOT NULL,
  	`turn` varchar(255) NOT NULL,
  	`daily_salary` decimal(65) NOT NULL,
  	`biweekly_salary` decimal(65) NOT NULL,
  	`monthly_salary` decimal(65) NOT NULL,
  	`bank` varchar(255) NOT NULL,
  	`account_number` varchar(255) NOT NULL,
  	`clabe` varchar(255) NOT NULL,

    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
