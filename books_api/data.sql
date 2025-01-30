begin transaction;
insert into
	publisher ("name")
values   
	('No Starch Press'),
	('O''Reilly Media'),
	('The MIT Press');

insert into 
	author ("full_name")
values
	('Eric Matthes'),
	('Al Sweigart'),
	('Luciano Ramalho'),
	('Wes McKinney'),
	('Thomas H. Cormen'),
	('Charles E. Leiserson'),
	('Ronald L. Rivest'),
	('Clifford Stein');

insert into
	book ("title", "isbn13", "pages", "overview", "publisher_id")
values
	('Python Crash Course','9781718502703',552,'Python Crash Course is the world’s best-selling guide to the Python programming language. This fast-paced, thorough introduction will have you writing programs, solving problems, and developing functioning applications in no time.',1),
	('Automate the Boring Stuff with Python','9781593279929',592,'Learn how to code while you write programs that effortlessly perform useful feats of automation!',1),
	('Fluent Python','9781492056355',1012,'Don''t waste time bending Python to fit patterns you''ve learned in other languages. Python''s simplicity lets you become productive quickly, but often this means you aren''t using everything the language has to offer. With the updated edition of this hands-on guide, you''ll learn how to write effective, modern Python 3 code by leveraging its best ideas.',2),
	('Python for Data Analysis','9781098104030',579,'Get the definitive handbook for manipulating, processing, cleaning, and crunching datasets in Python. Updated for Python 3.10 and pandas 1.4, the third edition of this hands-on guide is packed with practical case studies that show you how to solve a broad set of data analysis problems effectively. You''ll learn the latest versions of pandas, NumPy, and Jupyter in the process.',2),
	('Introduction to Algorithms','9780262046305',1312,'A comprehensive update of the leading algorithms text, with new material on matchings in bipartite graphs, online algorithms, machine learning, and other topics.',3);

insert into
	book_author ("book_id", "author_id")
values
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(5, 6),
	(5, 7),
	(5, 8);
commit transaction;