/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 100422
 Source Host           : localhost:3306
 Source Schema         : mydb

 Target Server Type    : MySQL
 Target Server Version : 100422
 File Encoding         : 65001

 Date: 28/06/2022 04:24:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for articles
-- ----------------------------
DROP TABLE IF EXISTS `articles`;
CREATE TABLE `articles`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `pm_id` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `pm_link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `date_pub` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `journal_id` int NULL DEFAULT NULL,
  `title` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `abstract` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `category_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `n_participant` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for authors
-- ----------------------------
DROP TABLE IF EXISTS `authors`;
CREATE TABLE `authors`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `author_ranking` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for authors_connect
-- ----------------------------
DROP TABLE IF EXISTS `authors_connect`;
CREATE TABLE `authors_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `author_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for data_type
-- ----------------------------
DROP TABLE IF EXISTS `data_type`;
CREATE TABLE `data_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `data_type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for data_type_connect
-- ----------------------------
DROP TABLE IF EXISTS `data_type_connect`;
CREATE TABLE `data_type_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `data_type_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for geography
-- ----------------------------
DROP TABLE IF EXISTS `geography`;
CREATE TABLE `geography`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `country` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `region` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `city` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for geography_connect
-- ----------------------------
DROP TABLE IF EXISTS `geography_connect`;
CREATE TABLE `geography_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `region_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for journals
-- ----------------------------
DROP TABLE IF EXISTS `journals`;
CREATE TABLE `journals`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `journal` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `journal_country` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `ranking` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for mesh
-- ----------------------------
DROP TABLE IF EXISTS `mesh`;
CREATE TABLE `mesh`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `mesh` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `concept_id` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `domain` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `category_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for meshes_connect
-- ----------------------------
DROP TABLE IF EXISTS `meshes_connect`;
CREATE TABLE `meshes_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `mesh_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for study_design
-- ----------------------------
DROP TABLE IF EXISTS `study_design`;
CREATE TABLE `study_design`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `study_design` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for study_design_connect
-- ----------------------------
DROP TABLE IF EXISTS `study_design_connect`;
CREATE TABLE `study_design_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `study_design_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for vocabs_connect
-- ----------------------------
DROP TABLE IF EXISTS `vocabs_connect`;
CREATE TABLE `vocabs_connect`  (
  `article_id` int NULL DEFAULT NULL,
  `vocab_id` int NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for vocabularies
-- ----------------------------
DROP TABLE IF EXISTS `vocabularies`;
CREATE TABLE `vocabularies`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `omop_vocab` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
