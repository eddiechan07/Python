-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Normalization
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Normalization
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Normalization` DEFAULT CHARACTER SET utf8 ;
USE `Normalization` ;

-- -----------------------------------------------------
-- Table `Normalization`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Normalization`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`students` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_students_dojos_idx` (`dojos_id` ASC) VISIBLE,
  CONSTRAINT `fk_students_dojos`
    FOREIGN KEY (`dojos_id`)
    REFERENCES `Normalization`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Normalization`.`addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `zip_code` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Normalization`.`shared_addresses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`shared_addresses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `address_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_students_has_addresses_addresses1_idx` (`address_id` ASC) VISIBLE,
  INDEX `fk_students_has_addresses_students1_idx` (`student_id` ASC) VISIBLE,
  CONSTRAINT `fk_students_has_addresses_students1`
    FOREIGN KEY (`student_id`)
    REFERENCES `Normalization`.`students` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_has_addresses_addresses1`
    FOREIGN KEY (`address_id`)
    REFERENCES `Normalization`.`addresses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Normalization`.`interests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`interests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Normalization`.`students_has_interests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Normalization`.`students_has_interests` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `students_id` INT NOT NULL,
  `interests_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_students_has_interests_interests1_idx` (`interests_id` ASC) VISIBLE,
  INDEX `fk_students_has_interests_students1_idx` (`students_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_students_has_interests_students1`
    FOREIGN KEY (`students_id`)
    REFERENCES `Normalization`.`students` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_has_interests_interests1`
    FOREIGN KEY (`interests_id`)
    REFERENCES `Normalization`.`interests` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
