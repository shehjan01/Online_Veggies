import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myshop"
)
#cur= conn.cursor()
#cur.execute("CREATE DATABASE myshop")
#print("DataBase Createed")
# Establish a connection to the MySQL database

# conn.close()

# Create a cursor object
cursor = conn.cursor()
# sql=('''CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     price DECIMAL(10, 2) NOT NULL,
#     description TEXT,
#     image_url VARCHAR(255) NOT NULL)''')
# cursor.execute(sql)

#Sample product data
# products = [
#     {"name": "Best Okra(Bhindi)", "price": 90.00, "description": "Best Okra(Bhindi)", "image_url": "../vaggies/okra-bhindi.jpg"},
#     {"name": "Best Tomato", "price": 80.00, "description": "Best Tomato", "image_url": "../vaggies/Tomato.jpeg"},
#     {"name": "fenugreek (methi)", "price": 140.00, "description": "fenugreek (methi)", "image_url": "../vaggies/fenugreek.jpeg"},
#     {"name": "cluster beans(guar)", "price": 120.00, "description": "cluster beans(guar)", "image_url": "../vaggies/cluster-beans-(guar).jpg"},
#     {"name": "brinjal(bhatta)", "price": 60.00, "description": "brinjal(bhatta)", "image_url": "../vaggies/brinjal(bhatta).jpg"},
#     {"name": "kakdi", "price": 50.00, "description": "kakdi", "image_url": "../vaggies/kakdi.jpg"},
#     {"name": "best bitter Gourd(karela)", "price": 50.00, "description": "best bitter Gourd(karela)", "image_url": "../vaggies/bitter_Gourd(karela).jpeg"},
#     {"name": "bottle gourd(lauki)", "price": 40.00, "description": "bottle gourd(lauki)", "image_url": "../vaggies/bottle_gourd.jpeg"},
#     {"name": "peas", "price": 140.00, "description": "peas", "image_url": "../vaggies/peas.jpeg"},
#     {"name": "spinach(palak)", "price": 60.00, "description": "spinach(palak)", "image_url": "../vaggies/spinach(palak).jpg"},
#     {"name": "pigeon pea seeds(tuvar)", "price": 180.00, "description": "pigeon pea seeds(tuvar)", "image_url": "../vaggies/pigeon-pea-seeds(tuvar).webp"},
#     {"name": "cauliflower", "price": 80.00, "description": "cauliflower", "image_url": "../vaggies/cauliflower.jpg"},
#     {"name": "valor", "price": 150.00, "description": "valor", "image_url": "../vaggies/valor.webp"},
#     {"name": "cobbage", "price": 40.00, "description": "cobbage", "image_url": "../vaggies/cobbage.jpeg"},
#     {"name": "Normal Mirch", "price": 80.00, "description": "Normal Mirch", "image_url": "../vaggies/normal_mirchi.jpg.webp"},
#     {"name": "g4 mirch", "price": 150.00, "description": "g4 mirch", "image_url": "../vaggies/g-4_mirchi.webp"},
#     {"name": "popat mircha", "price": 80.00, "description": "popat mircha", "image_url": "../vaggies/popat_mircha.webp"},
#     {"name": "Simla Mirch", "price": 80.00, "description": "Simla Mirch", "image_url": "../vaggies/Simla-Mirchi-.webp"},
#     {"name": "red simla", "price": 280.00, "description": "red simla", "image_url": "../vaggies/red_simla.webp"},
#     {"name": "Yellow Simla", "price": 290.00, "description": "Yellow Simla", "image_url": "../vaggies/yellow_simla.jpg"},
#     {"name": "Bhavnagiri Mirchi", "price": 120.00, "description": "Bhavnagiri Mirchi", "image_url": "../vaggies/bhavnagiri-mirchi.webp"},
#     {"name": "potatos", "price": 40.00, "description": "potatos", "image_url": "../vaggies/potatos.jpg"},
#     {"name": "Nasik onion", "price": 40.00, "description": "Nasik onion", "image_url": "../vaggies/onion.jpeg"},
#     {"name": "Best Garlic", "price": 300.00, "description": "Best Garlic", "image_url": "../vaggies/garlic.jpeg"},
#     {"name": "ginger", "price": 160.00, "description": "ginger", "image_url": "../vaggies/ginger.jpg.webp"},
#     {"name": "yam(suran)", "price": 120.00, "description": "yam(suran)", "image_url": "../vaggies/yam(suran).webp"},
#     {"name": "Ratalu", "price": 180.00, "description": "Ratalu", "image_url": "../vaggies/RATALU.webp"},
#     {"name": "bit", "price": 80.00, "description": "bit", "image_url": "../vaggies/bit.jpg"},
#     {"name": "Frozen Peas", "price": 140.00, "description": "Frozen Peas", "image_url": "../vaggies/vegestore-frozen-green-peas.jpg"},
#     {"name": "Frozen Garlic", "price": 250.00, "description": "Frozen Garlic", "image_url": "../vaggies/1kg-unpeeled-clove-garlic.jpeg"}
# ]

# # Insert product data into the database
# for product in products:
#     cursor.execute("""
#         INSERT INTO products (name, price, description, image_url)
#         VALUES (%s, %s, %s, %s)
#     """, (product['name'], product['price'], product['description'], product['image_url']))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Products inserted successfully!")
