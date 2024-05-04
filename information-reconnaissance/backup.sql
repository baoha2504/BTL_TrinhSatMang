-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: trinhsatthongtin
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Chủ tịch quốc hội Vương Đình Huệ'),(2,'Phó chủ nhiệm Văn phòng Quốc hội bị bắt'),(3,'Tập đoàn Thuận An'),(4,'Tập đoàn Vạn Thịnh Phát'),(5,'Xung đột Nga Ukraina'),(6,'Bầu cử Tổng thống Mỹ');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `object`
--

DROP TABLE IF EXISTS `object`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `object` (
  `object_id` int(11) NOT NULL AUTO_INCREMENT,
  `object_name` varchar(255) DEFAULT NULL,
  `object_link_web` varchar(255) DEFAULT NULL,
  `object_link_youtube` varchar(255) DEFAULT NULL,
  `object_link_facebook` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`object_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `object`
--

LOCK TABLES `object` WRITE;
/*!40000 ALTER TABLE `object` DISABLE KEYS */;
INSERT INTO `object` VALUES (1,'Việt Tân','https://viettan.org/','https://www.youtube.com/@VietTan/','https://web.facebook.com/viettan'),(2,'VOA Tiếng Việt','https://www.voatiengviet.com/p/6159.html','https://www.youtube.com/@VOATiengViet/','https://web.facebook.com/VOATiengViet'),(3,'RFA Tiếng Việt','https://www.rfa.org/vietnamese/','https://www.youtube.com/@rfavietnamese/','https://web.facebook.com/RFAVietnam'),(4,'BBC Tiếng Việt','https://www.bbc.com/vietnamese','https://www.youtube.com/@bbctiengviet/','https://web.facebook.com/BBCnewsVietnamese'),(5,'Vịt Vui Vẻ',NULL,'https://www.youtube.com/@vitvuive/',NULL),(6,'Dân Trí','https://dantri.com.vn/xa-hoi/chinh-tri.htm',NULL,NULL),(7,'VnExpress','https://vnexpress.net/thoi-su/chinh-tri',NULL,NULL),(8,'Ngẫm Sử Thi',NULL,'https://www.youtube.com/@ngamsuthiNKD/',NULL);
/*!40000 ALTER TABLE `object` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 11:46:45
