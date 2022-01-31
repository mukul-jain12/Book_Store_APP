DELIMITER $$
CREATE PROCEDURE get_ordered_details(IN sp_user_id INT, IN user_address VARCHAR(600))
BEGIN
	DECLARE total_cost INTEGER default 0;
	DECLARE sp_order_id INTEGER default 0;
	DECLARE fetch_book_id INTEGER default 0;
    DECLARE fetch_quantity INTEGER default 0;
    DECLARE books_quantity INTEGER default 0;
    DECLARE flag INTEGER DEFAULT 0;
    DECLARE cart_list_cursor CURSOR FOR SELECT book_id, quantity FROM cart WHERE user_id = sp_user_id;
	
    DECLARE CONTINUE HANDLER for NOT FOUND SET flag = 1;

    SELECT sum(price*cart.quantity) INTO total_cost FROM cart INNER JOIN books ON books.id = cart.book_id WHERE user_id = sp_user_id;
    
    INSERT INTO order_details(user_id, total_price, address, order_date) VALUES(sp_user_id, total_cost, user_address, current_timestamp());

	SELECT id INTO sp_order_id FROM order_details WHERE user_id = sp_user_id AND is_ordered = 0;
    
    OPEN cart_list_cursor;
		retrieve_bookid_and_quantity_list : LOOP
			FETCH cart_list_cursor INTO fetch_book_id, fetch_quantity;
			IF flag =1
				THEN LEAVE retrieve_bookid_and_quantity_list;
			END IF;
			
            SELECT quantity into books_quantity from books where id = fetch_book_id;
			IF fetch_quantity <= books_quantity 
			THEN
				INSERT INTO order_item(user_id, book_id, order_id, quantity) VALUES(sp_user_id, fetch_book_id, sp_order_id, fetch_quantity);
			ELSE 
				SIGNAL SQLSTATE '45000' SET message_text='selected quantity not available at stock';
			END IF;
		END LOOP retrieve_bookid_and_quantity_list;
	CLOSE cart_list_cursor;
    
	UPDATE books INNER JOIN cart ON books.id = cart.book_id SET books.quantity = (books.quantity - cart.quantity) WHERE user_id = sp_user_id;

 	DELETE FROM cart WHERE user_id = sp_user_id;
    
	UPDATE order_details SET is_ordered = 1 WHERE user_id = sp_user_id;
END$$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE place_order(IN sp_user_id INT, IN user_address VARCHAR(600))
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT "Trasaction Error: Rollback"
        ROLLBACK;
    END;
	
    START TRANSACTION;
		CALL get_ordered_details(sp_user_id, user_address);
    COMMIT;
    SELECT * FROM order_details WHERE user_id=sp_user_id;
END$$
DELIMITER ;

drop procedure get_ordered_details;
drop procedure place_order;
call place_order(3, "Dungarpur");