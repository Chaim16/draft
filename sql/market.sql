CREATE DATABASE draft;
USE draft;

CREATE TABLE `user` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(64) NOT NULL UNIQUE,
    `password` VARCHAR(1024) NOT NULL,
    `nickname` VARCHAR(64) NOT NULL,
    `gender` INT NOT NULL DEFAULT 0,
    `phone` VARCHAR(32) NOT NULL,
    `is_ban` INT NOT NULL DEFAULT 0,
    `role` VARCHAR(20) NOT NULL,
    `balance` FLOAT NOT NULL DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `order` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `amount` FLOAT NOT NULL,
    `status` VARCHAR(20) NOT NULL,
    `draft_id` BIGINT UNSIGNED NOT NULL,
    `create_time` BIGINT NOT NULL,
    `is_cancel` INT NOT NULL,
    `cancel_time` BIGINT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `category` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64) NOT NULL,
    `description` VARCHAR(1024) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `draft` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(64) NOT NULL,
    `description` VARCHAR(1024) NOT NULL,
    `image_url` VARCHAR(2048) NOT NULL,
    `price` FLOAT NOT NULL,
    `category_id` BIGINT UNSIGNED NOT NULL,
    `designer_id` BIGINT UNSIGNED NOT NULL,
    `status` VARCHAR(20) NOT NULL,
    `online_time` BIGINT NOT NULL,
    `is_outline` INT NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `browse` (
    `id` BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `draft_id` BIGINT UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
