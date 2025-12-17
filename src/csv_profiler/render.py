import json
from pathlib import Path

def generate_json_report(report: dict) -> str:
    """Generate JSON report string (Day 4 Ex 3)."""
    return json.dumps(report, indent=2, ensure_ascii=False)

def generate_markdown_report(report: dict) -> str:
    """Generate Markdown report string (Day 4 Ex 3)."""
    lines = []
    lines.append("# CSV Profiling Report")
    lines.append("## Summary")
    lines.append(f"- **Rows:** {report.get('rows', 0)}")
    lines.append(f"- **Columns:** {report.get('n_cols', 0)}")
    
    lines.append("\n## Column Details")
    lines.append("| Column | Type | Missing | Stats |")
    lines.append("|---|---|---|---|")
    
    for col_name, stats in report.get("columns", {}).items():
        ctype = stats.get("type", "unknown")
        missing = stats.get("missing", 0)
        
        if ctype == "number":
            mn = stats.get("min", 0)
            mx = stats.get("max", 0)
            details = f"Min: {mn:.2f}, Max: {mx:.2f}"
        else:
            top_list = stats.get("top", [])
            top_strs = [f"{item['value']}({item['count']})" for item in top_list]
            details = ", ".join(top_strs)
            
        lines.append(f"| {col_name} | {ctype} | {missing} | {details} |")

    return "\n".join(lines)


def write_json(report: dict, path: str) -> None:
    text = generate_json_report(report)
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")

def write_markdown(report: dict, path: str) -> None:
    text = generate_markdown_report(report)
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")