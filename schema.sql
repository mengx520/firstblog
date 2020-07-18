CREATE TABLE IF NOT EXIST 'users'(
    'username' TEXT NOT NULL,
    'passwordhash' TEXT NOT NULL
);

CREATE TABLE IF NOT EXIST 'post'(
    'title' TEXT NOT NULL,
    'author' TEXT NOT NULL,
    'timecreated' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'body' TEXT NOT NULL
);