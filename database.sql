CREATE TABLE `articles` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `pm_id` text,
  `pm_link` text,
  `date_pub` text,
  `journal_id` int,
  `title` longtext NOT NULL,
  `abstract` longtext NOT NULL,
  `n_participants` int
);

CREATE TABLE `meshes_connect` (
  `article_id` INT,
  `mesh_id` INT
);

CREATE TABLE `study_design_connect` (
  `article_id` INT,
  `study_design_id` INT
);

CREATE TABLE `geography_connect` (
  `article_id` INT,
  `region_id` INT
);

CREATE TABLE `data_type_connect` (
  `article_id` INT,
  `data_type_id` INT
);

CREATE TABLE `vocabs_connect` (
  `article_id` INT,
  `vocab_id` INT
);

CREATE TABLE `authors_connect` (
  `article_id` INT,
  `author_id` INT
);

CREATE TABLE `mesh` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `mesh` text NOT NULL,
  `concept_id` text,
  `domain` text,
  `category_name` text
);

CREATE TABLE `study_design` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `study_design` text
);

CREATE TABLE `data_type` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `data_type` text
);

CREATE TABLE `geography` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `country` text,
  `region` text,
  `city` text
);

CREATE TABLE `journals` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `journal` text,
  `journal_country` text,
  `ranking` text
);

CREATE TABLE `vocabularies` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `omop_vocab` text
);

CREATE TABLE `authors` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `author` text,
  `author_ranking` text
);
