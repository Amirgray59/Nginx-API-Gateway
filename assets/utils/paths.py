from pathlib import Path

BASE_STATIC_DIR = (Path(__file__).resolve().parents[1] / "static" / "img")

BASE_STATIC_DIR.mkdir(parents=True, exist_ok=True)

