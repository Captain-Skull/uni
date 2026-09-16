# Group: ИКБО-70-25
# Student: George Mkrtchyan

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "variant_13" / "task_2.csv"


def clean_text(value: str) -> str:
    return value.strip() if isinstance(value, str) else value


def parse_number(value: str):
    text = clean_text(value)
    if text in {"", "н/д", "нет данных"}:
        return None
    text = text.replace(",", ".")
    try:
        number = float(text)
    except ValueError:
        return None
    return int(number) if number.is_integer() else number


def quartiles(values: list[float]) -> tuple[float, float, float]:
    ordered = sorted(values)
    median = statistics.median(ordered)
    lower = ordered[: len(ordered) // 2]
    upper = ordered[(len(ordered) + 1) // 2 :] if len(ordered) % 2 else ordered[len(ordered) // 2 :]
    q1 = statistics.median(lower)
    q3 = statistics.median(upper)
    return q1, median, q3


with INPUT_FILE.open(encoding="utf-8-sig", newline="") as f:
    rows = [{k: clean_text(v) for k, v in row.items()} for row in csv.DictReader(f)]

for row in rows:
    for field in ["visits_month", "trainer_hours", "progress_score", "subscription_months", "churn_flag"]:
        row[field] = parse_number(row[field])

category_field = "age_group"
metric_field = "progress_score"

metric_values = [row[metric_field] for row in rows if row[metric_field] is not None]
q1, median_value, q3 = quartiles(metric_values)
mean_value = statistics.mean(metric_values)

filtered_rows = [
    row
    for row in rows
    if row[metric_field] is not None and (row[metric_field] > median_value or row[metric_field] >= q3)
]

with (BASE_DIR / "task2_filtered.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(filtered_rows)

summary = defaultdict(list)
for row in filtered_rows:
    summary[row[category_field]].append(row[metric_field])

summary_rows = []
for group, values in sorted(summary.items()):
    summary_rows.append(
        {
            "age_group": group,
            "count": len(values),
            "mean_progress_score": round(statistics.mean(values), 2),
            "min_progress_score": min(values),
            "max_progress_score": max(values),
        }
    )

with (BASE_DIR / "task2_group_summary.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["age_group", "count", "mean_progress_score", "min_progress_score", "max_progress_score"],
    )
    writer.writeheader()
    writer.writerows(summary_rows)

focus_group = min(summary_rows, key=lambda row: row["mean_progress_score"])
report = [
    f"Файл: {INPUT_FILE.name}",
    f"Выбранное категориальное поле: {category_field}",
    f"Выбранный числовой показатель: {metric_field}",
    f"Среднее значение показателя: {mean_value:.2f}",
    f"Медиана показателя: {median_value:.2f}",
    f"Границы квартилей: Q1={q1:.2f}, Q3={q3:.2f}",
    f"После фильтрации отобрано строк: {len(filtered_rows)}",
    f"Наименьшее среднее значение у группы {focus_group['age_group']} ({focus_group['mean_progress_score']:.2f}), ей стоит уделить внимание.",
    f"Наиболее сильная группа по среднему значению: {max(summary_rows, key=lambda row: row['mean_progress_score'])['age_group']}.",
]
(BASE_DIR / "task2_report.txt").write_text("\n".join(report), encoding="utf-8")

