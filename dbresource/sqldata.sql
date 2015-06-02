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
INSERT INTO `b_bike_common` VALUES (1000100,'222',333,'2015-06-04 15:32:04','1','2','http://www.minitcp.com/ddd',NULL);
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
  `throttle_state` varchar(20) DEFAULT NULL,
  `brake_state` varchar(20) DEFAULT NULL,
  `motor_state` varchar(20) DEFAULT NULL,
  `lock_state` varchar(20) DEFAULT NULL,
  `indicator_state` varchar(20) DEFAULT NULL,
  `longitude` decimal(10,7) DEFAULT NULL,
  `latitude` decimal(10,7) DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `time_samp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`bike_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b_bike_dynamic`
--

LOCK TABLES `b_bike_dynamic` WRITE;
/*!40000 ALTER TABLE `b_bike_dynamic` DISABLE KEYS */;
/*!40000 ALTER TABLE `b_bike_dynamic` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `u_d_history`
--

LOCK TABLES `u_d_history` WRITE;
/*!40000 ALTER TABLE `u_d_history` DISABLE KEYS */;
INSERT INTO `u_d_history` VALUES (1,100000000,1000100,12,15,'2015-06-01 15:33:03','2015-06-01 15:40:13'),(2,100000000,1000100,12,15,'2015-06-01 15:33:03','2015-06-01 15:33:03');
/*!40000 ALTER TABLE `u_d_history` ENABLE KEYS */;
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
INSERT INTO `sys_user` VALUES (100000000,'15652750943','15652750943',NULL,100,20,NULL,NULL,NULL,'2015-06-01 15:21:11','0000-00-00 00:00:00');
/*!40000 ALTER TABLE `sys_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-02  0:08:40
DELIMITER $$
DROP FUNCTION IF EXISTS `fun_distance`$$

CREATE FUNCTION `fun_distance`(lat1 float,lng1 float,lat2 float,lng2 float) RETURNS float
BEGIN
set @num=2 * 6378.137*ASIN(SQRT(POW(SIN(PI()*(lat1–(lat2))/360),2)+ COS(PI()*lat1/180)*COS(lat2*PI()/180)*POW(SIN(PI()*(lng1–(lng2))/360),2)));
RETURN @num;
END$$

DELIMITER ;