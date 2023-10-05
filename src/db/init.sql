/*Create Database*/
CREATE DATABASE IF NOT EXISTS TODO;

/*Create Task Table*/
CREATE TABLE `tasks` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `status` VARCHAR(100) NOT NULL,
    `dueDate` DATETIME,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


/*Enter some values*/
INSERT INTO tasks (name, description, status, dueDate) VALUES
  ('Task 1', 'This is the first task.', 'New', '2023-10-06 12:00:00'),
  ('Task 2', 'This is the second task.', 'In Progress', '2023-10-07 12:00:00'),
  ('Task 3', 'This is the third task.', 'Completed', '2023-10-05 12:00:00');
