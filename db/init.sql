CREATE TABLE IF NOT EXISTS book (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    description TEXT,
    rating DECIMAL,
    date_published TIMESTAMP WITH TIME ZONE
);

INSERT INTO book(id, title, author, genre, description, rating, date_published) VALUES('75d78c06-f134-4d9c-b1ae-c3e28d312faa', 'Harry Potter', 'JK Rowling', 'fantasy', 'Kid goes to magic school', 9.2, '2004-10-19 10:23:54+02');
INSERT INTO book(id, title, author, genre, description, rating, date_published) VALUES('1561d744-0124-4dbd-b43a-e37bca283c55', 'Percy Jackson', 'Rick Riordan', 'fantasy', 'Kid goes to magic camp', 9.0, '2010-10-19 11:23:54+02');
INSERT INTO book(id, title, author, genre, description, rating, date_published) VALUES('12e78d1b-f003-4d9f-a71c-1e66b3ed660a', 'Twilight', 'Stephanie Meyer', 'fantasy', 'Girls falls in love with vampire', 6.0, '2004-10-19 10:23:54+02');
INSERT INTO book(id, title, author, genre, description, rating, date_published) VALUES('027be1fa-eaaf-4a25-aa45-dc37a7fd9079', 'Star Wars', 'George Lucas', 'sci-fi', 'Kid goes on space adventure', 8, '2004-10-19 10:23:54+02');