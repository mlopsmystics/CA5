CREATE TABLE ToDo (
  ID INT NOT NULL PRIMARY KEY,
  Task VARCHAR(255) NOT NULL,
  TaskStatus VARCHAR(255) NOT NULL
);

INSERT INTO ToDo (ID, Task, TaskStatus)
VALUES (1, 'Learn Python', 'In Progress'),
       (2, 'Finish my homework', 'To Do'),
       (3, 'Go to the gym', 'Not Started');


SELECT * FROM ToDo;
```

