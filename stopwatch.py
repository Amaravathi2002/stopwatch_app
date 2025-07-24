import time
from pymongo import MongoClient
from datetime import datetime

# 🔁 Replace with your actual connection string
client = MongoClient("mongodb+srv://Amaravathi_2002:Amara_2002@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Connect to database and collection
db = client["stopwatchDB"]
collection = db["timings"]

# START the stopwatch
input("⏱ Press Enter to START the stopwatch...")
start_time = datetime.now()
print("⏳ Stopwatch started at:", start_time)

# STOP the stopwatch
input("⏹ Press Enter to STOP the stopwatch...")
end_time = datetime.now()
print("🛑 Stopwatch stopped at:", end_time)

# CALCULATE duration
duration = end_time - start_time
print("🕒 Duration:", duration)

# SAVE to MongoDB
record = {
    "start_time": start_time,
    "end_time": end_time,
    "duration": str(duration)
}

collection.insert_one(record)
print("✅ Data saved to MongoDB.")