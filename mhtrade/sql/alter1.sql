ALTER TABLE `mhtrade`.`users` 
CHANGE COLUMN `email` `email` VARCHAR(50) NOT NULL ,
ADD COLUMN `level` VARCHAR(10) NOT NULL DEFAULT 'user' AFTER `self_introduction`,
ADD COLUMN `code` INT NOT NULL DEFAULT 0 AFTER `level`;