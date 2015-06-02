CREATE DATABASE  IF NOT EXISTS `zebra` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `zebra`;
-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: zebra
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `b_bike_common`
--

DROP TABLE IF EXISTS `b_bike_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_bike_common` (
  `bike_id` int(11) NOT NULL,
  `bike_type` varchar(64) NOT NULL,
  `price` double NOT NULL,
  `register_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `power_type` varchar(64) DEFAULT NULL,
  `motor_type` varchar(64) DEFAULT NULL,
  `images` varchar(64) DEFAULT NULL,
  `note` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`bike_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b_bike_common`
--

LOCK TABLES `b_bike_common` WRITE;
/*!40000 ALTER TABLE `b_bike_common` DISABLE KEYS */;
INSERT INTO `b_bike_common` VALUES (1000100,'222',333,'2015-06-04 15:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000101,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000102,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000103,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000104,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL);
/*!40000 ALTER TABLE `b_bike_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b_bike_dynamic`
--

DROP TABLE IF EXISTS `b_bike_dynamic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_bike_dynamic` (
  `bike_id` int(11) NOT NULL,
  `cur_power` int(11) DEFAULT NULL,
  `throttle_state` int(11) DEFAULT '1',
  `brake_state` int(11) DEFAULT '1',
  `motor_state` int(11) DEFAULT '1',
  `lock_state` int(11) DEFAULT '1',
  `indicator_state` int(11) DEFAULT '1',
  `longitude` decimal(10,7) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `time_samp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `order_state` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`bike_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b_bike_dynamic`
--

LOCK TABLES `b_bike_dynamic` WRITE;
/*!40000 ALTER TABLE `b_bike_dynamic` DISABLE KEYS */;
INSERT INTO `b_bike_dynamic` VALUES (1000100,50,1,1,1,1,1,116.3974543,39.9180140,50,'2015-06-02 00:10:56',0),(1000101,50,1,1,1,1,1,116.3954543,39.9170140,50,'2015-06-02 00:10:37',0),(1000102,50,1,1,1,1,1,116.3964543,39.9270140,50,'2015-06-02 00:11:00',0),(1000103,50,1,1,1,1,1,116.3984543,39.9130140,50,'2015-06-02 14:07:48',0),(1000104,50,1,1,1,1,1,116.3975543,39.9178140,50,'2015-06-02 00:11:06',0);
/*!40000 ALTER TABLE `b_bike_dynamic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permission`
--

DROP TABLE IF EXISTS `permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permission` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '权限id',
  `permission_name` varchar(32) DEFAULT NULL COMMENT '权限名',
  `permission_sign` varchar(128) DEFAULT NULL COMMENT '权限标识,程序中判断使用,如"user:create"',
  `description` varchar(256) DEFAULT NULL COMMENT '权限描述,UI界面显示使用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC COMMENT='权限表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permission`
--

LOCK TABLES `permission` WRITE;
/*!40000 ALTER TABLE `permission` DISABLE KEYS */;
INSERT INTO `permission` VALUES (1,'用户','user:create',NULL);
/*!40000 ALTER TABLE `permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '角色id',
  `role_name` varchar(32) DEFAULT NULL COMMENT '角色名',
  `role_sign` varchar(128) DEFAULT NULL COMMENT '角色标识,程序中判断使用,如"admin"',
  `description` varchar(256) DEFAULT NULL COMMENT '角色描述,UI界面显示使用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC COMMENT='角色表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'admin','admin','管理员');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permission`
--

DROP TABLE IF EXISTS `role_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_permission` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '表id',
  `role_id` bigint(20) unsigned DEFAULT NULL COMMENT '角色id',
  `permission_id` bigint(20) unsigned DEFAULT NULL COMMENT '权限id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC COMMENT='角色与权限关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permission`
--

LOCK TABLES `role_permission` WRITE;
/*!40000 ALTER TABLE `role_permission` DISABLE KEYS */;
INSERT INTO `role_permission` VALUES (1,2,1);
/*!40000 ALTER TABLE `role_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sys_user`
--

DROP TABLE IF EXISTS `sys_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_num` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(128) DEFAULT NULL,
  `balance` double DEFAULT '0',
  `integral` int(11) DEFAULT '0',
  `user_sex` varchar(16) DEFAULT NULL,
  `user_age` int(11) DEFAULT NULL,
  `occupation` varchar(16) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `edit_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100000001 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sys_user`
--

LOCK TABLES `sys_user` WRITE;
/*!40000 ALTER TABLE `sys_user` DISABLE KEYS */;
INSERT INTO `sys_user` VALUES (100000000,'15652750943','15652750943','eric',3392,20,'1',15,NULL,'2015-06-02 14:07:48','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `sys_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_order`
--

DROP TABLE IF EXISTS `t_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `bike_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `order_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mileage` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100010 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_order`
--

LOCK TABLES `t_order` WRITE;
/*!40000 ALTER TABLE `t_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_d_history`
--

DROP TABLE IF EXISTS `u_d_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `u_d_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `bike_id` int(11) NOT NULL,
  `mileage` double NOT NULL DEFAULT '0',
  `costTime` int(11) NOT NULL DEFAULT '0',
  `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `order_id` int(11) NOT NULL,
  `cost` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `u_d_history`
--

LOCK TABLES `u_d_history` WRITE;
/*!40000 ALTER TABLE `u_d_history` DISABLE KEYS */;
INSERT INTO `u_d_history` VALUES (1,100000000,1000100,12,15,'2015-06-01 15:33:03','2015-06-01 15:40:13',0,0),(2,100000000,1000100,12,15,'2015-06-01 15:33:03','2015-06-01 15:33:03',0,0),(3,100000000,1000103,0,5,'2015-06-02 13:56:28','2015-06-02 14:02:04',100004,5),(4,123,1000103,0,0,'2015-06-02 14:02:45','2015-06-02 14:03:36',100005,1),(5,123,1000103,0,0,'2015-06-02 14:04:28','2015-06-02 14:04:32',100006,1),(6,123,1000103,0,0,'2015-06-02 14:05:22','2015-06-02 14:05:26',100007,1),(7,123,1000103,0,0,'2015-06-02 14:06:59','2015-06-02 14:07:42',100008,1),(8,100000000,1000103,0,0,'2015-06-02 14:07:44','2015-06-02 14:07:48',100009,1);
/*!40000 ALTER TABLE `u_d_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `username` varchar(50) NOT NULL COMMENT '用户名',
  `password` char(64) NOT NULL COMMENT '密码',
  `state` int(11) NOT NULL DEFAULT '0' COMMENT '状态',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1000000052 DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'starzou','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92',1,'2014-07-17 04:59:08'),(1000000000,'shuai','qqqq',0,'2015-05-25 15:26:43'),(1000000001,'15652750944','qqqq',0,'2015-05-26 00:31:35'),(1000000002,'shuai1','qqqq',0,'2015-05-26 00:36:20'),(1000000003,'shuai1','qqqq',0,'2015-05-26 00:36:41'),(1000000004,'shuai1','qqqq',0,'2015-05-26 00:37:33'),(1000000005,'shuai1','qqqq',0,'2015-05-26 00:38:09'),(1000000006,'shuai1','qqqq',0,'2015-05-26 00:38:58'),(1000000007,'shuai1','qqqq',0,'2015-05-26 00:39:57'),(1000000008,'shuai1','qqqq',0,'2015-05-26 00:40:19'),(1000000009,'shuai1','qqqq',0,'2015-05-26 00:41:05'),(1000000010,'shuai1','qqqq',0,'2015-05-26 00:41:33'),(1000000011,'shuai1','qqqq',0,'2015-05-26 00:41:51'),(1000000012,'shuai1','qqqq',0,'2015-05-26 00:42:05'),(1000000013,'shuai1','qqqq',0,'2015-05-26 00:42:56'),(1000000014,'shuai1','qqqq',0,'2015-05-26 00:43:44'),(1000000015,'shuai1','qqqq',0,'2015-05-26 00:44:10'),(1000000016,'shuai1','qqqq',0,'2015-05-26 00:46:15'),(1000000017,'shuai1','qqqq',0,'2015-05-26 00:46:38'),(1000000018,'shuai1','qqqq',0,'2015-05-26 00:46:58'),(1000000019,'shuai1','qqqq',0,'2015-05-26 00:54:10'),(1000000020,'shuai1','qqqq',0,'2015-05-26 00:54:26'),(1000000021,'shuai1','qqqq',0,'2015-05-26 00:54:42'),(1000000022,'shuai1','qqqq',0,'2015-05-26 00:55:33'),(1000000023,'shuai1','qqqq',0,'2015-05-26 00:56:42'),(1000000024,'shuai1','qqqq',0,'2015-05-26 00:56:59'),(1000000025,'shuai1','qqqq',0,'2015-05-26 00:57:18'),(1000000026,'shuai1','qqqq',0,'2015-05-26 00:58:51'),(1000000027,'shuai1','qqqq',0,'2015-05-26 01:39:12'),(1000000028,'shuai1','qqqq',0,'2015-05-26 01:39:50'),(1000000029,'shuai1','qqqq',0,'2015-05-26 01:44:42'),(1000000030,'shuai1','qqqq',0,'2015-05-26 01:45:04'),(1000000031,'shuai1','qqqq',0,'2015-05-26 01:45:30'),(1000000032,'shuai1','qqqq',0,'2015-05-26 01:47:17'),(1000000033,'shuai1','qqqq',0,'2015-05-26 03:02:09'),(1000000034,'1234567','123456',0,'2015-05-26 03:02:48'),(1000000035,'1234567\\','1234567\\',0,'2015-05-26 05:33:09'),(1000000036,'shuai1','qqqq',0,'2015-05-26 08:54:13'),(1000000037,'shuai1','qqqq',0,'2015-05-26 08:54:28'),(1000000038,'shuai1','qqqq',0,'2015-05-27 07:24:07'),(1000000039,'15652750942','15652750942',0,'2015-05-27 07:40:15'),(1000000040,'15652750945','15652750942',0,'2015-05-27 07:41:57'),(1000000041,'15652750988','3163504123',0,'2015-05-27 11:49:19'),(1000000042,'15555555555','15555555555',0,'2015-05-27 12:18:24'),(1000000043,'15652750922','15652750922',0,'2015-05-29 02:07:09'),(1000000044,'15652705943','15652705943',0,'2015-05-29 09:50:45'),(1000000045,'15652750948','15652750948',0,'2015-05-29 09:52:43'),(1000000046,'15652750522','15652750522',0,'2015-05-29 14:32:11'),(1000000047,'15444444444','15444444444',0,'2015-05-30 12:33:23'),(1000000048,'15652750521','15652750522',0,'2015-05-30 12:47:22'),(1000000049,'15652777777','15652777777',0,'2015-05-30 13:34:40'),(1000000050,'15652777778','15652777778',0,'2015-05-30 14:20:33'),(1000000051,'15652750921','15652750921',0,'2015-05-30 15:24:59');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_role` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '表id',
  `user_id` bigint(20) unsigned DEFAULT NULL COMMENT '用户id',
  `role_id` bigint(20) unsigned DEFAULT NULL COMMENT '角色id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC COMMENT='用户与角色关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (1,1,1);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-02 22:10:25
