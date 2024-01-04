-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 03:36 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `house_rental`
--

-- --------------------------------------------------------

--
-- Table structure for table `house_rental_registration`
--

CREATE TABLE `house_rental_registration` (
  `Ic_Number` varchar(12) NOT NULL,
  `Customer_Name` char(30) NOT NULL,
  `Contact_Number` varchar(11) NOT NULL,
  `Type_Of_House` char(7) NOT NULL,
  `Year_Rent` int(10) NOT NULL,
  `Cleaning_Service` char(3) NOT NULL,
  `Total_Rent` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `house_rental_registration`
--

INSERT INTO `house_rental_registration` (`Ic_Number`, `Customer_Name`, `Contact_Number`, `Type_Of_House`, `Year_Rent`, `Cleaning_Service`, `Total_Rent`) VALUES
('010203149761', 'Nurul Haffizah', '01197623109', 'HOUSE A', 3, 'YES', 1900),
('751205082097', 'Nor Affidah', '01170298162', 'HOUSE A', 10, 'NO', 6000),
('790910117620', 'Zulkhairi Bahrain', '01297010612', 'HOUSE B', 9, 'YES', 3700),
('991107014501', 'Nur Saffiah', '01230910381', 'HOUSE A', 6, 'NO', 3600),
('950607084601', 'Faridah', '01894710312', 'HOUSE A', 2, 'NO', 1200),
('930810090348', 'Mohd Rashid', '01198072301', 'HOUSE B', 5, 'NO', 2000),
('950415111023', 'Mustaffa', '01197043918', 'HOUSE B', 7, 'YES', 2900),
('010212086510', 'Muhammad Danial', '01289710902', 'HOUSE A', 7, 'YES', 4300),
('040706110348', 'Nurul Syafiqah', '01151623714', 'HOUSE B', 4, 'YES', 1700),
('040706110348', 'Nurul Syafiqah', '01151623714', 'HOUSE A', 3, 'YES', 1900),
('030402148976', 'Aleesya Qaisarah', '01198702391', 'HOUSE B', 3, 'NO', 1200);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
