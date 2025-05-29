import pandas as pd
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["SuperstoreDB"]
collection = db["Orders"]

# Step 2: OPTIONAL - Clear existing data to avoid duplicates
collection.delete_many({})

# Step 3: Load CSV into MongoDB
try:
    df = pd.read_csv("superstore.csv", encoding='ISO-8859-1')
    print("✅ CSV loaded successfully")
    print(df.head())

    # Insert data into MongoDB
    collection.insert_many(df.to_dict("records"))
    print("✅ Data inserted into MongoDB")

except Exception as e:
    print("❌ Error loading or inserting CSV:", e)

# ---------- PRACTICAL QUESTIONS BELOW ---------- #

# 1. Retrieve and print all documents from the Orders collection
print("\n1. All Orders:")
for doc in collection.find():
    print(doc)

# 2. Count and display the total number of documents
total_docs = collection.count_documents({})
print(f"\n2. Total Documents: {total_docs}")

# 3. Fetch all orders from the "West" region
print("\n3. Orders from West Region:")
for doc in collection.find({"Region": "West"}):
    print(doc)


# 4. Find orders where Sales > 500
print("\n4. Orders with Sales > 500:")
for doc in collection.find({"Sales": {"$gt": 500}}):
    print(doc)

# 5. Top 3 orders with highest Profit
print("\n5. Top 3 Orders by Profit:")
for doc in collection.find().sort("Profit", -1).limit(3):
    print(doc)

# 6. Update all Ship Mode = "First Class" to "Premium Class"
result = collection.update_many(
    {"Ship Mode": "First Class"},
    {"$set": {"Ship Mode": "Premium Class"}}
)
print(f"\n6. Updated {result.modified_count} documents from 'First Class' to 'Premium Class'.")

# 7. Delete all orders where Sales < 50
deleted = collection.delete_many({"Sales": {"$lt": 50}})
print(f"7. Deleted {deleted.deleted_count} orders with Sales < 50.")

# 8. Group by Region and calculate total Sales per region
print("\n8. Total Sales per Region:")
pipeline = [
    {"$group": {"_id": "$Region", "TotalSales": {"$sum": "$Sales"}}}
]
for result in collection.aggregate(pipeline):
    print(result)


# 9. Fetch all distinct values for Ship Mode
ship_modes = collection.distinct("Ship Mode")
print("\n9. Distinct Ship Modes:", ship_modes)

# 10. Count the number of orders for each Category
print("\n10. Number of Orders per Category:")
pipeline = [
    {"$group": {"_id": "$Category", "Count": {"$sum": 1}}}
]
for result in collection.aggregate(pipeline):
    print(result)

    