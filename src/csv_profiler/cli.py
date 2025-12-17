import typer
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profile import basic_profile
from csv_profiler.render import generate_json_report, generate_markdown_report

app = typer.Typer()

@app.command()
def profile(
    dataset: str = typer.Argument(..., help="Path to the input CSV file"),
    out_dir: str = typer.Option("outputs", help="Directory to save the reports")
):
    """
    Profile a CSV dataset and generate reports.
    """
    print(f"Reading from {dataset}...")
    
    try:
        rows = read_csv_rows(dataset)
    except FileNotFoundError:
        print(f"Error: The file '{dataset}' was not found.")
        raise typer.Exit(code=1)

    print(f"Profiling {len(rows)} rows...")
    report = basic_profile(rows)

    
    json_content = generate_json_report(report)
    md_content = generate_markdown_report(report)

    
    output_path = Path(out_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    json_file = output_path / "report.json"
    md_file = output_path / "report.md"
    
    json_file.write_text(json_content, encoding="utf-8")
    md_file.write_text(md_content, encoding="utf-8")
    
    print(f"Reports saved to {out_dir}/")

if __name__ == "__main__":
    app()