# Flask Todo App

A lightweight and fast Todo application built with **Flask**, **SQLAlchemy**, and styled with **Semantic UI**. 

This project is designed to be easy to set up for local development and is fully configured for seamless deployment to serverless platforms like Vercel.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (Local) / PostgreSQL (Production)
- **ORM:** Flask-SQLAlchemy
- **Frontend:** HTML/Jinja2 templates, Semantic UI CSS

---

## 💻 Local Development Setup

Follow these steps to get the app running on your local machine.

### Prerequisites
- Python 3.8+ installed
- `pip` installed

### 1. Clone & Navigate
```console
$ git clone <your-repo-url>
$ cd flask-todo-master
```

### 2. Create a Virtual Environment
It's best practice to use a virtual environment to manage your dependencies.

**macOS/Linux:**
```console
$ python3 -m venv venv
$ source venv/bin/activate
```

**Windows:**
```console
> python -m venv venv
> venv\Scripts\activate
```

### 3. Install Dependencies
Install all required packages from `requirements.txt`:
```console
$ pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```console
$ python app.py
```
*Note: The local SQLite database (`db.sqlite`) and its tables will be automatically created on the first run.*

Open your browser and navigate to `http://127.0.0.1:5000` to see the app in action!

---

## 🚀 Deployment to Vercel

This application is pre-configured with a `vercel.json` file for easy serverless deployment on Vercel.

### Phase 1: Initial Deployment
1. Push your code to a new repository on GitHub.
2. Log in to [Vercel](https://vercel.com/) and click **Add New** -> **Project**.
3. Import your GitHub repository.
4. Keep all the default settings and click **Deploy**.
5. *Note: The app will initially deploy using a temporary SQLite database in `/tmp`. This means your todos will work, but the data will be lost
    when Vercel spins down the serverless function. It may fail also so you need to create a Database on vercel*

### Phase 2: Setup Vercel Postgres (Permanent Storage)
To make your data persist permanently, connect a PostgreSQL database:
1. In your Vercel Dashboard, go to your newly deployed project.
2. Click on the **Storage** tab at the top.
3. Click **Connect Database** (or **Connect Store**), select **Neon Postgres**, and click **Continue**.
4. Accept the terms, choose a database name (e.g., `flask-todo-db`), pick a region close to your users, and click **Create**.
5. When prompted, ensure the database is connected to all environments (Production, Preview, Development) and click **Connect**.
6. *Vercel automatically injects the required `POSTGRES_URL` environment variable into your project.*
7. Finally, go back to the **Deployments** tab and **Redeploy** your application. 

Your app will automatically detect the new Postgres connection, create the necessary tables, and start saving your todos permanently!
