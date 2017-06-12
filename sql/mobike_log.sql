/*
Navicat MySQL Data Transfer

Source Server         : iLocalHost
Source Server Version : 50628
Source Host           : localhost:3306
Source Database       : mobike

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-06-10 19:32:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mobike_log
-- ----------------------------
DROP TABLE IF EXISTS `mobike_log`;
CREATE TABLE `mobike_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` datetime DEFAULT NULL,
  `end` datetime DEFAULT NULL,
  `left` double(10,6) DEFAULT NULL,
  `right` double(10,6) DEFAULT NULL,
  `top` double(10,6) DEFAULT NULL,
  `bottom` double(10,6) DEFAULT NULL,
  `cost` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
