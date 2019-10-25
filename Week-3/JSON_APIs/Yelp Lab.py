import mysql.connector;
import config;

# connecting to the database

cnx = mysql.connector.connect(
        host = config.host,
        user = config.user,
        password = config.password
);

cursor = cnx.cursor();

db_hotel = "hotels";
db_review = "reviews";

TABLES = {}
TABLES["hotels"] = ("""
      CREATE TABLE hotels (
      hotel_id int(4) NOT NULL AUTO_INCREMENT,
      name varchar(100) NOT NULL,
      review_count int(4) NOT NULL,
      rating float(4) NOT NULL,
      price varchar(5)
      PRIMARY KEY (hotel_id)
      ) ENGINE = InnoDB
""");

TABLES["reviews"] = ("""
      CREATE TEABLE reviews (
      review_id int(4) NOT NULL AUTO_INCREMENT
      hotel_id int(4) NOT NULL AUTO_INCREMENT
      review_text varchar(500) NOT NULL
      FOREIGN KEY (hotel_id)
      ) ENGINE = InnoDB
""");