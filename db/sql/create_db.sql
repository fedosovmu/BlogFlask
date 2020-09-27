CREATE TABLE IF NOT EXISTS post (
    post_id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    short_description text,
    img_url text,
    publication_date text
);

CREATE TABLE IF NOT EXISTS comment (
    comment_id integer PRIMARY KEY AUTOINCREMENT,
    post_id integer,
    text text,
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);