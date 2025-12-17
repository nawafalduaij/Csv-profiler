from statistics import mean
from collections import Counter

# --- Helper Functions ---
def is_missing(value: str) -> bool:
    if value is None: return True
    return value.strip().casefold() in {"", "na", "n/a", "null", "none", "nan"}

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def infer_type(values: list[str]) -> str:
    usable = [v for v in values if not is_missing(v)]
    if not usable: return "text"
    for v in usable:
        if try_float(v) is None: return "text"
    return "number"

def numeric_stats(values: list[str]) -> dict:
    usable = [v for v in values if not is_missing(v)]
    nums = [try_float(v) for v in usable if try_float(v) is not None]
    if not nums: return {}
    return {"min": min(nums), "max": max(nums), "mean": mean(nums)}

def text_stats(values: list[str], top_k: int = 3) -> dict:
    usable = [v for v in values if not is_missing(v)]
    counts = Counter(usable)
    top = [{"value": v, "count": c} for v, c in counts.most_common(top_k)]
    return {"top": top}

# --- Class ---
class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self.name = name
        self.inferred_type = inferred_type
        self.total = total
        self.missing = missing
        self.unique = unique
        self.extra_stats = {} 

    @property
    def missing_pct(self) -> float:
        return (self.missing / self.total * 100) if self.total else 0.0

    def to_dict(self) -> dict:
        base = {
            "name": self.name, "type": self.inferred_type, 
            "total": self.total, "missing": self.missing, 
            "missing_pct": self.missing_pct, "unique": self.unique
        }
        base.update(self.extra_stats)
        return base

# --- Main Logic (The name MUST be basic_profile) ---
def basic_profile(rows: list[dict[str, str]]) -> dict:
    if not rows: return {"rows": 0, "n_cols": 0, "columns": {}}
    
    columns = list(rows[0].keys())
    col_profiles = []

    for col in columns:
        values = [row.get(col, "") for row in rows]
        total = len(values)
        usable = [v for v in values if not is_missing(v)]
        missing = total - len(usable)
        unique = len(set(usable))
        col_type = infer_type(values)

        profile = ColumnProfile(col, col_type, total, missing, unique)
        
        if col_type == "number":
            profile.extra_stats = numeric_stats(values)
        else:
            profile.extra_stats = text_stats(values)
            
        col_profiles.append(profile)

    return {
        "rows": len(rows), "n_cols": len(columns),
        "columns": {p.name: p.to_dict() for p in col_profiles}
    }
