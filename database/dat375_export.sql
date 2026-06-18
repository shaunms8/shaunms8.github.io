CREATE DATABASE  IF NOT EXISTS `dat375` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dat375`;
-- MySQL dump 10.13  Distrib 8.0.46, for macos15 (arm64)
--
-- Host: 127.0.0.1    Database: dat375
-- ------------------------------------------------------
-- Server version	9.7.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'c468952e-6a89-11f1-9e8e-f1085284a19a:1-154';

--
-- Table structure for table `mpdcrimedata`
--

DROP TABLE IF EXISTS `mpdcrimedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mpdcrimedata` (
  `ï»¿ObjectID` int DEFAULT NULL,
  `CFSNumber` text,
  `CFSDate` text,
  `DoW` text,
  `Month` text,
  `IncidentType` text,
  `Block_Address` text,
  `BeatName` text,
  `Neighborhood` text,
  `CaseNumber` text,
  `Subject` text,
  `FLUCR` text,
  `IBRCode` text,
  `ZIP Code` text,
  `CommissionDistrict` text,
  `Longitude` text,
  `Latitude` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `stormevents2024`
--

DROP TABLE IF EXISTS `stormevents2024`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stormevents2024` (
  `BEGIN_YEARMONTH` int DEFAULT NULL,
  `BEGIN_DAY` int DEFAULT NULL,
  `BEGIN_TIME` int DEFAULT NULL,
  `END_YEARMONTH` int DEFAULT NULL,
  `END_DAY` int DEFAULT NULL,
  `END_TIME` int DEFAULT NULL,
  `EPISODE_ID` int DEFAULT NULL,
  `EVENT_ID` int DEFAULT NULL,
  `STATE` text,
  `STATE_FIPS` int DEFAULT NULL,
  `YEAR` int DEFAULT NULL,
  `MONTH_NAME` text,
  `EVENT_TYPE` text,
  `CZ_TYPE` text,
  `CZ_FIPS` int DEFAULT NULL,
  `CZ_NAME` text,
  `WFO` text,
  `BEGIN_DATE_TIME` text,
  `CZ_TIMEZONE` text,
  `END_DATE_TIME` text,
  `INJURIES_DIRECT` int DEFAULT NULL,
  `INJURIES_INDIRECT` int DEFAULT NULL,
  `DEATHS_DIRECT` int DEFAULT NULL,
  `DEATHS_INDIRECT` int DEFAULT NULL,
  `DAMAGE_PROPERTY` text,
  `DAMAGE_CROPS` text,
  `SOURCE` text,
  `MAGNITUDE` text,
  `MAGNITUDE_TYPE` text,
  `FLOOD_CAUSE` text,
  `CATEGORY` text,
  `TOR_F_SCALE` text,
  `TOR_LENGTH` text,
  `TOR_WIDTH` text,
  `TOR_OTHER_WFO` text,
  `TOR_OTHER_CZ_STATE` text,
  `TOR_OTHER_CZ_FIPS` text,
  `TOR_OTHER_CZ_NAME` text,
  `BEGIN_RANGE` text,
  `BEGIN_AZIMUTH` text,
  `BEGIN_LOCATION` text,
  `END_RANGE` text,
  `END_AZIMUTH` text,
  `END_LOCATION` text,
  `BEGIN_LAT` text,
  `BEGIN_LON` text,
  `END_LAT` text,
  `END_LON` text,
  `EPISODE_NARRATIVE` text,
  `EVENT_NARRATIVE` text,
  `DATA_SOURCE` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-17 21:05:42
