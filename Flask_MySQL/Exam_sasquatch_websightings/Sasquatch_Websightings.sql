-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Sasquatch_Websightings
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Sasquatch_Websightings
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Sasquatch_Websightings` DEFAULT CHARACTER SET utf8 ;
USE `Sasquatch_Websightings` ;

-- -----------------------------------------------------
-- Table `Sasquatch_Websightings`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sasquatch_Websightings`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(225) NULL,
  `confirm_password` VARCHAR(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Sasquatch_Websightings`.`sightings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Sasquatch_Websightings`.`sightings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(45) NULL,
  `date_of_sighting` DATE NULL,
  `number_of_sasquatch` INT NULL,
  `what_happened` TEXT(225) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sightings_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_sightings_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `Sasquatch_Websightings`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
