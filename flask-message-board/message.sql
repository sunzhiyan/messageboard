/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : testdb

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-06-25 23:00:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author_id` int DEFAULT NULL,
  `msg` varchar(1024) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES ('1', '1', '小时可能参加考试中长款双流机场步行街李自成', '2020-06-25 21:51:03');
INSERT INTO `message` VALUES ('2', '1', '小时可能参加考试中长款双流机场步行街李自成', '2020-06-25 21:51:10');
INSERT INTO `message` VALUES ('3', '1', 's5x64zc13zx1cd54c', '2020-06-25 21:51:18');
INSERT INTO `message` VALUES ('4', '2', '；需；需读后感成功的红包vidxc', '2020-06-25 21:51:56');
INSERT INTO `message` VALUES ('5', '2', '1514546531321', '2020-06-25 21:52:06');
INSERT INTO `message` VALUES ('6', '2', '151454653132', '2020-06-25 21:52:15');
INSERT INTO `message` VALUES ('7', '2', '15145465313', '2020-06-25 21:52:18');
INSERT INTO `message` VALUES ('8', '2', '1514546531', '2020-06-25 21:52:21');
INSERT INTO `message` VALUES ('9', '2', '151454653', '2020-06-25 21:52:23');
INSERT INTO `message` VALUES ('10', '2', '15145465', '2020-06-25 21:52:25');
