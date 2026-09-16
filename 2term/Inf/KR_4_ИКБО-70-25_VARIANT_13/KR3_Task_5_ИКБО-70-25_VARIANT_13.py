# Group: ИКБО-70-25
# Student: George Mkrtchyan

from __future__ import annotations

import csv
import re
from pathlib import Path

import statistics


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "variant_13" / "task_5.csv"

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
    raw_rows = [{k: clean_text(v) for k, v in row.items()} for row in csv.DictReader(f)]

rows = []
for row in raw_rows:
    visits = parse_number(row["visits_month"])
    progress = parse_number(row["progress_score"])
    subscription = parse_number(row["subscription_months"])
    churn = parse_number(row["churn_flag"])

    if visits is None or progress is None or subscription is None or churn is None:
        continue
    if subscription < 0:
        continue
    rows.append(
        {
            "client_id": row["client_id"],
            "visits_month": visits,
            "progress_score": progress,
            "subscription_months": subscription,
            "churn_flag": int(churn),
        }
    )

threshold_progress = 92.86
threshold_visits = 21.5
threshold_subscription = 7.5

predictions = []
correct = 0
for row in rows:
    if row["progress_score"] >= threshold_progress:
        predicted = 1
        branch = "high_progress"
    elif row["visits_month"] <= threshold_visits and row["subscription_months"] <= threshold_subscription:
        predicted = 1
        branch = "low_visits_short_subscription"
    else:
        predicted = 0
        branch = "regular_activity"
    correct += int(predicted == row["churn_flag"])
    predictions.append(
        {
            **row,
            "predicted_churn_flag": predicted,
            "decision_branch": branch,
        }
    )

accuracy = correct / len(rows) * 100 if rows else 0.0

with (BASE_DIR / "task5_predictions.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "client_id",
            "visits_month",
            "progress_score",
            "subscription_months",
            "churn_flag",
            "predicted_churn_flag",
            "decision_branch",
        ],
    )
    writer.writeheader()
    writer.writerows(predictions)

sample_rows = predictions[:10]
report = [
    "Метод: простое правило классификации по трём признакам.",
    "Правило: churn_flag=1, если progress_score >= 92.86; иначе churn_flag=1, если visits_month <= 21.5 и subscription_months <= 7.5; иначе churn_flag=0.",
    f"Использовано строк после очистки: {len(rows)}.",
    f"Accuracy: {accuracy:.2f}%.",
    "Сильнее всего влияет progress_score: очень высокий прогресс переводит объект в класс оттока.",
    "Вторая ветка правила показывает, что низкая активность и короткая подписка тоже указывают на churn.",
    "",
    "Сравнение фактического и прогнозного класса (первые 10 строк):",
]
for row in sample_rows:
    report.append(
        f"{row['client_id']}: факт={row['churn_flag']}, прогноз={row['predicted_churn_flag']}, "
        f"visits={row['visits_month']}, progress={row['progress_score']}, subscription={row['subscription_months']}."
    )
(BASE_DIR / "task5_model_report.txt").write_text("\n".join(report), encoding="utf-8")

