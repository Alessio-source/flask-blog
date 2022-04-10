-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Apr 10, 2022 alle 21:22
-- Versione del server: 10.4.18-MariaDB
-- Versione PHP: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('5eacd17e5903');

-- --------------------------------------------------------

--
-- Struttura della tabella `comment`
--

CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `comment`
--

INSERT INTO `comment` (`id`, `author_id`, `post_id`, `content`, `created_at`, `updated_at`) VALUES
(1, 1, 2, 'Test', '2022-04-09 17:08:37', NULL);

-- --------------------------------------------------------

--
-- Struttura della tabella `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `title` varchar(150) NOT NULL,
  `subtitle` varchar(350) DEFAULT NULL,
  `content` text NOT NULL,
  `card_cover` varchar(250) DEFAULT NULL,
  `image` varchar(250) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `slug` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `post`
--

INSERT INTO `post` (`id`, `author_id`, `title`, `subtitle`, `content`, `card_cover`, `image`, `created_at`, `updated_at`, `slug`) VALUES
(2, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit ornare sodales. Aliquam placerat facilisis risus, vel aliquam lorem condimentum in. Sed tristique vitae magna id vestibulum. Praesent in nibh ut sapien euismod euismod ut et turpis. Praesent fringilla libero sed nisl pretium consectetur. Sed pulvinar magna id felis pellentesque lobortis. Quisque et varius est, eu dignissim est. Duis egestas in risus sit amet ornare. Praesent viverra tortor lorem, sed auctor diam ullamcorper eu. Praesent eget est non justo vulputate varius vitae ac nisl. Suspendisse consectetur aliquet quam, et pretium odio eleifend ut. Suspendisse sit amet libero ante.\r\n\r\nProin nulla dolor, finibus vitae sollicitudin eget, elementum nec tortor. In felis massa, euismod et euismod eget, fringilla ut elit. Etiam nulla dolor, dignissim in lacinia sed, fermentum nec magna. In erat dui, facilisis ac viverra non, auctor sed nisi. Aliquam imperdiet sit amet diam ut gravida. Sed auctor nisi luctus leo suscipit, ut mattis eros vulputate. Ut nisi nulla, maximus nec mi sit amet, scelerisque sodales nibh. Quisque venenatis ultrices maximus.\r\n\r\nIn sit amet eleifend nisi. Mauris et tristique erat, in vulputate neque. Suspendisse euismod, erat ut semper accumsan, magna purus tempus arcu, quis feugiat metus velit quis felis. Duis vulputate eget nisl id accumsan. Mauris et pretium nunc. Suspendisse enim neque, fringilla nec blandit vitae, bibendum quis ligula. Curabitur posuere scelerisque finibus. Nullam id pulvinar erat, sit amet fringilla lectus. Praesent mauris metus, sodales id lobortis in, tempor at dolor. Praesent lobortis nisi sit amet lorem vestibulum, quis tincidunt odio dignissim. Nulla at porta purus, nec euismod massa. Vivamus nunc ante, imperdiet hendrerit sem id, efficitur porttitor erat. Aliquam eu condimentum quam, in sodales nunc.\r\n\r\nAliquam nunc augue, auctor quis dictum id, porta id justo. Pellentesque sollicitudin commodo risus non ullamcorper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec mattis nulla et nulla cursus cursus. Fusce elementum molestie mauris non posuere. Donec laoreet velit mauris, sed auctor ex maximus vel. Etiam pharetra enim vel ex hendrerit tincidunt. Quisque at neque sit amet ex vehicula blandit eu et nulla. Sed pharetra fringilla sapien, sed condimentum ipsum efficitur eleifend. Integer egestas, nisl sit amet aliquet dapibus, eros diam fringilla turpis, ac pulvinar nibh quam sit amet odio. Nullam sodales tellus et turpis sollicitudin, a sodales tortor placerat. Phasellus et bibendum mi.\r\n\r\nAliquam et enim sit amet ante hendrerit fermentum in a eros. Integer ac dignissim lectus. Duis nec velit eu nibh convallis rutrum eget a metus. Morbi molestie leo vitae enim condimentum sodales. Morbi sodales cursus tellus, at vulputate metus euismod sed. Integer orci mauris, auctor ut tempus finibus, consequat sit amet sapien. Duis porttitor lacinia nisl posuere tristique. Pellentesque ut posuere nibh. Nunc augue tellus, congue ac tellus nec, volutpat tempor urna.', 'sgcwkxlhtf4c4pbt-iphone.png', 'inz4hhyap0ij2xwo-background-iphone.jpg', '2022-04-08 19:37:51', NULL, 'primo-post-w9x49klxp6aw4f6b'),
(3, 1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit ornare sodales. Aliquam placerat facilisis risus, vel aliquam lorem condimentum in. Sed tristique vitae magna id vestibulum. Praesent in nibh ut sapien euismod euismod ut et turpis. Praesent fringilla libero sed nisl pretium consectetur. Sed pulvinar magna id felis pellentesque lobortis. Quisque et varius est, eu dignissim est. Duis egestas in risus sit amet ornare. Praesent viverra tortor lorem, sed auctor diam ullamcorper eu. Praesent eget est non justo vulputate varius vitae ac nisl. Suspendisse consectetur aliquet quam, et pretium odio eleifend ut. Suspendisse sit amet libero ante.\r\n\r\nProin nulla dolor, finibus vitae sollicitudin eget, elementum nec tortor. In felis massa, euismod et euismod eget, fringilla ut elit. Etiam nulla dolor, dignissim in lacinia sed, fermentum nec magna. In erat dui, facilisis ac viverra non, auctor sed nisi. Aliquam imperdiet sit amet diam ut gravida. Sed auctor nisi luctus leo suscipit, ut mattis eros vulputate. Ut nisi nulla, maximus nec mi sit amet, scelerisque sodales nibh. Quisque venenatis ultrices maximus.\r\n\r\nIn sit amet eleifend nisi. Mauris et tristique erat, in vulputate neque. Suspendisse euismod, erat ut semper accumsan, magna purus tempus arcu, quis feugiat metus velit quis felis. Duis vulputate eget nisl id accumsan. Mauris et pretium nunc. Suspendisse enim neque, fringilla nec blandit vitae, bibendum quis ligula. Curabitur posuere scelerisque finibus. Nullam id pulvinar erat, sit amet fringilla lectus. Praesent mauris metus, sodales id lobortis in, tempor at dolor. Praesent lobortis nisi sit amet lorem vestibulum, quis tincidunt odio dignissim. Nulla at porta purus, nec euismod massa. Vivamus nunc ante, imperdiet hendrerit sem id, efficitur porttitor erat. Aliquam eu condimentum quam, in sodales nunc.\r\n\r\nAliquam nunc augue, auctor quis dictum id, porta id justo. Pellentesque sollicitudin commodo risus non ullamcorper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec mattis nulla et nulla cursus cursus. Fusce elementum molestie mauris non posuere. Donec laoreet velit mauris, sed auctor ex maximus vel. Etiam pharetra enim vel ex hendrerit tincidunt. Quisque at neque sit amet ex vehicula blandit eu et nulla. Sed pharetra fringilla sapien, sed condimentum ipsum efficitur eleifend. Integer egestas, nisl sit amet aliquet dapibus, eros diam fringilla turpis, ac pulvinar nibh quam sit amet odio. Nullam sodales tellus et turpis sollicitudin, a sodales tortor placerat. Phasellus et bibendum mi.\r\n\r\nAliquam et enim sit amet ante hendrerit fermentum in a eros. Integer ac dignissim lectus. Duis nec velit eu nibh convallis rutrum eget a metus. Morbi molestie leo vitae enim condimentum sodales. Morbi sodales cursus tellus, at vulputate metus euismod sed. Integer orci mauris, auctor ut tempus finibus, consequat sit amet sapien. Duis porttitor lacinia nisl posuere tristique. Pellentesque ut posuere nibh. Nunc augue tellus, congue ac tellus nec, volutpat tempor urna.', 'dz1m6byfjigts522-MacBook.png', '66xya5cj7h89wnar-macbook-air.jpg', '2022-04-09 18:31:41', NULL, 'lorem-ipsum-xubluct63whw3oz0');

-- --------------------------------------------------------

--
-- Struttura della tabella `role`
--

CREATE TABLE `role` (
  `id` int(11) NOT NULL,
  `role_name` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `role`
--

INSERT INTO `role` (`id`, `role_name`, `created_at`, `updated_at`) VALUES
(1, 'user', '2022-04-07 11:43:33', '2022-04-07 11:43:33'),
(2, 'amministratore', '2022-04-07 11:44:15', '2022-04-07 11:44:15'),
(3, 'editor', '2022-04-07 14:06:54', '2022-04-07 14:06:54');

-- --------------------------------------------------------

--
-- Struttura della tabella `setting`
--

CREATE TABLE `setting` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `value_setting` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `setting`
--

INSERT INTO `setting` (`id`, `name`, `value_setting`) VALUES
(1, 'blog_name', 'Blog'),
(2, 'blog_motto', 'Motto lungo del blog'),
(3, 'blog_title_homepage', 'Titolo'),
(4, 'blog_subtitle_homepage', 'Est fringilla quis proin vehicula accumsan venenatis, tincidunt ornare sollicitudin semper ornare aenean, tincidunt habitasse quam. Faucibus primis cum etiam ultricies, placerat erat taciti cubilia duis, elit posuere malesuada nascetur hendrerit, hac euismod amet lorem, magnis lorem.');

-- --------------------------------------------------------

--
-- Struttura della tabella `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`, `role_id`, `created_at`, `updated_at`) VALUES
(1, 'test', 'test@test.com', 'pbkdf2:sha256:260000$my48s0iktrZVwivA$2806fe070483a3cc671ca32fdcf514909351889b767b4d1e2f12565c19b133be', 2, '2022-04-07 11:50:44', '2022-04-07 11:50:44');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indici per le tabelle `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author_id` (`author_id`),
  ADD KEY `post_id` (`post_id`);

--
-- Indici per le tabelle `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author_id` (`author_id`);

--
-- Indici per le tabelle `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `role_name` (`role_name`);

--
-- Indici per le tabelle `setting`
--
ALTER TABLE `setting`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `comment`
--
ALTER TABLE `comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT per la tabella `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT per la tabella `role`
--
ALTER TABLE `role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT per la tabella `setting`
--
ALTER TABLE `setting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT per la tabella `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`);

--
-- Limiti per la tabella `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`);

--
-- Limiti per la tabella `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
