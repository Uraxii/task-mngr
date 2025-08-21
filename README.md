# Task Manager

A Python script that prints task receipts to thermal receipt printers.

## Requirements

- Python 3.6+
- USB thermal receipt printer (tested with Epson TM-T20III)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Uraxii/task-mngr
cd task-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## CSV Format

Your CSV file should use semicolons (`;`) as delimiters and include these columns:

```csv
title;description;importance;urgency
Fix login bug;The login button is not responding on mobile devices;1;2
Update documentation;README needs to be updated with new API endpoints;2;1
Team meeting prep;Prepare slides for quarterly review meeting;3;1
```

**Column Definitions:**
- `title`: Brief task name
- `description`: Detailed task description
- `importance`: Integer (1=high, 2=medium, 3=low)
- `urgency`: Integer (1=high, 2=medium, 3=low)

## Usage

### Basic Usage

Print all tasks from a CSV file:
```bash
python main.py -f tasks.csv
```

### Preview Mode

See what will be printed without actually printing:
```bash
python main.py -f tasks.csv --whatif
```

### Test Printer

Test your printer connection:
```bash
python main.py --test
```

### Custom Delimiter

Use a different CSV delimiter:
```bash
python main.py -f tasks.csv -d ","
```

## Command Line Options

```
-f, --file          CSV file with tasks (required)
-d, --delimiter     CSV delimiter character (default: ';')
-t, --test          Run printer test
--whatif            Preview tasks without printing
```

## Receipt Format

Each printed receipt includes:
- Task title
- Importance and urgency ratings
- Full task description
- Proper formatting with spacing and cuts

Example output:
```
    Fix login bug

    I:(1) U:(2)

    The login button is not
    responding on mobile devices
```

## Supported Printers

The script includes definitions for various printer models:

To use a different printer, modify the vendor and model in `main.py`:
```python
vendor = VENDORS.CANON
model = MODELS.PIXMA
```
