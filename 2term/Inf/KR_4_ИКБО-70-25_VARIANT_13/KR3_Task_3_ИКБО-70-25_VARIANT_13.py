# Group: ИКБО-70-25
# Student: George Mkrtchyan

from __future__ import annotations

import csv
import re
import statistics
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "variant_13" / "task_3.csv"


NUM_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")


def clean_text(value: str) -> str:
    return value.strip() if isinstance(value, str) else value


def parse_number(value: str):
    text = clean_text(value)
    if text in {"", "н/д", "нет данных"}:
        return None
    text = text.replace(",", ".")
    match = NUM_RE.search(text)
    if not match:
        return None
    number = float(match.group())
    return int(number) if number.is_integer() else number


def iqr_bounds(values: list[float]) -> tuple[float, float]:
    ordered = sorted(values)
    q1 = statistics.median(ordered[: len(ordered) // 2])
    q3 = statistics.median(ordered[(len(ordered) + 1) // 2 :]) if len(ordered) % 2 else statistics.median(ordered[len(ordered) // 2 :])
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


with INPUT_FILE.open(encoding="utf-8-sig", newline="") as f:
    raw_rows = [dict(row) for row in csv.DictReader(f)]

numeric_fields = ["visits_month", "trainer_hours", "progress_score", "subscription_months", "churn_flag"]
numeric_values = {field: [] for field in numeric_fields}
for row in raw_rows:
    for field in numeric_fields:
        value = parse_number(row[field])
        if value is not None:
            numeric_values[field].append(value)

outlier_bounds = {field: iqr_bounds(values) for field, values in numeric_values.items() if len(values) >= 4}

seen_ids: set[str] = set()
cleaned_rows = []
rejected_rows = []
error_counter = Counter()

for row in raw_rows:
    reasons = []
    cleaned = {key: clean_text(value) for key, value in row.items()}

    client_id = cleaned["client_id"]
    if client_id in seen_ids:
        reasons.append("duplicate_id")
    else:
        seen_ids.add(client_id)

    parsed = {}
    for field in numeric_fields:
        parsed[field] = parse_number(cleaned[field])

    if parsed["progress_score"] is None:
        reasons.append("missing_progress_score")
    if parsed["subscription_months"] is None:
        reasons.append("missing_subscription_months")
    if parsed["trainer_hours"] is None:
        reasons.append("invalid_numeric_trainer_hours")
    if parsed["trainer_hours"] is not None and parsed["trainer_hours"] < 0:
        reasons.append("negative_trainer_hours")
    if parsed["churn_flag"] not in {0, 1}:
        reasons.append("invalid_churn_flag")

    for field, value in parsed.items():
        if field in outlier_bounds and value is not None:
            lower, upper = outlier_bounds[field]
            if value < lower or value > upper:
                reasons.append(f"iqr_outlier_{field}")

    visits = parsed["visits_month"]
    progress = parsed["progress_score"]
    subscription = parsed["subscription_months"]
    churn = parsed["churn_flag"]

    if churn == 1 and progress is not None and subscription is not None and progress > 80 and subscription > 24:
        reasons.append("contradiction_high_progress_long_subscription")
    if churn == 0 and visits == 0 and progress is not None and progress > 80:
        reasons.append("contradiction_zero_visits_high_progress")

    if reasons:
        error_counter.update(reasons)
        cleaned["rejection_reasons"] = "; ".join(reasons)
        rejected_rows.append(cleaned)
        continue

    for field, value in parsed.items():
        if value is not None:
            cleaned[field] = str(value)
    cleaned_rows.append(cleaned)

out_clean = BASE_DIR / "task3_cleaned.csv"
with out_clean.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(raw_rows[0].keys()))
    writer.writeheader()
    writer.writerows(cleaned_rows)

out_rejected = BASE_DIR / "task3_rejected.csv"
with out_rejected.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(raw_rows[0].keys()) + ["rejection_reasons"])
    writer.writeheader()
    writer.writerows(rejected_rows)

accepted_count = len(cleaned_rows)
rejected_count = len(rejected_rows)
coefficient = accepted_count / len(raw_rows) * 100 if raw_rows else 0.0

quality_report_lines = [
    f"Файл: {INPUT_FILE.name}",
    f"Всего строк: {len(raw_rows)}",
    f"Принято строк: {accepted_count}",
    f"Отклонено строк: {rejected_count}",
    f"Коэффициент пригодности данных: {coefficient:.2f}%",
    "",
    "Типы ошибок:",
]
for name, count in error_counter.most_common():
    quality_report_lines.append(f"- {name}: {count}")
(BASE_DIR / "task3_quality_report.txt").write_text("\n".join(quality_report_lines), encoding="utf-8")

rules_text = [
    "Правила контроля качества для task_3.csv:",
    "1. Строки с пропуском progress_score или subscription_months отклоняются.",
    "2. Строки с отрицательным trainer_hours отклоняются.",
    "3. Повторяющиеся client_id отклоняются начиная со второго вхождения.",
    "4. Для числовых полей используется правило межквартильного размаха (IQR); выбросы отклоняются.",
    "5. Строки отклоняются при межполевых противоречиях: churn_flag=1 при progress_score>80 и subscription_months>24, а также churn_flag=0 при visits_month=0 и progress_score>80.",
    "6. Допустимые текстовые пробелы по краям значений удаляются.",
]
(BASE_DIR / "task3_validation_rules.txt").write_text("\n".join(rules_text), encoding="utf-8")

