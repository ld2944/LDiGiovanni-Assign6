PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage)
VALUES 
    (1, 'Music Biographies', 'music.jpg'),
    (2, 'Movie and TV Biographies', 'films.jpg'),
    (3, 'Sports Biographies', 'sports.jpg'),
    (4,'Historical Figure Biographies', 'history.jpg');

INSERT INTO book(bookId, categoryId, title, author, isbn, price, image, readNow)
VALUES
    (1, 1, 'Cher: Part One: The Memoir', 'Cher', 9780062863119, 21.99, 'cher.jpg', 1),
    (2,1, 'Moonwalk: A Memoir', 'Michael Jackson', 9780307716989, 32.99, 'mj.jpg', 1),
    (3, 1, 'The Woman in Me', ' Britney Spears', 9781668009055, 20.00, 'britney.jpg', 0),
    (4,1, 'Be My Baby: A Memoir', 'Ronnie Spector', 9781250837189, 19.99, 'ronnieSpector.jpg', 0),
    (5,2, 'My Name is Barbara', 'Barbara Streisand', 9780525429524, 47.00, 'barbara.jpg', 0),
    (6,2, 'Greenlights', 'Matthew McConaughey', 9780593139158, 20.00,'matthew.Mc.jpg', 1),
    (7,2, 'Unrequited Infatuations: A Memoir', 'Stevie Van Zandt', 9780306925429, 31.00, 'vanZandt.jpg', 0),
    (8,2, 'Softly, As I Leave You: Life After Elvis', 'Priscilla Presley', 9781538778722, 27.99, 'priscilla.jpg', 1),
    (9, 3, 'All In: An Autobiography', 'Billy Jean King',9781101971475, 21.00, 'billyJeanKing.jpg', 0),
    (10, 3, 'The Closer', 'Mariano Rivera', 9780316400749, 19.99, 'mariano.jpg', 1),
    (11, 3, 'Undisputed Truth', 'Mike Tyson', 9780399161285, 22.99, 'tyson.jpg', 0),
    (12, 3, 'Through My Eyes', 'Tim Tebow', 9780062007285, 24.00, 'tebow.jpg', 0),
    (13, 4,'Up from Slavery: An Autobiography', 'Booker T. Washington', 9781454949992, 9.99, 'bookerT.jpg', 1),
    (14, 4, 'Autobiographies', 'Charles Dawrin', 9780140433906, 15.00, 'darwin.jpg', 0),
    (15, 4, 'Autobiography and Other Writings', 'Benjamin Franklin', 9780199554904, 9.95, 'franklin.jpg', 1),
    (16, 4, 'Life: My Story through History', 'Pope Francis', 9780063387522, 19.95, 'pope.jpg', 1)



