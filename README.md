# CSV Unique Value Counter

A simple, user-friendly tool to count unique values in CSV columns, powered by DuckDB for fast processing.

## Features

- 📁 Easy file selection with GUI dialog
- 🔍 Fast CSV processing with DuckDB
- 📊 Count unique values in any column
- 💾 Automatic save to Downloads folder
- 📈 Results sorted by frequency
- 🖥️ Works with large CSV files efficiently

## Quick Start

### Option 1: Download Pre-Built Executable (Easiest - No Installation!)

**For Windows and Mac users - no Python or setup required!**

1. Go to the [Releases](../../releases) page
2. Download the latest version:
   - **Windows**: `CSV_Unique_Counter.exe`
   - **Mac**: `CSV_Unique_Counter`
3. Double-click to run!

**Mac users**: On first run, right-click → Open to bypass security warnings.

> **Note**: Executables are automatically built using GitHub Actions. See [GITHUB_SETUP.md](GITHUB_SETUP.md) for details.

### Option 2: Using Python

1. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **Install DuckDB**
   ```bash
   pip install duckdb
   ```

3. **Run the program**
   - Double-click `csv_unique_counter.py`
   - Or run from command line:
     ```bash
     python csv_unique_counter.py
     ```

### Option 3: Using Virtual Environment (Isolated Setup)

1. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program**
   ```bash
   python csv_unique_counter.py
   ```

### Option 4: Build Executable Yourself (Advanced)

If you want to build the executable manually on your own computer:

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Create executable**
   - Windows:
     ```bash
     pyinstaller --onefile --name "CSV_Unique_Counter" csv_unique_counter.py
     ```
   - Mac:
     ```bash
     pyinstaller --onefile --windowed --name "CSV_Unique_Counter" csv_unique_counter.py
     ```

3. **Find the executable**
   - Located in `dist/CSV_Unique_Counter.exe` (Windows) or `dist/CSV_Unique_Counter` (Mac)
   - **Note**: Executables are platform-specific. Build on Windows for Windows, Mac for Mac.

> **Tip**: Use GitHub Actions (see [GITHUB_SETUP.md](GITHUB_SETUP.md)) to build for both platforms automatically!

## How to Use

1. **Run the program** - Double-click the Python file or executable

2. **Select a CSV file** - A file dialog will open automatically

3. **Choose a column** - Select which column you want to analyze from the list

4. **View results** - The top 20 results will display in the console

5. **Check Downloads folder** - A complete report is saved automatically with timestamp

## Output Format

The program creates a CSV file in your Downloads folder named:
```
unique_values_[COLUMN_NAME]_[TIMESTAMP].csv
```

The file contains:
- Metadata header (source file, column name, total count, timestamp)
- Column headers: "Value" and "Count"
- Complete list of values with their counts (sorted by frequency, most common first)

**Benefits of CSV format:**
- ✅ Opens directly in Excel, Google Sheets, or any spreadsheet program
- ✅ Easy to sort, filter, and analyze further
- ✅ Can be imported into databases or other tools
- ✅ Preserves numerical formatting for counts

## System Requirements

- Python 3.7 or higher
- Windows/Mac/Linux
- DuckDB library (automatically handles CSV files of any size)

## Why DuckDB?

DuckDB is extremely fast for CSV processing and can handle:
- Large files (millions of rows)
- Various CSV formats (auto-detection)
- Complex queries efficiently
- In-memory processing (no database setup needed)

## Troubleshooting

**"Python is not recognized"**
- Make sure Python is added to your system PATH
- Try reinstalling Python with "Add to PATH" checked

**"No module named 'duckdb'"**
- Run: `pip install duckdb`

**File dialog doesn't appear**
- Make sure you're not running in a restricted environment
- Try running from command prompt/terminal

**Large files taking too long**
- DuckDB is optimized for large files, but extremely large files (GB+) may take time
- Consider filtering the CSV first if possible

## Support

For issues or questions, contact your IT administrator or the development team.


