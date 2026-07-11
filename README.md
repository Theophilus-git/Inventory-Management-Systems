# Inventory Management System

A web-based inventory management system built with Django. This project allows users to track products, manage stock levels, and maintain supplier information through a simple, database-backed interface.

## Features

- Add, view, update, and delete products
- Track key product details: name, SKU, price, quantity, and supplier
- Unique SKU enforcement to prevent duplicate stock entries
- Form-based product creation and editing using Django's `ModelForm`
- Built on Django's ORM for reliable data management

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default, configurable for production use)
- **Frontend:** Django Templates, HTML/CSS

## Project Structure

```
inventory_Management_Systems/
├── invProject/
│   ├── invApp/
│   │   ├── models.py       # Product model definition
│   │   ├── forms.py        # ProductForm linked to Product model
│   │   ├── views.py        # Application logic
│   │   ├── urls.py         # App-level routing
│   │   └── templates/      # HTML templates
│   ├── invProject/
│   │   ├── settings.py     # Project configuration
│   │   └── urls.py         # Project-level routing
│   └── manage.py
├── venv/                   # Virtual environment (not tracked in git)
└── README.md
```

## Model Overview

The core of the system is the `Product` model:

| Field         | Type        | Description                        |
|---------------|-------------|-------------------------------------|
| `product_id`  | AutoField   | Primary key (auto-generated)        |
| `name`        | CharField   | Product name                        |
| `sku`         | CharField   | Unique stock keeping unit           |
| `price`       | FloatField  | Product price                       |
| `quantity`    | IntegerField| Quantity in stock                   |
| `supplier`    | CharField   | Supplier name                       |

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/inventory_Management_Systems.git
   cd inventory_Management_Systems
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install django
   ```

4. Navigate into the project folder and run migrations
   ```bash
   cd invProject
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://127.0.0.1:8000/`

## Usage

Once the server is running, you can:
- Add new products through the product creation form
- View a list of all products currently in stock
- Edit product details as stock levels or prices change
- Remove products that are discontinued

## Roadmap

- [ ] Add user authentication for staff access
- [ ] Convert `supplier` field into a dedicated `Supplier` model with a foreign key relationship
- [ ] Add low-stock alerts and notifications
- [ ] Add search and filtering by SKU, name, or supplier
- [ ] Deploy to a production environment

## Contributing

This is currently a personal learning project. Suggestions and feedback are welcome via issues or pull requests.

## License

This project is open source and available for personal and educational use.
