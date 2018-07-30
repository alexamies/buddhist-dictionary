/**
 * Firsttime only setup relational database
 * 
 * Change password value before executing
 */

USE mysql;

CREATE DATABASE IF NOT EXISTS ntireader CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

CREATE user IF NOT EXISTS 'app_user' IDENTIFIED BY '***';
GRANT SELECT, INSERT, UPDATE ON ntireader.* TO 'app_user'@'%';
GRANT SELECT, INSERT, UPDATE ON ntireader.* TO 'proxyuser'@'%';

USE ntireader;
