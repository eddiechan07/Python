-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema event_planner_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `event_planner_schema` DEFAULT CHARACTER SET utf8 ;
USE `event_planner_schema` ;

-- -----------------------------------------------------
-- Table `event_planner_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `address` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`events` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `discription` VARCHAR(255) NULL,
  `location` VARCHAR(45) NULL,
  `start_time` DATETIME NULL,
  `end_time` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_events_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_events_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `event_planner_schema`.`revps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `event_planner_schema`.`revps` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `revp_status` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  `event_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_revps_users_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_revps_events1_idx` (`event_id` ASC) VISIBLE,
  CONSTRAINT `fk_revps_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `event_planner_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_revps_events1`
    FOREIGN KEY (`event_id`)
    REFERENCES `event_planner_schema`.`events` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
