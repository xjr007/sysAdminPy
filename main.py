from feedbackdb import ConnectMySQL

class Main:
    """
    Main class.

    Main class for feedbackdb.
    """
    def __init__(self, db):
        self.db = db

    def start_connection(self):

        global conn

        try:
            conn = self.db.connect()

            print('Database connected...\n')

        except Exception as e:
            print(e)
        finally:
            return

    def view_databases(self):
        databases = []
        counter = 0

        try:
            c = conn.cursor()

            c.execute('SHOW DATABASES;')
            databases = c.fetchall()

            print('Databases\n---------')

            for db in databases:
                for schema in db:
                    counter += 1
                    print('{}: '.format(counter) + schema)

            return

        except Exception as e:
            print(e)
        finally:
            return

    def view_tables(self):
        tables = []
        counter = 0

        try:
            c = conn.cursor()

            c.execute('USE feedback;')

            c.execute('SHOW TABLES;')
            databases = c.fetchall()

            print('Tables\n------')

            for table in tables:
                counter += 1
                print('{}: '.format(counter) + table)

            return

        except Exception as e:
            print(e)
        finally:
            return


if __name__ == '__main__':
    establish_connection = Main(ConnectMySQL)
    establish_connection.start_connection()
    establish_connection.view_tables()
