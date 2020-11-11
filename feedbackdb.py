import mysql.connector as mysql

class ConnectMySQL:
    def connect():
        """
        Connect MySQL database.

        Database connected...
        """

        try:
            db = mysql.connect(
                host='localhost',
                user='*****',
                passwd='*****'
                )

            print('Connected to MySQL database...')

            # Create table for database feedbackdb

            c = db.cursor()

            c.execute('CREATE DATABASE IF NOT EXISTS feedback;')

            c.execute('USE `feedback`;')

            c.execute('CREATE TABLE `users` (`id` AUTO_INCREMENT INT(10) NOT NULL, `employee_code` VARCHAR(50) DEFAULT NULL, `name` VARCHAR(30) DEFAULT NULL, `surname` VARCHAR(30) DEFAULT NULL, `email` VARCHAR(50) DEFAULT NULL, `contact_no` INT(10) DEFAULT NULL, `role` VARCHAR(30) DEFAULT NULL, UNIQUE KEY `employee_code` (`employee_code`, `email`), PRIMARY KEY(`id`));')

            c.commit()

        except Exception as e:
            print('Error thrown in feedbackdb, ' + e)
        finally:

            c.close()

            return db


if __name__ == '__main__':
    ConnectMySQL.connect()
