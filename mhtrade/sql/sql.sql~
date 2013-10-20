drop database if exists mhtrade;

CREATE TABLE `mhtrade`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  `QQ` VARCHAR(15) NULL,
  `email` VARCHAR(50) NULL,
  `self_introduction` VARCHAR(100) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = '不区分大小写';

CREATE TABLE `mhtrade`.`servers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `big_server_name` VARCHAR(10) NOT NULL,
  `server_name` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `server_name_UNIQUE` (`server_name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE `mhtrade`.`roles` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(15) NOT NULL,
  `game_id` VARCHAR(15) NOT NULL,
  `user_id` INT NULL,
  `server_id` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_roles_1_idx` (`user_id` ASC),
  INDEX `fk_roles_2_idx` (`server_id` ASC),
  CONSTRAINT `fk_roles_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `mhtrade`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_roles_2`
    FOREIGN KEY (`server_id`)
    REFERENCES `mhtrade`.`servers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE `mhtrade`.`items` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  `image_path` VARCHAR(100) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE `mhtrade`.`sold_orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `amount` INT NOT NULL,
  `unitprice` INT NOT NULL,
  `description` VARCHAR(100) NULL,
  `status` INT NOT NULL,
  `server_id` INT NULL,
  `items_id` INT NULL,
  `role_id` INT NULL,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  PRIMARY KEY (`id`),
  INDEX `fk_sold_orders_1_idx` (`server_id` ASC),
  INDEX `fk_sold_orders_2_idx` (`items_id` ASC),
  INDEX `fk_sold_orders_3_idx` (`role_id` ASC),
  CONSTRAINT `fk_sold_orders_1`
    FOREIGN KEY (`server_id`)
    REFERENCES `mhtrade`.`servers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sold_orders_2`
    FOREIGN KEY (`items_id`)
    REFERENCES `mhtrade`.`items` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sold_orders_3`
    FOREIGN KEY (`role_id`)
    REFERENCES `mhtrade`.`roles` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


