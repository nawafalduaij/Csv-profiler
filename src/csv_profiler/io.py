from csv import DictReader
from pathlib import Path
from io import StringIO

def read_csv_rows(path: str) -> list[dict[str, str]]:

    file_path = Path(path)
    with file_path.open("r", encoding="utf-8", newline="") as f:
        reader = DictReader(f)
        return [dict(row) for row in reader]

def parse_csv_string(csv_text: str) -> list[dict[str, str]]:
    
    reader = DictReader(StringIO(csv_text))
    return list(reader)


def write_json(text: str, path: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")

def write_markdown(text: str, path: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")
