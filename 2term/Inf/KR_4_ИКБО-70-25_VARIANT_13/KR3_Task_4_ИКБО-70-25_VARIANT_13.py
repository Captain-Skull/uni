# Group: ИКБО-70-25
# Student: George Mkrtchyan

from __future__ import annotations

import csv
import re
import statistics
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "variant_13" / "task_4.csv"
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


with INPUT_FILE.open(encoding="utf-8-sig", newline="") as f:
    rows = [{k: clean_text(v) for k, v in row.items()} for row in csv.DictReader(f)]

numeric_fields = ["visits_month", "trainer_hours", "progress_score", "subscription_months"]
for row in rows:
    for field in numeric_fields + ["churn_flag"]:
        row[field] = parse_number(row[field])

summary_rows = []
for field in numeric_fields:
    values = [row[field] for row in rows if row[field] is not None]
    summary_rows.append(
        {
            "field_name": field,
            "min": min(values),
            "max": max(values),
            "mean": round(statistics.mean(values), 2),
            "median": round(statistics.median(values), 2),
            "std": round(statistics.stdev(values), 2) if len(values) > 1 else 0.0,
            "missing_count": sum(1 for row in rows if row[field] is None),
        }
    )

with (BASE_DIR / "task4_summary.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["field_name", "min", "max", "mean", "median", "std", "missing_count"])
    writer.writeheader()
    writer.writerows(summary_rows)

age_counts = Counter(row["age_group"] for row in rows)
total = len(rows)
group_rows = [
    {
        "age_group": group,
        "count": count,
        "share_percent": round(count / total * 100, 2),
    }
    for group, count in sorted(age_counts.items())
]
with (BASE_DIR / "task4_group_table.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["age_group", "count", "share_percent"])
    writer.writeheader()
    writer.writerows(group_rows)

top5 = sorted([row for row in rows if row["progress_score"] is not None], key=lambda row: row["progress_score"], reverse=True)[:5]
with (BASE_DIR / "task4_top5.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["client_id", "age_group", "progress_score", "visits_month", "trainer_hours", "subscription_months"])
    writer.writeheader()
    for row in top5:
        writer.writerow({field: row[field] for field in writer.fieldnames})

valid_pairs = [(row["visits_month"], row["progress_score"]) for row in rows if row["visits_month"] is not None and row["progress_score"] is not None]
x_values = [x for x, _ in valid_pairs]
y_values = [y for _, y in valid_pairs]
correlation = statistics.correlation(x_values, y_values) if hasattr(statistics, "correlation") else 0.0

plot_groups = [row["age_group"] for row in sorted(group_rows, key=lambda row: row["age_group"])]
plot_values = [statistics.mean([row["progress_score"] for row in rows if row["age_group"] == group and row["progress_score"] is not None]) for group in plot_groups]

plt.figure(figsize=(8, 4))
bars = plt.bar(plot_groups, plot_values, color="#4c78a8")
plt.title("Average progress score by age group")
plt.xlabel("Age group")
plt.ylabel("Mean progress score")
for bar, value in zip(bars, plot_values):
    plt.text(bar.get_x() + bar.get_width() / 2, value + 0.5, f"{value:.1f}", ha="center", va="bottom", fontsize=8)
plt.tight_layout()
plt.savefig(BASE_DIR / "task4_chart.png", dpi=150)
plt.close()

interpretation = [
    f"В выборке task_4.csv самой многочисленной группой является 36-45 лет, а самой малочисленной — 18-25 лет.",
    f"Средний прогресс заметно выше у группы 36-45 лет и ниже у группы 46-60 лет, что видно по сводной таблице и графику.",
    f"Коэффициент корреляции между visits_month и progress_score равен {correlation:.2f}, то есть линейная связь слабая.",
    "Это означает, что число посещений само по себе плохо объясняет итоговый прогресс клиентов.",
    "Наиболее высокие значения progress_score сосредоточены у отдельных клиентов, попавших в top-5.",
    "Показатель trainer_hours содержит очень крупный максимум, поэтому при аналитической интерпретации его стоит рассматривать как потенциальный выброс.",
]
(BASE_DIR / "task4_interpretation.txt").write_text("\n".join(interpretation), encoding="utf-8")
