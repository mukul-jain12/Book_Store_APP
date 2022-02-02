"""
    @File :   user_service.py
    @Author : mukul
    @Date :   20-01-2022
"""
from core.db import DBConnection

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def retrieve_all_users():
    """
        desc: query to get all user detail from database
        return: employee detail in dictionary format
    """
    get_user_query = "SELECT * FROM users"
    cursor.execute(get_user_query)
    connection.commit()
    users = [i for i in cursor]
    if users:
        return users
    else:
        raise Exception("There is no result for the user data.")


def retrieve_user(user_id: int):
    """
        desc: query to get a user detail from database
        param: user id
        return: employee detail in dictionary format
    """
    show_data_query = f"SELECT * FROM users WHERE id={user_id}"
    cursor.execute(show_data_query)
    connection.commit()
    user = [i for i in cursor]
    if user:
        return user
    else:
        raise Exception("User with this Id doesn't exist in the Database!")


def register_user(users):
    """
        desc: query to insert employee details in database
        param: name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    show_data_query = "insert into users (user_name, email_id, password, mobile_number) values('%s', '%s', '%s', %d)" \
                      % (users.user_name, users.email_id, users.password, users.mobile_number)
    cursor.execute(show_data_query)
    connection.commit()
    return users


def retrieve_user_by_email_id(email_id: str):
    """
        desc: query to get a user detail from database
        param: user id
        return: employee detail in dictionary format
    """
    show_data_query = "SELECT * FROM users WHERE email_id = '%s'" % email_id
    cursor.execute(show_data_query)
    connection.commit()
    user = [i for i in cursor]
    if user:
        return user
    else:
        raise Exception("User with this Id doesn't exist in the Database!")


def verification(is_verified: int, email_id: str):
    if is_verified == 0:
        show_data_query = f"UPDATE users SET is_verified = 1 WHERE email_id='{email_id}'"
        cursor.execute(show_data_query)
        connection.commit()
        return "User Account Successfully Verified!!"
    else:
        raise Exception("User with this Id already verified!")


def login_into_book_store(email_id, password):
    """
        desc: query to get a user detail from database
        param: user id
        return: employee detail in dictionary format
    """
    show_data_query = f"SELECT * FROM users WHERE email_id = '{email_id}' and password = '{password}'"
    cursor.execute(show_data_query)
    connection.commit()
    user = [i for i in cursor]
    if user:
        return user
    else:
        raise Exception("Credentials Are incorrect, Please Try again!")


def delete_user(user_id):
    """
        desc: query to delete employee details from database
        param: id: user id, which you want to delete.
        return: user id which is deleted from db
    """
    show_data_query = f"delete from users where id = {user_id}"
    cursor.execute(show_data_query)
    connection.commit()
    return user_id


def update_user(user_id, users):
    """
        desc: query to update employee details in database
        param: id, name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    show_data_query = "UPDATE users SET user_name = '%s', email_id = '%s', password = '%s', mobile_number " \
                      "= %d WHERE id = %d" % (users.user_name, users.email_id, users.password, users.mobile_number,
                                              user_id)
    cursor.execute(show_data_query)
    connection.commit()
    user_data = retrieve_user(user_id)
    return user_data
