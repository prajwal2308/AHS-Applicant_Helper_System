-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: login
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `rskills` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'test','test','test@test.com',''),(2,'praju','praju','abc@email.com',''),(3,'praj','praj','ad@anc.com','');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` int NOT NULL,
  `file_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `uploaded_on` datetime NOT NULL,
  `status` enum('1','0') CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdata`
--

DROP TABLE IF EXISTS `userdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userdata` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `Rskillfname` varchar(50) DEFAULT NULL,
  `Rskillcontent` blob,
  `uploaded_on` datetime DEFAULT NULL,
  `status` enum('1','0') NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdata`
--

LOCK TABLES `userdata` WRITE;
/*!40000 ALTER TABLE `userdata` DISABLE KEYS */;
INSERT INTO `userdata` VALUES (1,'test','test','test@test.com','Resume.pdf',_binary 'C\nTIME MANAGEMENT\nWEB DESIGN\nHTML\nCOMMUNICATION\nAWS\nMYSQL\nUI\nPYTHON\nWORDPRESS\nCSS\nTOOLS USAGE\nDJANGO\nPLANNING\nJS\n','2023-05-07 19:25:53','1'),(2,'test','test','test@test.com','rskill.txt',_binary 'rskilltext',NULL,'1'),(3,'praju','praju','praju@abc.com','Resume.pdf',_binary 'FRAMEWORKS\n.NET\nUI\nC++\nCSS\nBI\nTESTING\nMOBILE\nWORD\nPYTHON\nAWS\nSQL\nPROGRAMMING\nCLOUD\nPROJECT MANAGEMENT\nLAN\nDATABASE\nHTML\n','2023-06-05 19:15:49','1'),(4,'praju1','praju1','praju1@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-05 13:09:14','1'),(5,'james','james','james@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-07 17:13:25','1'),(6,'new','new','new@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-07 17:17:55','1'),(7,'nithin','nithin','abc@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-08 10:27:02','1'),(8,'pava ','pava','prah@abcmccon.cin',NULL,NULL,NULL,'1'),(9,'naveen','naveen','abc@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-08 12:38:46','1'),(10,'lynsha','lynsha','aba@abc.com','Rskills.txt',_binary 'Database Administration\nDatabase Design\nDatabase Development\nSolutions Delivery\nSQL\nStructured Query Language (SQL)\nSystem Integration\nSystems Administration','2023-03-08 12:59:10','1');
/*!40000 ALTER TABLE `userdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'login'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 11:51:40
