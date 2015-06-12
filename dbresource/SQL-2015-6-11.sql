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
-- Table structure for table `t_bike_common`
--

DROP TABLE IF EXISTS `t_bike_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_bike_common` (
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
-- Dumping data for table `t_bike_common`
--

LOCK TABLES `t_bike_common` WRITE;
/*!40000 ALTER TABLE `t_bike_common` DISABLE KEYS */;
INSERT INTO `t_bike_common` VALUES (1000100,'222',333,'2015-06-04 15:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000101,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000102,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000103,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL),(1000104,'222',333,'2015-06-04 07:32:04','1','2','http://www.minitcp.com/ddd',NULL);
/*!40000 ALTER TABLE `t_bike_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_bike_dynamic`
--

DROP TABLE IF EXISTS `t_bike_dynamic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_bike_dynamic` (
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
  `mileage` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`bike_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_bike_dynamic`
--

LOCK TABLES `t_bike_dynamic` WRITE;
/*!40000 ALTER TABLE `t_bike_dynamic` DISABLE KEYS */;
INSERT INTO `t_bike_dynamic` VALUES (1000100,50,1,1,1,1,1,116.3974543,39.9180140,50,'2015-06-12 01:18:01',0,0),(1000101,50,1,1,1,1,1,116.3954543,39.9170140,50,'2015-06-12 06:43:25',1,0),(1000102,50,1,1,1,1,1,116.3964543,39.9270140,50,'2015-06-12 02:48:43',0,0),(1000103,50,1,1,1,1,1,116.3984543,39.9130140,50,'2015-06-12 04:22:22',0,0),(1000104,50,1,1,1,1,1,116.3975543,39.9178140,50,'2015-06-12 06:12:40',0,0),(1000105,50,1,1,1,1,1,116.3975543,39.9178140,50,'2015-06-10 09:00:57',0,0);
/*!40000 ALTER TABLE `t_bike_dynamic` ENABLE KEYS */;
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
  `begin_mileage` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`order_id`),
  KEY `i_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1287547 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_order`
--

LOCK TABLES `t_order` WRITE;
/*!40000 ALTER TABLE `t_order` DISABLE KEYS */;
INSERT INTO `t_order` VALUES (1287546,1000101,100000015,'2015-06-12 06:43:25',0);
/*!40000 ALTER TABLE `t_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_order_history`
--

DROP TABLE IF EXISTS `t_order_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_order_history` (
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
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_order_history`
--

LOCK TABLES `t_order_history` WRITE;
/*!40000 ALTER TABLE `t_order_history` DISABLE KEYS */;
INSERT INTO `t_order_history` VALUES (94,100000015,1000102,0,3945,'2015-06-11 16:22:27','2015-06-11 17:28:12',1287521,65),(95,100000015,1000102,0,3997,'2015-06-11 16:22:27','2015-06-11 17:29:04',1287521,66),(96,100000015,1000101,0,8,'2015-06-11 17:31:32','2015-06-11 17:31:40',1287522,10),(97,100000015,1000100,0,7,'2015-06-11 17:35:53','2015-06-11 17:36:00',1287523,10),(98,100000015,1000103,0,134,'2015-06-12 01:08:12','2015-06-12 01:10:26',1287524,10),(99,100000015,1000104,0,4,'2015-06-12 01:18:23','2015-06-12 01:18:27',1287525,10),(100,100000015,1000103,0,65,'2015-06-12 01:24:05','2015-06-12 01:25:10',1287526,10),(101,100000015,1000101,-10,80,'2015-06-12 01:58:40','2015-06-12 02:00:00',1287527,10),(102,100000015,1000103,0,3,'2015-06-12 02:13:47','2015-06-12 02:13:50',1287528,10),(103,100000015,1000102,0,839,'2015-06-12 02:14:01','2015-06-12 02:28:00',1287529,13),(104,100000015,1000101,0,814,'2015-06-12 02:28:59','2015-06-12 02:42:33',1287530,13),(105,100000015,1000101,0,9,'2015-06-12 02:42:43','2015-06-12 02:42:52',1287531,10),(106,100000015,1000102,0,3,'2015-06-12 02:48:40','2015-06-12 02:48:43',1287532,10),(107,100000015,1000104,0,3734,'2015-06-12 03:03:48','2015-06-12 04:06:02',1287533,62),(108,100000015,1000103,0,10,'2015-06-12 04:22:12','2015-06-12 04:22:22',1287534,10),(109,100000015,1000104,0,279,'2015-06-12 04:23:10','2015-06-12 04:27:49',1287535,10),(110,100000015,1000104,0,652,'2015-06-12 04:28:18','2015-06-12 04:39:10',1287536,10),(111,100000015,1000104,0,8,'2015-06-12 04:40:24','2015-06-12 04:40:32',1287537,10),(112,100000015,1000104,0,3,'2015-06-12 04:42:18','2015-06-12 04:42:21',1287538,10),(113,100000015,1000104,0,4,'2015-06-12 04:43:11','2015-06-12 04:43:15',1287539,10),(114,100000015,1000104,0,27,'2015-06-12 04:45:08','2015-06-12 04:45:35',1287540,10),(115,100000015,1000104,0,599,'2015-06-12 04:46:20','2015-06-12 04:56:19',1287541,10),(116,100000015,1000104,0,642,'2015-06-12 04:59:49','2015-06-12 05:10:31',1287542,10),(117,100000015,1000104,0,6,'2015-06-12 05:13:12','2015-06-12 05:13:18',1287543,10),(118,100000015,1000104,0,5,'2015-06-12 05:28:38','2015-06-12 05:28:43',1287544,10),(119,100000015,1000104,0,3,'2015-06-12 06:12:37','2015-06-12 06:12:40',1287545,10);
/*!40000 ALTER TABLE `t_order_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_recharge`
--

DROP TABLE IF EXISTS `t_recharge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_recharge` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `pay_to_uid` int(11) NOT NULL,
  `pay_from_uid` int(11) NOT NULL DEFAULT '0',
  `pay_type` int(11) NOT NULL,
  `pay_amount` double NOT NULL DEFAULT '0',
  `coin` int(11) NOT NULL DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `third_id` int(32) DEFAULT '0',
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=100000000 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_recharge`
--

LOCK TABLES `t_recharge` WRITE;
/*!40000 ALTER TABLE `t_recharge` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_recharge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_num` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `username` varchar(128) DEFAULT NULL,
  `balance` double DEFAULT '0',
  `points` int(11) DEFAULT NULL,
  `user_sex` varchar(16) DEFAULT NULL,
  `user_age` int(11) DEFAULT NULL,
  `occupation` varchar(16) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `edit_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `total_mileage` int(11) DEFAULT NULL,
  `total_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100000016 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (100000015,'15652750943','27b5cb718d7c4685cf89e6227214402ec5bdbe26','',280,10,NULL,NULL,NULL,'2015-06-12 06:44:24','0000-00-00 00:00:00',-10,7789);
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'zebra'
--
/*!50003 DROP FUNCTION IF EXISTS `fun_distance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `fun_distance`(lat1 float,lng1 float,lat2 float,lng2 float) RETURNS float
BEGIN
    set @num=2 * 6378.137*ASIN(SQRT(POW(SIN(PI()*(lat1-(lat2))/360),2)+ COS(PI()*lat1/180)*COS(lat2*PI()/180)*POW(SIN(PI()*(lng1-(lng2))/360),2)));
    RETURN @num;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `order_bike` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `order_bike`(bikeid INT,userid int,start_mileage int)
begin
    DECLARE order_bike_id int;
    DECLARE order_user_id int;

    DECLARE txn_error INTEGER DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN
      SET txn_error=1;
    END;

    START TRANSACTION;

    SELECT user_id into order_user_id from t_order where t_order.user_id = userid;

    SELECT bike_id into order_bike_id FROM t_bike_dynamic
    WHERE order_state=0 and bike_id=bikeid FOR UPDATE ;

    if(order_bike_id is not Null and order_user_id is Null) THEN

      update t_bike_dynamic set order_state=1 WHERE bike_id = order_bike_id;
      INSERT INTO t_order(bike_id, user_id,begin_mileage)  VALUES(order_bike_id,userid,start_mileage);

      IF(txn_error) THEN
        ROLLBACK;
      ELSE
        SELECT LAST_INSERT_ID();
        COMMIT;
      END IF;
    ELSE
      ROLLBACK;
    END IF ;
  end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-12 15:40:41
