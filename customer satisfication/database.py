
import sqlite3 
conn = sqlite3.connect('planedata.db')  

query_to_create_table = """
CREATE TABLE planeDetails (
age INT,
flight_distance INT,
inflight_entertainment INT,
baggage_handling INT,
cleanliness INT,
 departure_delay INT,
 arrival_delay INT,
 gender VARCHAR(40),
 customer_type VARCHAR(40),
 travel_type VARCHAR(40)
 ,economy VARCHAR(40),
 economy_plus VARCHAR(40),
 label_dict[PREDICTION] INT
)
"""

cur = conn.cursor() 
cur.execute(query_to_create_table) 
print("Your database is created!")
cur.close() 
conn.close()