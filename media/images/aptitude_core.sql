-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:4306
-- Generation Time: Mar 06, 2022 at 01:22 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aptitude_core`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_candidates`
--

CREATE TABLE `app_candidates` (
  `id` bigint(20) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `contact_no` varchar(100) NOT NULL,
  `address1` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `reference` varchar(100) NOT NULL,
  `qualifications` varchar(100) NOT NULL,
  `university` varchar(200) NOT NULL,
  `passout_year` varchar(100) NOT NULL,
  `cgpa` varchar(100) DEFAULT NULL,
  `backlogs` varchar(20) NOT NULL,
  `percentage` varchar(100) DEFAULT NULL,
  `graduation_certificate` varchar(100) NOT NULL,
  `highschool_percentage` varchar(100) NOT NULL,
  `highschool_certificate` varchar(100) NOT NULL,
  `highersecondary_percentage` varchar(100) NOT NULL,
  `highersecondary_certificate` varchar(100) NOT NULL,
  `exam_status` varchar(20) NOT NULL,
  `dob` date DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_candidates`
--

INSERT INTO `app_candidates` (`id`, `firstname`, `lastname`, `email`, `password`, `username`, `contact_no`, `address1`, `district`, `state`, `reference`, `qualifications`, `university`, `passout_year`, `cgpa`, `backlogs`, `percentage`, `graduation_certificate`, `highschool_percentage`, `highschool_certificate`, `highersecondary_percentage`, `highersecondary_certificate`, `exam_status`, `dob`, `mark`, `image`) VALUES
(1, 'Leya', 'Kunjumon', 'leyakunjumon99@gmail.com', 'Leya3736', 'LeyaKunjumon', '98989777777', 'Thadathivila Veedu', 'Kollam', 'Kerala', 'Anoop', 'Btech', 'KTU', '2020', '7.35', 'no', '70%', 'images/Capture_IfbkdXd.PNG', '80%', 'images/Capture_wjF6tJw.PNG', '83%', 'images/Capture_1JCVsnT.PNG', '1', '2018-03-26', 10, 'images/Capture.PNG'),
(2, 'Sanisha', 'Santhosh', 'sanishasanthosh01@gmail.com', 'Sanisha2730', 'SanishaSanthosh', '8989767777', 'kikijuhghhhh', 'Palakkad', 'Kerala', 'no reference', 'Diploma', 'Profesional', '2021', '8.30', 'no', '80%', 'images/Capture_sgCGQlb.PNG', '90%', 'images/Capture_xUnF1Ee.PNG', '90%', 'images/Capture_oOTElHZ.PNG', '1', '2001-02-22', 10, 'images/Capture_phmJkiq.PNG'),
(4, 'Kripa', 'Mariyam', 'leyakunjumon@gmail.com', 'Kripa9485', 'KripaMariyam', '89876778888', 'juhtgggg', 'Alappuzha', 'Kerala', 'Arun', 'Btech', 'KTU', '2021', '8.45', 'NO', '80%', 'images/Capture_bqdgqjr_6a45IGu.PNG', '90%', 'images/Screenshot_717_vsedpNN.png', '90%', 'images/Screenshot_717_EBuTdUt.png', '0', '1998-05-14', 50, 'images/face15_vr3hQDz.jpg'),
(5, 'Kripa', 'Mariyam', 'leyakunjumon@gmail.com', 'Kripa6088', 'KripaMariyam', '89876778888', 'juhtgggg', 'Alappuzha', 'Kerala', 'Anoop', 'Btech', 'KTU', '2021', '8.45', 'NO', '80%', 'images/Capture_bqdgqjr_O4sKanW.PNG', '90%', 'images/Screenshot_717_BiOEWzb.png', '90%', 'images/Screenshot_717_VBUWAZC.png', '0', '1998-05-14', 40, 'images/face15_mXVy4MV.jpg'),
(6, 'Kripa', 'Mariyam', 'leyakunjumon@gmail.com', 'Kripa3494', 'KripaMariyam', '89876778888', 'juhtgggg', 'Alappuzha', 'Kerala', 'Anoop', 'Btech', 'KTU', '2021', '8.45', 'NO', '80%', 'images/Capture_bqdgqjr_C7xnLiY.PNG', '90%', 'images/Screenshot_717_emxrdRC.png', '90%', 'images/Screenshot_717_pYzgJ33.png', '0', '1998-05-14', 30, 'images/face15_M27oc5J.jpg'),
(12, 'Ammu', 'Joe', 'leyakunjumon99@gmail.com', 'Ammu3654', 'AmmuJoe', '8787666666', 'Thadathivila Veedu', 'Kollam', 'Kerala', 'Anoop', 'Btech', 'KTU', '2020', '9.78', 'NO', '90%', 'images/Screenshot_717_r8cg46n.png', '90%', 'images/Capture_IfbkdXd_E27WlQP.PNG', '90%', 'images/Capture_IfbkdXd_7chmlcr.PNG', '0', '2022-03-03', 20, 'images/face15_lqzfGBA.jpg'),
(13, 'Ammu', 'Joe', 'leyakunjumon99@gmail.com', 'Ammu635', 'AmmuJoe', '8787666666', 'Thadathivila Veedu', 'Kollam', 'Kerala', 'Arun', 'Btech', 'KTU', '2020', '9.78', 'NO', '90%', 'images/Screenshot_717_eJnJA6V.png', '90%', 'images/Capture_IfbkdXd_Eio9FOI.PNG', '90%', 'images/Capture_IfbkdXd_aNGnHNr.PNG', '1', '2022-03-03', 10, 'images/face15_PpF17rj.jpg'),
(22, 'bbbbbbb', 'nnnnnnnnnn', 'leyakunjumon99@gmail.com', 'bbbbbbb1172', 'bbbbbbbnnnnnnnnnn', '8989999999999', 'Thadathivila Veedu', 'klm', 'Kerala', 'Arun', 'btech', 'ktu', '2020', '8', 'no', '80', 'images/Screenshot_717_EBuTdUt_maCOKet.png', '90', 'images/Capture_IfbkdXd_BMQiy95.PNG', '90', 'images/Capture_IfbkdXd_ib5ZP3v.PNG', '0', '2022-03-01', NULL, 'images/Screenshot_717_EBuTdUt_1_VUOCfw2.png'),
(27, 'bhbh', 'bhyu', 'leyakunjumon99@gmail.com', 'bhbh6691', 'bhbhbhyu', '7878788989', 'Thadathivila Veedu', 'klm', 'Kerala', 'no reference', 'btch', 'ku', '2016', '8', 'no', '80', 'images/Screenshot_717_EBuTdUt_tyVQSTz.png', '80', 'images/Capture_IfbkdXd_g6hBVHs.PNG', '80', 'images/Capture_IfbkdXd_uidwTRW.PNG', '0', '2022-03-01', NULL, 'images/Screenshot_717_EBuTdUt_pxAPheV.png'),
(28, 'vghj', 'ujhik', 'leyakunjumon99@gmail.com', 'vghj1914', 'vghjujhik', '786799000', 'Thadathivila Veedu', 'klm', 'Kerala', 'Anoop', 'btch', 'ku', '2017', '8', 'no', '80', 'images/Screenshot_717_EBuTdUt_42JtLs4.png', '80', 'images/Screenshot_717_EBuTdUt_XQMqd1Q.png', '80', 'images/Screenshot_717_EBuTdUt_Ybm3npg.png', '1', '2022-03-01', 10, 'images/Capture_IfbkdXd_ZTG0D4g.PNG');

-- --------------------------------------------------------

--
-- Table structure for table `app_designation`
--

CREATE TABLE `app_designation` (
  `id` bigint(20) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_designation`
--

INSERT INTO `app_designation` (`id`, `designation`) VALUES
(1, 'ADMIN'),
(2, 'HR');

-- --------------------------------------------------------

--
-- Table structure for table `app_login`
--

CREATE TABLE `app_login` (
  `id` bigint(20) NOT NULL,
  `fullname` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `designation_id` bigint(20) DEFAULT NULL,
  `contact_no` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_login`
--

INSERT INTO `app_login` (`id`, `fullname`, `password`, `image`, `designation_id`, `contact_no`, `email`) VALUES
(1, 'Anoop', '1234', 'face12.jpg', 1, '987867888', 'anoop@gmail.com'),
(2, 'Arun', '1234', 'face14.jpg', 2, '8987678888', 'arun@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `app_question`
--

CREATE TABLE `app_question` (
  `id` bigint(20) NOT NULL,
  `questions` varchar(200) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `correct_option` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app_question`
--

INSERT INTO `app_question` (`id`, `questions`, `option1`, `option2`, `option3`, `option4`, `correct_option`) VALUES
(1, 'What the does random.seed(3) return?', 'True   ', 'None', '3', '1', 'None'),
(2, 'Which type of elements are accepted by random.shuffle()?', 'strings ', 'lists ', 'tuples ', ' integers ', 'lists'),
(3, 'What is the range of values that random.random() can return?', '[0.0, 1.0]   ', '(0.0, 1.0]', '(0.0, 1.0)  ', '[0.0, 1.0) ', '[0.0, 1.0)'),
(4, 'Which of the following is equivalent to random.randrange(3)?', 'range(3)', 'random.choice(range(0, 3)) ', ' random.shuffle(range(3)) ', 'random.select(range(3)) ', 'random.choice(range(0, 3))'),
(5, 'The function random.randint(4) can return only one of the following values. Which?', '4   ', '3.4', 'error ', '5', 'error'),
(6, 'Which of the following will not be returned by random.choice(“1 ,”)?', ' 1  ', '(space) ', ',', 'none of the mentioned', ' none of the mentioned');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add candidates', 7, 'add_candidates'),
(26, 'Can change candidates', 7, 'change_candidates'),
(27, 'Can delete candidates', 7, 'delete_candidates'),
(28, 'Can view candidates', 7, 'view_candidates'),
(29, 'Can add designation', 8, 'add_designation'),
(30, 'Can change designation', 8, 'change_designation'),
(31, 'Can delete designation', 8, 'delete_designation'),
(32, 'Can view designation', 8, 'view_designation'),
(33, 'Can add question', 9, 'add_question'),
(34, 'Can change question', 9, 'change_question'),
(35, 'Can delete question', 9, 'delete_question'),
(36, 'Can view question', 9, 'view_question'),
(37, 'Can add login', 10, 'add_login'),
(38, 'Can change login', 10, 'change_login'),
(39, 'Can delete login', 10, 'delete_login'),
(40, 'Can view login', 10, 'view_login');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$6srDrisWt67UQMQ5vEhAnh$KmMGdy6dm3vTGxrddB1Md69UW+KFTU/H8jsWM0nMCdM=', NULL, 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2022-03-06 12:15:34.171620');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'app', 'candidates'),
(8, 'app', 'designation'),
(10, 'app', 'login'),
(9, 'app', 'question'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-03-06 05:40:16.256796'),
(2, 'auth', '0001_initial', '2022-03-06 05:40:24.801374'),
(3, 'admin', '0001_initial', '2022-03-06 05:40:26.776553'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-03-06 05:40:26.981679'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-03-06 05:40:27.101376'),
(6, 'app', '0001_initial', '2022-03-06 05:40:27.906774'),
(7, 'app', '0002_candidates_dob', '2022-03-06 05:40:28.306520'),
(8, 'app', '0003_designation_question_candidates_mark_and_more', '2022-03-06 05:40:30.836364'),
(9, 'app', '0004_alter_candidates_mark', '2022-03-06 05:40:31.536770'),
(10, 'app', '0005_candidates_image', '2022-03-06 05:40:31.727035'),
(11, 'app', '0006_alter_candidates_exam_status', '2022-03-06 05:40:31.771577'),
(12, 'contenttypes', '0002_remove_content_type_name', '2022-03-06 05:40:32.406349'),
(13, 'auth', '0002_alter_permission_name_max_length', '2022-03-06 05:40:33.231986'),
(14, 'auth', '0003_alter_user_email_max_length', '2022-03-06 05:40:33.386664'),
(15, 'auth', '0004_alter_user_username_opts', '2022-03-06 05:40:33.461677'),
(16, 'auth', '0005_alter_user_last_login_null', '2022-03-06 05:40:34.336572'),
(17, 'auth', '0006_require_contenttypes_0002', '2022-03-06 05:40:34.366638'),
(18, 'auth', '0007_alter_validators_add_error_messages', '2022-03-06 05:40:34.446444'),
(19, 'auth', '0008_alter_user_username_max_length', '2022-03-06 05:40:34.636661'),
(20, 'auth', '0009_alter_user_last_name_max_length', '2022-03-06 05:40:34.916809'),
(21, 'auth', '0010_alter_group_name_max_length', '2022-03-06 05:40:35.136484'),
(22, 'auth', '0011_update_proxy_permissions', '2022-03-06 05:40:35.286874'),
(23, 'auth', '0012_alter_user_first_name_max_length', '2022-03-06 05:40:35.992196'),
(24, 'sessions', '0001_initial', '2022-03-06 05:40:36.566661'),
(25, 'app', '0007_login_contact_no_login_email', '2022-03-06 06:18:36.178113');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('d2gs6qo6kjjnq3zy0l9u86ohyu7mkowh', '.eJyrViotTi3KS8xNzShSsjLSQeIaKlkpORaV5ikhBBNTlKwMEVyggrL0jKzSrIzMbCRVQI1GFgiuEVCZAYohYJPz8vMLlJDtM0KxPzEFyDesBQDqZjT6:1nQpij:BwbYfx9FqJoXOmKISPwbqch9tT3j9PQh_rJgLR5gprw', '2022-03-20 12:10:41.765663');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_candidates`
--
ALTER TABLE `app_candidates`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_designation`
--
ALTER TABLE `app_designation`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_login`
--
ALTER TABLE `app_login`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_login_designation_id_46a3e3d9_fk_app_designation_id` (`designation_id`);

--
-- Indexes for table `app_question`
--
ALTER TABLE `app_question`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_candidates`
--
ALTER TABLE `app_candidates`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `app_designation`
--
ALTER TABLE `app_designation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_login`
--
ALTER TABLE `app_login`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `app_question`
--
ALTER TABLE `app_question`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_login`
--
ALTER TABLE `app_login`
  ADD CONSTRAINT `app_login_designation_id_46a3e3d9_fk_app_designation_id` FOREIGN KEY (`designation_id`) REFERENCES `app_designation` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
