-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2017-02-21 12:30:48
-- 服务器版本： 10.1.13-MariaDB
-- PHP Version: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fyp`
--

-- --------------------------------------------------------

--
-- 表的结构 `indexing`
--

CREATE TABLE `indexing` (
  `Tag_ID` int(10) NOT NULL,
  `Image_ID` varchar(500) NOT NULL,
  `Tag` varchar(500) NOT NULL,
  `ClickTimes` int(20) NOT NULL,
  `SuggestClickTimes` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `indexing`
--

INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES
(1, '1', 'animal', 6, 0),
(2, '1', 'dog', 10, 0),
(3, '1', 'white', 3, 0),
(4, '1', 'cute', 5, 0),
(5, '2', 'animal', 2, 0),
(6, '2', 'dog', 5, 0),
(7, '2', 'yellow', 3, 0),
(8, '2', 'cute', 1, 0),
(9, '3', 'human', 9, 0),
(10, '3', 'woman', 0, 0),
(11, '3', 'black', 6, 0),
(12, '3', 'face', 7, 0),
(13, '4', 'human', 7, 0),
(14, '4', 'man', 7, 0),
(15, '4', 'white', 6, 0),
(16, '4', 'face', 7, 0),
(17, '5', 'sea', 7, 0),
(18, '5', 'sky', 7, 0),
(19, '5', 'landscape', 7, 0),
(20, '5', 'tree', 7, 0),
(21, '5', 'people', 7, 0),
(22, '5', 'canoeing', 7, 0),
(23, '6', 'green', 5, 0),
(24, '6', 'boat', 7, 0),
(25, '7', 'waterfall', 4, 0),
(26, '7', 'tree', 8, 0),
(27, '7', 'lake', 6, 0),
(28, '8', 'waterfall', 8, 0),
(29, '8', 'mountain', 5, 0),
(30, '8', 'man', 15, 3),
(31, '8', 'person', 9, 0),
(32, '8', 'red', 6, 0),
(33, '9', 'superman', 14, 3),
(34, '9', 'water', 8, 0),
(35, '9', 'city', 6, 0),
(36, '9', 'building', 9, 0),
(37, '9', 'lake', 6, 0),
(38, '10', 'superman', 9, 2),
(39, '10', 'landscape', 7, 0),
(40, '10', 'face', 6, 0),
(41, '10', 'rushmore', 9, 0),
(42, '10', 'mountain', 5, 0),
(43, '10', 'america', 7, 0),
(44, '11', 'cat', 6, 0),
(45, '11', 'animal', 1, 0),
(46, '11', 'grey', 5, 0),
(47, '12', 'animal', 4, 0),
(48, '12', 'dog', 5, 0),
(49, '12', 'white', 8, 0),
(50, '13', 'animal', 4, 0),
(51, '13', 'sea', 5, 0),
(52, '13', 'dolphin', 4, 0),
(53, '14', 'animal', 4, 0),
(54, '14', 'sea', 5, 0),
(55, '14', 'whale', 4, 0),
(56, '15', 'building', 4, 0),
(57, '15', 'sky', 8, 0),
(58, '15', 'scenery', 9, 0),
(59, '16', 'building', 8, 0),
(60, '16', 'night', 8, 0),
(61, '16', 'light', 3, 0),
(62, '17', 'book', 8, 0),
(63, '17', 'dictonsry', 0, 0),
(64, '17', 'dictionary', 5, 0),
(65, '17', 'red', 1, 0),
(66, '18', 'book', 4, 0),
(67, '18', 'magazine', 4, 0),
(68, '18', 'magazine', 5, 0),
(69, '18', 'man', 4, 1),
(70, '19', 'phone', 8, 0),
(71, '19', 'iPhone', 8, 0),
(72, '20', 'phone', 3, 0),
(73, '20', 'red', 4, 0),
(74, '20', 'nokia', 3, 0),
(75, '21', 'bag', 5, 0),
(76, '21', 'gucci', 8, 0),
(77, '21', 'white', 8, 0),
(78, '22', 'bag', 5, 0),
(79, '22', 'starbuck', 8, 0),
(80, '22', 'paper', 8, 0),
(81, '23', 'bag', 8, 0),
(82, '23', 'paper', 8, 0),
(83, '23', 'muji', 6, 0),
(84, '24', 'cup', 4, 0),
(85, '24', 'starbuck', 8, 0),
(86, '24', 'white', 4, 0),
(87, '25', 'cup', 4, 0),
(88, '25', 'white', 3, 0),
(89, '26', 'cup', 7, 0),
(90, '26', 'glass', 9, 0),
(91, '27', 'glass', 8, 0),
(92, '27', 'church', 3, 0),
(93, '27', 'building', 3, 0),
(94, '28', 'building', 3, 0),
(95, '28', 'glass', 3, 0),
(96, '29', 'scenery', 6, 0),
(97, '29', 'sky', 7, 0),
(98, '29', 'water', 9, 0),
(99, '30', 'scenery', 6, 0),
(100, '30', 'sea', 4, 0),
(101, '30', 'sky', 8, 0),
(102, '31', 'scenery', 8, 0),
(103, '31', 'tree', 12, 0),
(104, '31', 'sky', 7, 0),
(105, '32', 'yellow', 9, 0),
(106, '32', 'fruit', 7, 0),
(107, '32', 'banana', 9, 0),
(108, '33', 'apple', 8, 0),
(109, '33', 'red', 11, 0),
(110, '33', 'fruit', 5, 0),
(111, '34', 'lemon', 8, 0),
(112, '34', 'yellow', 9, 0),
(113, '34', 'fruit', 8, 0),
(114, '35', 'red', 8, 0),
(115, '35', 'flag', 9, 0),
(116, '35', 'china', 12, 0),
(117, '36', 'flag', 9, 0),
(118, '36', 'america', 9, 0),
(119, '36', 'red', 8, 0),
(120, '37', 'america', 9, 0),
(121, '37', 'man', 6, 0),
(122, '37', 'black', 9, 0),
(123, '38', 'america', 12, 0),
(124, '38', 'man', 8, 2),
(125, '38', 'white', 10, 0),
(126, '39', 'china', 5, 0),
(127, '39', 'man', 7, 1),
(128, '39', 'yellow', 9, 0),
(129, '40', 'scenery', 5, 0),
(130, '40', 'china', 9, 0),
(131, '40', 'beijing', 10, 0),
(132, '41', 'building', 9, 0),
(133, '41', 'china', 5, 0),
(134, '41', 'shanghai', 8, 0),
(135, '42', 'scenery', 9, 0),
(136, '42', 'america', 8, 0),
(137, '42', 'women', 6, 0),
(138, '43', 'tower', 7, 0),
(139, '43', 'scenery', 8, 0),
(140, '43', 'paris', 9, 0),
(141, '44', 'tower', 6, 0),
(142, '44', 'scenery', 7, 0),
(143, '44', 'macao', 8, 0),
(144, '45', 'bridge', 9, 0),
(145, '45', 'china', 6, 0),
(146, '45', 'sea', 7, 0),
(147, '46', 'bridge', 8, 0),
(148, '46', 'england', 7, 0),
(149, '46', 'water', 8, 0),
(150, '47', 'bridge', 9, 0),
(151, '47', 'scenery', 8, 0),
(152, '47', 'america', 7, 0),
(153, '48', 'building', 9, 0),
(154, '48', 'england', 15, 0),
(155, '48', 'water', 9, 0),
(156, '49', 'mountain', 9, 0),
(157, '49', 'japan', 8, 0),
(158, '49', 'scenery', 9, 0),
(159, '50', 'bridge', 5, 0),
(160, '50', 'building', 6, 0),
(161, '50', 'japan', 8, 0);

-- --------------------------------------------------------

--
-- 表的结构 `information`
--

CREATE TABLE `information` (
  `id` int(10) NOT NULL,
  `Image_FileName` varchar(500) NOT NULL,
  `Image_FilePath` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `information`
--

INSERT INTO `information` (`id`, `Image_FileName`, `Image_FilePath`) VALUES
(1, 'test1', '../image/ResultImage/test1.jpg'),
(2, 'test2', '../image/ResultImage/test2.jpg'),
(3, 'test3', '../image/ResultImage/test3.jpg'),
(4, 'test4', '../image/ResultImage/test4.jpg'),
(5, 'test5', '../image/ResultImage/test5.jpg'),
(6, 'test6', '../image/ResultImage/test6.jpg'),
(7, 'test7', '../image/ResultImage/test7.jpg'),
(8, 'test8', '../image/ResultImage/test8.jpg'),
(9, 'test9', '../image/ResultImage/test9.jpg'),
(10, 'test10', '../image/ResultImage/test10.jpg'),
(11, 'test11', '../image/ResultImage/test11.jpg'),
(12, 'test12', '../image/ResultImage/test12.jpg'),
(13, 'test13', '../image/ResultImage/test13.jpg'),
(14, 'test14', '../image/ResultImage/test14.jpg'),
(15, 'test15', '../image/ResultImage/test15.jpg'),
(16, 'test16', '../image/ResultImage/test16.jpg'),
(17, 'test17', '../image/ResultImage/test17.jpg'),
(18, 'test18', '../image/ResultImage/test18.jpg'),
(19, 'test19', '../image/ResultImage/test19.jpg'),
(20, 'test20', '../image/ResultImage/test20.jpg'),
(21, 'test21', '../image/ResultImage/test21.jpg'),
(22, 'test22', '../image/ResultImage/test22.jpg'),
(23, 'test23', '../image/ResultImage/test23.jpg'),
(24, 'test24', '../image/ResultImage/test24.jpg'),
(25, 'test25', '../image/ResultImage/test25.jpg'),
(26, 'test26', '../image/ResultImage/test26.jpg'),
(27, 'test27', '../image/ResultImage/test27.jpg'),
(28, 'test28', '../image/ResultImage/test28.jpg'),
(29, 'test29', '../image/ResultImage/test29.jpg'),
(30, 'test30', '../image/ResultImage/test30.jpg'),
(31, 'test31', '../image/ResultImage/test31.jpg'),
(32, 'test32', '../image/ResultImage/test32.jpg'),
(33, 'test33', '../image/ResultImage/test33.jpg'),
(34, 'test34', '../image/ResultImage/test34.jpg'),
(35, 'test35', '../image/ResultImage/test35.jpg'),
(36, 'test36', '../image/ResultImage/test36.jpg'),
(37, 'test37', '../image/ResultImage/test37.jpg'),
(38, 'test38', '../image/ResultImage/test38.jpg'),
(39, 'test39', '../image/ResultImage/test39.jpg'),
(40, 'test40', '../image/ResultImage/test40.jpg'),
(41, 'test41', '../image/ResultImage/test41.jpg'),
(42, 'test42', '../image/ResultImage/test42.jpg'),
(43, 'test43', '../image/ResultImage/test43.jpg'),
(44, 'test44', '../image/ResultImage/test44.jpg'),
(45, 'test45', '../image/ResultImage/test45.jpg'),
(46, 'test46', '../image/ResultImage/test46.jpg'),
(47, 'test47', '../image/ResultImage/test47.jpg'),
(48, 'test48', '../image/ResultImage/test48.jpg'),
(49, 'test49', '../image/ResultImage/test49.jpg'),
(50, 'test50', '../image/ResultImage/test50.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `indexing`
--
ALTER TABLE `indexing`
  ADD PRIMARY KEY (`Tag_ID`);

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `indexing`
--
ALTER TABLE `indexing`
  MODIFY `Tag_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=162;
--
-- 使用表AUTO_INCREMENT `information`
--
ALTER TABLE `information`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
