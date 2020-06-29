CREATE TABLE IF NOT EXISTS users(
  user_id  INTEGER PRIMARY KEY,
  first_nm VARCHAR(50),
  last_nm  VARCHAR(50),
  user_nm  VARCHAR(50),
  known    BOOLEAN
);
