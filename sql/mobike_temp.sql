/*
Navicat MySQL Data Transfer

Source Server         : iLocalHost
Source Server Version : 50628
Source Host           : localhost:3306
Source Database       : mobike

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-06-10 19:33:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for mobike_temp
-- ----------------------------
DROP TABLE IF EXISTS `mobike_temp`;
CREATE TABLE `mobike_temp` (
  `time` datetime DEFAULT NULL,
  `bikeid` varchar(20) DEFAULT NULL,
  `biketype` smallint(6) DEFAULT NULL,
  `distid` varchar(20) DEFAULT NULL,
  `distnum` tinyint(4) DEFAULT NULL,
  `type` tinyint(4) DEFAULT NULL,
  `x` double(10,6) DEFAULT NULL,
  `y` double(10,6) DEFAULT NULL,
  `host` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
