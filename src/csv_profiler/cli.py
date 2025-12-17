import typer
import sys
import subprocess
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import generate_json_report, generate_markdown_report

app = typer.Typer()

@app.command()
def profile(
    dataset: str = typer.Argument(..., help="Path to the input CSV file"),
    out_dir: str = typer.Option("outputs", help="Directory to save the reports"),
    format: str = typer.Option("both", help="Output format: json, markdown, or both")
):
    """
    Profile a CSV dataset and generate reports.
    """
    try:
        rows = read_csv_rows(dataset)
    except FileNotFoundError:
        print(f"Error: The file '{dataset}' was not found.")
        raise typer.Exit(code=1)

    report = basic_profile(rows)

    output_path = Path(out_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    json_file = output_path / "report.json"
    md_file = output_path / "report.md"

    fmt = format.lower()
    
    if fmt in ["json", "both"]:
        json_content = generate_json_report(report)
        json_file.write_text(json_content, encoding="utf-8")
        print(f"Saved {json_file}")

    if fmt in ["markdown", "both"]:
        md_content = generate_markdown_report(report)
        md_file.write_text(md_content, encoding="utf-8")
        print(f"Saved {md_file}")

    print("Done!")

@app.command()
def web():
    """
    Launch the Streamlit web interface.
    """
    # Find app.py relative to this script (cli.py)
    app_path = Path(__file__).parent / "app.py"
    
    print("Starting Streamlit app...")
    
    # Run the shell command: python -m streamlit run src/csv_profiler/app.py
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path)])

@app.command()
def version():
    print("CSV Profiler v1.0")

if __name__ == "__main__":
    app()