# Inventory Management System

## Description

A Flask-based REST API for managing inventory items.

The application provides CRUD operations and integrates
with the Open Food Facts API to retrieve product information.

## Features

- View inventory
- View individual products
- Add inventory items
- Update inventory items
- Delete inventory items
- Search Open Food Facts
- Import products from Open Food Facts
- CLI interface
- Automated tests

## Technologies

- Python
- Flask
- Requests
- Pytest
- Open Food Facts API
- Git/GitHub

## Installation

Clone the repository:

git clone YOUR_REPOSITORY_URL

Navigate into the project:

cd inventory-management-system

Create virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Running the API

python3 app.py

## Running the CLI

python3 cli.py

## Running Tests

pytest

## API Routes

GET /inventory

GET /inventory/<id>

POST /inventory

PATCH /inventory/<id>

DELETE /inventory/<id>

GET /products/barcode/<barcode>

POST /inventory/import/<barcode>