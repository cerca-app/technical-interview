## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
alembic upgrade head
```

4. Run the `populate_db.py` script to populate the database with test data:
```bash
python3 populate_db.py
```