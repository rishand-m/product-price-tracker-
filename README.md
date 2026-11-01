# Product Price Tracker

A Python automation project that retrieves product data from an API, sorts and filters products by price, and exports affordable products into an Excel spreadsheet.

## Features
- Fetches product data using an API
- Sorts products by price
- Filters products below ₹50
- Exports results into an Excel file
- Uses environment variables to protect API credentials

## Technologies Used
- Python
- Requests
- OpenPyXL
- REST APIs
- Git and GitHub

## Installation

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API key:

```env
API_KEY=your_api_key
```

4. Run the project:

```bash
python main.py
```

## Output

Generates `affordable_products.xlsx` containing filtered product names and prices.

## Security

API credentials are stored in environment variables and are not included in the repository.
