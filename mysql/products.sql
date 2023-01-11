DROP TABLE IF EXISTS `products`;

CREATE TABLE `products`
(
    `id` SMALLINT(4) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `rental_class` VARCHAR(8) NOT NULL,
    `price` decimal(13,2) NOT NULL,
    `sale_price` decimal(13,2),
    `package_quantity` TINYINT UNSIGNED NOT NULL DEFAULT 1,
    `description` TINYTEXT,
    `for_rent` ENUM('0','1'),
    `keywords` VARCHAR(100)
)
    ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLE `products` WRITE;

INSERT INTO `products`
(
    `rental_class`,
    `price`,
    `sale_price`,
    `package_quantity`,
    `description`,
    `for_rent`,
    `keywords`  
)
VALUES
(
    '','a001',3.99,'','','Widget',1,'widget'
);

UNLOCK TABLES;