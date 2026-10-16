# 🛒 SUPERMARKET MANAGEMENT SYSTEM

> A professional desktop application for comprehensive supermarket/retail store management and operations, built on **Python** and **PySide6 (Qt for Python)** following standard **Layered Architecture / MVC**.

---

## 👥 Team Members & Task Assignments

| # | Member | Role & Subsystem | Detailed Tasks |
| :--- | :--- | :--- | :--- |
| **1** | **Le Tran Khang** | **Team Leader / Backend & Core Architecture** | - Build **Dashboard overview** (KPIs, revenue, orders, stock alerts).<br>- Design system-wide configuration (`config/settings.py`, `config/database.py`).<br>- **Login, Logout** & **Forgot Password** module (send OTP via Email).<br>- **Role-Based Access Control (RBAC)** architecture & Session management (`Session`). |
| **2** | **Le Hong Gam** | **HR & Partner Management** | - **Employee Account Management** module (CRUD employees, role assignment, password reset, activity status).<br>- **Supplier Management** module (supplier information, address, contacts, vendor directory management). |
| **3** | **Tran Thai Kiet** | **POS Sales & UI/UX Design** | - **POS (Point of Sale)** subsystem: scan/select products, apply discounts, calculate VAT, cash/bank transfer payment, print invoices.<br>- **Help Center** module: user guides and operational support.<br>- **UI/UX Styling & Theme design**: standardize icon system (`qtawesome`), layout and user experience. |
| **4** | **Dang Hoang Quoc Cuong** | **Customer & Analytics Reporting** | - **Customer Management** module: store profiles, purchase history, customer tier classification, search and select customers at checkout.<br>- **Analytics & Reporting** subsystem: visual charts for revenue over time, category breakdown, business trends. |
| **5** | **Phan Tuan Kha** | **Product & Inventory Management** | - **Product Management** module: manage product catalog, retail price, cost price, barcode, business status.<br>- **Purchase / Import Orders** subsystem: create import orders from suppliers, quantity checking, automatic inventory update. |

---

## 🛠️ Technologies & Libraries

- **Programming Language**: Python 3.10+
- **User Interface (UI/UX)**:
  - `PySide6` (Qt6 for Python)
  - `qtawesome` (FontAwesome icon set for Qt)
- **Database & ORM**:
  - `SQLAlchemy` (ORM & Database Session Management)
  - `mysql-connector-python` (MySQL support)
  - `pymssql` (Microsoft SQL Server support)
- **Security & Utilities**:
  - `bcrypt` (Secure password hashing)
  - `python-dotenv` (Environment variable management)
  - `smtplib` & `email.mime` (Send OTP verification emails for password reset)
  - `reportlab` & `Pillow` (Export sales invoices in standard PDF format)

---

## 🏛️ Project Structure

```text
Supermarket_Manager/
├── assets/                    # Images, icons, fonts and UI resources
├── config/                    # System configuration
│   ├── database.py            # Database connection management (MySQL / SQL Server)
│   └── settings.py            # Read and define system parameters from .env
├── src/
│   ├── controller/            # UI logic controllers and user interaction handling
│   ├── converter/             # Data conversion between Entity and DTO
│   ├── dtos/                  # Data Transfer Objects (DTO) for data passing
│   ├── entities/              # ORM table definitions and relationships (Entities)
│   ├── gui/                   # Qt interface (Dialogs, Windows, Tabs)
│   ├── repositories/          # Data access layer for direct database queries
│   ├── services/              # Business logic layer
│   └── utils/                 # Utilities: EmailHelper, PasswordHasher, Theme, InvoicePrinter...
├── .env.example               # Sample configuration file
├── requirements.txt           # List of dependency libraries
├── README.md                  # Project documentation and guide
└── main.py                    # Application entry point
```

---

## ⚙️ Installation & Configuration Guide

### 1. Prerequisites
- **Python 3.10** or higher installed ([Download Python](https://www.python.org/downloads/)).
- A database management system installed: **MySQL** (XAMPP/MySQL Server recommended) or **Microsoft SQL Server**.

### 2. Environment setup and library installation
Open Terminal / Command Prompt / PowerShell at the project root directory and run the following commands:

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment:
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# Or on Command Prompt (cmd):
.venv\Scripts\activate.bat

# Install dependencies:
pip install -r requirements.txt
```

---

### 3. Environment variable configuration (`.env`)

Create a `.env` file at the project root directory (copy from `.env.example`):

```bash
cp .env.example .env
```

Configuration contents in the `.env` file:

```ini
# ==============================================================================
# 1. DATABASE CONFIGURATION
# ==============================================================================
# Choose DB type: 'mysql' or 'mssql'
DB_TYPE=mysql

# MySQL Configuration
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=supermarket_db

# SQL Server Configuration (if using MSSQL)
MSSQL_SERVER=localhost
MSSQL_PORT=1433
MSSQL_USER=sa
MSSQL_PASSWORD=your_mssql_password
MSSQL_NAME=supermarket_db

DB_POOL_NAME=supermarket_pool
DB_POOL_SIZE=5

# ==============================================================================
# 2. SALES & INVENTORY CONFIGURATION
# ==============================================================================
VAT_RATE=0.08
DEFAULT_DISCOUNT_RATE=0.0
MAX_DISCOUNT_RATE=0.5
LOW_STOCK_THRESHOLD=10
PRODUCT_PAGE_SIZE=60

# ==============================================================================
# 3. EMAIL VERIFICATION (SMTP) CONFIGURATION
# ==============================================================================
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

---

### 4. 📧 Email Verification Configuration Guide (Google App Password)

To enable the system to send verification codes (6-digit OTP) when employees/managers use the **Forgot Password** feature, you need to configure a Gmail account with an **App Password**:

> ⚠️ **Important security notes**:
> - **Never** use your Gmail account's direct login password.
> - **Do not push the `.env` file containing real passwords to the Git repository**.

#### Steps to create an App Password on Gmail:
1. Go to [Google Account Security](https://myaccount.google.com/security).
2. Under **"How you sign in to Google"**, make sure you have enabled **2-Step Verification**.
3. Search for **"App Passwords"** or go directly to: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
4. Enter an app name (e.g., `Supermarket_Manager`) and click **Create**.
5. Google will generate a **16-character** string (format: `xxxx xxxx xxxx xxxx`).
6. Paste this 16-character string into the `EMAIL_PASSWORD` variable in the `.env` file (you may keep or remove the spaces).
7. Enter the corresponding Gmail address in `EMAIL_USER`.

---

## 🚀 Running the Application

After completing the database and `.env` file configuration, start the system with:

```bash
python main.py
```

- The system will automatically check and initialize the database table structure (if it does not yet exist).
- The login screen will appear, allowing users to sign in according to their assigned roles.

---

## 🔐 System Authorization (RBAC)

The system supports role groups with separate permissions:
- **Admin**: Full access to Dashboard, employee management, configuration, products, suppliers, customers, and financial reports.
- **Cashier**: Access to POS sales subsystem, customer search, apply discounts within limits, print invoices.
- **Inventory Staff**: Manage products, create import orders, monitor stock levels and out-of-stock alerts.

---

## 📄 License

- This project was developed as a **final project for the Python Programming and Applications course**.
- It serves educational and research purposes for retail management software applications. All contributions and source code comply with the team's academic regulations.

