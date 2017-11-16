DROP TABLE IF EXISTS urls;
CREATE TABLE `urls` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `page_url` varchar(255) DEFAULT NULL,
  `img_url` varchar(255) DEFAULT NULL,
  `jiforjpg` enum('gif','jpg') DEFAULT NULL,
  `img_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4009 DEFAULT CHARSET=utf8