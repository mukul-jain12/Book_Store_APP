CREATE DATABASE book_store_app;

USE book_store_app;

CREATE TABLE users(
	id INT AUTO_INCREMENT,
	user_name VARCHAR(100) NOT NULL ,
	email_id VARCHAR(100) NOT NULL UNIQUE,
	password VARCHAR(40) NOT NULL,
    mobile_number BIGINT NOT NULL,
    is_verified INT DEFAULT 0,
    PRIMARY KEY(id, email_id)
);


CREATE TABLE books(
	id INT AUTO_INCREMENT UNIQUE,
	author_name VARCHAR(100) NOT NULL,
	title VARCHAR(150) NOT NULL,
	image TEXT NOT NULL,
	quantity INT NOT NULL,
	price INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY(id)
);


CREATE TABLE cart(
	id INT AUTO_INCREMENT,
	user_id INT NOT NULL,
	book_id INT NOT NULL,
	quantity INT DEFAULT 1,
    KEY `FK_cart_user_id` (`user_id`), 
    CONSTRAINT `FK_cart_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
    KEY `FK_cart_book_id` (`book_id`), 
    CONSTRAINT `FK_cart_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
	PRIMARY KEY(id)
);


CREATE TABLE wishlist(
	id INT AUTO_INCREMENT,
	user_id INT NOT NULL,
	book_id INT NOT NULL,
    KEY `FK_wishlist_user_id` (`user_id`), 
    CONSTRAINT `FK_wishlist_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
    KEY `FK_wishlist_book_id` (`book_id`), 
    CONSTRAINT `FK_wishlist_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
	PRIMARY KEY(id)
);


CREATE TABLE order_details(
	id INT AUTO_INCREMENT,
	user_id INT NOT NULL,
    total_price INT NOT NULL,
    address VARCHAR(500) NOT NULL,
    order_date DATETIME NOT NULL,
    is_ordered INT DEFAULT 0,
    KEY `FK_order_book_user_id` (`user_id`), 
    CONSTRAINT `FK_order_book_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
	PRIMARY KEY(id)
);


CREATE TABLE order_item(
	id INT AUTO_INCREMENT,
	user_id INT NOT NULL,
    book_id INT NOT NULL,
    order_id INT NOT NULL,
    quantity INT NOT NULL,
    KEY `FK_user_id` (`user_id`), 
    CONSTRAINT `FK_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
	KEY `FK_book_id` (`book_id`),
    CONSTRAINT `FK_book_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
    KEY `FK_order_id` (`order_id`),
    CONSTRAINT `FK_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_details` (`id`),
	PRIMARY KEY(id)
);