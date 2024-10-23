-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema blogs_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema blogs_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `blogs_schema` DEFAULT CHARACTER SET utf8 ;
USE `blogs_schema` ;

-- -----------------------------------------------------
-- Table `blogs_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`blogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`blogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`admins` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_blogs_blogs1_idx` (`blog_id` ASC) VISIBLE,
  INDEX `fk_users_has_blogs_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_blogs_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `blogs_schema`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`posts` (
  `id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `blog_id` VARCHAR(45) NULL,
  `content` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_admins1_idx` (`admin_id` ASC) VISIBLE,
  INDEX `fk_posts_blogs1_idx` (`blog_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs_schema`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `blogs_schema`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`comments` (
  `id` INT NOT NULL,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `content` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `blogs_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`files` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post_id` INT NOT NULL,
  `admin_id` INT NOT NULL,
  `content` BLOB NULL,
  `post_id` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_files_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_files_admins1_idx` (`admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_files_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `blogs_schema`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_files_admins1`
    FOREIGN KEY (`admin_id`)
    REFERENCES `blogs_schema`.`admins` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blogs_schema`.`page_viewers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blogs_schema`.`page_viewers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `view_length` VARCHAR(45) NULL,
  `ip_address` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  INDEX `fk_users_has_blogs_blogs2_idx` (`blog_id` ASC) VISIBLE,
  INDEX `fk_users_has_blogs_users1_idx` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_has_blogs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `blogs_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_blogs_blogs2`
    FOREIGN KEY (`blog_id`)
    REFERENCES `blogs_schema`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
