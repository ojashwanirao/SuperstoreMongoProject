
---

## 🚀 Technologies Used

- Python 3.x  
- pandas  
- pymongo  
- MongoDB (local)  
- MongoDB Compass  
- Git & GitHub

---

## 📁 Dataset: `superstore.csv`

The dataset contains sample order records including:
- Order ID, Customer Name, Product, Category, Region, Sales, Profit, Ship Mode, etc.

---

## 🧪 What the Python Script Does

### 🔗 1. Connects to MongoDB
- Connects to local server at `mongodb://localhost:27017/`

### 📥 2. Loads CSV into MongoDB
- Loads `superstore.csv` into a MongoDB collection named `Orders` inside the database `SuperstoreDB`

### 🔍 3. Performs Practical Queries
- Print all orders  
- Count total documents  
- Find all orders from the "West" region  
- Find orders with `Sales > 500`  
- Find **Top 3 orders** by `Profit`  
- Update all `Ship Mode = First Class` → `Premium Class`  
- Delete all orders with `Sales < 50`  
- Group by `Region` and calculate total `Sales`  
- Show distinct values of `Ship Mode`  
- Count number of orders per `Category`

Run the script with:

```bash
python superstore_practicals.py

