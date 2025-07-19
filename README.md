
# 🚆 KPA Backend Assignment – FastAPI + PostgreSQL

This is a backend model for the KPA form data assignment. It includes two main API endpoints developed using **FastAPI** and stores the data in a **PostgreSQL** database.

---

## ✅ Features Implemented

### 1. Create Wheel Specification API
- **Endpoint:** `POST /wheel-spec`
- **Fields:**
  - `wheel_number` (str)
  - `diameter` (float)
  - `width` (float)
  - `material` (str)
  - `inspection_date` (date)

### 2. Create Bogie Checksheet API
- **Endpoint:** `POST /bogie-check`
- **Fields:**
  - `bogie_number` (str)
  - `inspector_name` (str)
  - `status` (str)
  - `checked_on` (date)

### 🛠️ Functionality
- Stores data in **PostgreSQL**
- APIs tested using **Postman** and **Swagger UI** (`/docs`)

---

## 🧰 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Python-dotenv
- PgAdmin (for DB verification)
- Postman

---

## 📁 Project Structure

```

.
├── main.py                # FastAPI app
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── database.py            # DB setup and connection
├── .env                   # Environment variables
├── postman\_collection.json  # Postman collection for testing
├── requirements.txt       # Dependencies
├── README.md              # Project overview

````

---

## 🧪 How to Run and Test

### Step 1: Clone & Install
```bash
git clone https://github.com/aby-595/kpa-assignment.git
cd kpa-assignment
pip install -r requirements.txt
````

### Step 2: Configure Environment

Create a `.env` file with your PostgreSQL credentials:

```
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/your_database
```

### Step 3: Start the Server

```bash
uvicorn main:app --reload
```

### Step 4: Test APIs

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* **Postman:** Use `postman_collection.json` to test locally

---

## 📷 Submission Includes

* ✅ Screenshot of successful Postman tests
* ✅ Screenshot of stored data in PgAdmin
* ✅ GitHub repository with code
* ✅ README file (this)

---

## 🙋 Author

**Aby Daniel Varghese**
Backend Developer – KPA Assignment
GitHub: [aby-595](https://github.com/aby-595)


