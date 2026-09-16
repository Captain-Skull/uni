# Group: ИКБО-70-25
# Student: George Mkrtchyan

from __future__ import annotations

import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "variant_13" / "task_1.csv"


def clean_text(value: str) -> str:
    return value.strip() if isinstance(value, str) else value


def parse_number(value: str):
    text = clean_text(value)
    if text == "":
        return None
    if isinstance(text, str):
        try:
            if "." in text or "e" in text.lower():
                number = float(text)
                return int(number) if number.is_integer() else number
            return int(text)
        except ValueError:
            return None
    return None


def infer_role(field_name: str, sample_values: list[str]) -> tuple[str, str]:
    lowered = field_name.lower()
    if lowered.endswith("_id") or lowered == "client_id" or lowered == "operator_id":
        return "str", "identification"

    parsed_numbers = [parse_number(v) for v in sample_values if clean_text(v) != ""]
    valid_numbers = [v for v in parsed_numbers if v is not None]
    if valid_numbers and all(v in (0, 1) for v in valid_numbers):
        return "int", "logical"
    if valid_numbers and all(float(v).is_integer() for v in valid_numbers):
        return "int", "numeric"
    if valid_numbers:
        return "float", "numeric"
    return "str", "categorical"


with INPUT_FILE.open(encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    records = [{k: clean_text(v) for k, v in row.items()} for row in reader]

field_names = reader.fieldnames or []
row_count = len(records)
col_count = len(field_names)

first_three = records[:3]
last_three = records[-3:]
preview = records[:10]

types_by_field: list[tuple[str, str, str, str]] = []
for field in field_names:
    sample = [row[field] for row in records[: min(20, row_count)]]
    inferred_type, role = infer_role(field, sample)
    comment = {
        "client_id": "Идентификатор записи",
        "age_group": "Возрастная группа клиента",
        "visits_month": "Число посещений в месяц",
        "trainer_hours": "Часы работы с тренером",
        "progress_score": "Оценка прогресса клиента",
        "subscription_months": "Срок подписки в месяцах",
        "churn_flag": "Логический признак оттока",
        "validation_status": "Служебный статус проверки",
        "error_comment": "Текстовый комментарий по качеству",
        "region": "Регион клиента",
        "operator_id": "Идентификатор оператора",
    }.get(field, "")
    types_by_field.append((field, inferred_type, role, comment))

report_lines = [
    f"Файл: {INPUT_FILE.name}",
    f"Количество строк: {row_count}",
    f"Количество полей: {col_count}",
    "",
    "Первые 3 наблюдения:",
    json.dumps(first_three, ensure_ascii=False, indent=2),
    "",
    "Последние 3 наблюдения:",
    json.dumps(last_three, ensure_ascii=False, indent=2),
    "",
    "Автоматическая классификация полей:",
]
for field, inferred_type, role, comment in types_by_field:
    report_lines.append(f"- {field}: {inferred_type} / {role} — {comment}")

(BASE_DIR / "task1_read_report.txt").write_text("\n".join(report_lines), encoding="utf-8")

with (BASE_DIR / "task1_preview.json").open("w", encoding="utf-8") as f:
    json.dump(preview, f, ensure_ascii=False, indent=2)

with (BASE_DIR / "task1_data_dictionary.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["field_name", "inferred_type", "role", "comment"])
    writer.writeheader()
    for field_name, inferred_type, role, comment in types_by_field:
        writer.writerow(
            {
                "field_name": field_name,
                "inferred_type": inferred_type,
                "role": role,
                "comment": comment,
            }
        )

selected_fields = ["client_id", "age_group", "visits_month", "progress_score"]
with (BASE_DIR / "task1_selected_columns.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=selected_fields)
    writer.writeheader()
    for row in records:
        writer.writerow({field: row[field] for field in selected_fields})

