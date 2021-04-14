from flask_mysqldb import MySQL
from mysql.connector import MySQLConnection


class MySqlDb():
    def __init__(self, app, host, user, password, dbName="CoolScraperApp"):
        self.app = app
        self.host = host
        self.user = user
        self.password = password
        self.dbName = dbName
        self.secretKey = dbName

        # create db if doesnt exist - for local env
        self.createDatabase(self.dbName)

        self.db = self.makeConnection()

    def createDatabase(self, dbName):
        config = {
            'user': self.user,
            'password': self.password,
            'host': self.host
        }
        connection = MySQLConnection(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SHOW DATABASES;")
        databases = [i['Database'] for i in cursor.fetchall()]
        if not self.dbName in databases:
            cursor.execute(
                "CREATE DATABASE {} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;".format(self.dbName))
            config['database'] = self.dbName  # not necessary but just in case
            cursor.execute("CREATE TABLE `coolscraperapp`.`products` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(500) NOT NULL , `image` VARCHAR(500) NOT NULL , `price` FLOAT(20) NOT NULL , `price_symbol` VARCHAR(10) NOT NULL , `description` VARCHAR(500) NOT NULL , PRIMARY KEY (`id`)) CHARSET=utf8 COLLATE utf8_general_ci;")
        connection.commit()
        connection.close()

    def makeConnection(self):
        self.app.secret_key = self.secretKey
        self.app.config["MYSQL_HOST"] = self.host
        self.app.config["MYSQL_USER"] = self.user
        self.app.config["MYSQL_PASSWORD"] = self.password
        self.app.config["MYSQL_DB"] = self.dbName
        self.app.config["MYSQL_CURSORCLASS"] = 'DictCursor'
        return MySQL(self.app)

    def addProduct(self, name, image, price, price_symbol, description):
        query = "INSERT INTO products(name,image,price,price_symbol,description) values ('{}','{}','{}','{}','{}')".format(
            name, image, price, price_symbol, description)
        # sorguyu değiştir
        print(query)
        self.runQuery(query)

    def getProduct(self, product_id):
        query = "select * from products where id='{}'".format(product_id)
        return self.fetchOne(query)

    def getProducts(self):
        query = "select * from products order by id desc"
        return self.fetchAll(query)

    def runQuery(self, query):
        cursor = self.db.connection.cursor()
        cursor.execute(query)
        self.db.connection.commit()
        cursor.close()

    def fetchAll(self, query):
        cursor = self.db.connection.cursor()
        result = cursor.execute(query)
        if result > 0:
            return cursor.fetchall()
        return False

    def fetchOne(self, query):
        cursor = self.db.connection.cursor()
        result = cursor.execute(query)
        if result > 0:
            return cursor.fetchone()
        return False
