# CSV Profiler

A simple tool I built to quickly analyze CSV files. It reads a dataset and generates a report with row counts, missing values, and column stats.

You can run it in the terminal or use the web interface if you like.

## ⚡ Quick Start (No Install)
If you have `uv` installed, you can run the tool directly from GitHub without downloading anything:

**To launch the Web App:**
```bash
uvx [https://github.com/nawafalduaij/Csv-profiler.git](https://github.com/nawafalduaij/Csv-profiler.git) web
```

**To run the CLI:**
```bash
uvx [https://github.com/nawafalduaij/Csv-profiler.git](https://github.com/nawafalduaij/Csv-profiler.git) profile data/sample.csv
```

## What it does
- **CLI Mode:** Run a command, get a JSON or Markdown report.
- **Web App:** A simple Streamlit dashboard to drag-and-drop files.
- **Stats:** Detailed breakdown of your data (min/max, unique values, types).

## Setup
You need Python 3.10+ installed.

1. Clone the repo:
   ```bash
   git clone [https://github.com/nawafalduaij/Csv-profiler.git](https://github.com/nawafalduaij/Csv-profiler.git)
   cd Csv-profiler
   ```

2. Install it:
   ```bash
   uv pip install .
   ```

## How to run it

### 1. In the Terminal
To analyze a file and save the reports to an `outputs` folder:
```bash
python -m csv_profiler.cli profile data/sample.csv
```

You can also specify the format if you only want one type:
```bash
python -m csv_profiler.cli profile data/sample.csv --format markdown
```

### 2. The Web App
If you want to use the UI, just run this shortcut:
```bash
python -m csv_profiler.cli web
```
This will open the dashboard in your browser.

## Project Layout
Everything is inside the `src` folder to keep things clean.
- `cli.py`: The command line logic (Typer).
- `app.py`: The web dashboard (Streamlit).
- `profile.py`: The actual math/stats logic.
