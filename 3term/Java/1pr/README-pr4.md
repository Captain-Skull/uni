# Практическая работа 4

Код находится в `src/main/java/org/example/pr4`. В `geometry` расположены классы фигур, в `app` — программы для запуска.

Это итоговая версия после всех доработок: `GeometricObject` абстрактный (задание 3), конструктор `Triangle` проверяет стороны и выбрасывает `IllegalTriangleException` (задание 2). `TestTriangle` используется для заданий 1–3.

## Запуск в IntelliJ IDEA

Открой проект `1pr` и запускай нужный класс через зелёную кнопку возле `main`.

| Задание | Класс | Что вводить |
| --- | --- | --- |
| 4.1.1–4.1.3 | `TestTriangle` | Стороны `3 4 5`, затем цвет `red`, затем `true` (каждый шаг с новой строки) |
| 4.1.2 | `TestTriangle` | Стороны `1 2 3`, цвет `red`, заливка `false`: сообщение об исключении |
| 4.1.3 | `TestComparison` | Ввод не требуется |
| 4.1.4 | `TestColorable` | Ввод не требуется |
| 4.2.1 | `MonthDaysBasic` | Номер месяца: `1`, `12`; ошибки: `0`, `13`; проверка типа: `abc`, затем `3` |
| 4.2.2 | `MonthDays` | Месяц `2`, затем год `2024`, `2025`, `1900` или `2000` |

Дробные стороны вводятся через точку. Сравнение фигур выполняется по площади. `ComparableCircle` наследует `Comparable<GeometricObject>` через `Circle`, поэтому сравнивает и круги, и прямоугольники.

## Запуск без Maven

Для новых файлов достаточно JDK 17 или новее, дополнительных библиотек нет. В терминале из папки `1pr`:

```sh
mkdir -p out-pr4
javac -encoding UTF-8 -d out-pr4 src/main/java/org/example/pr4/geometry/*.java src/main/java/org/example/pr4/app/*.java
java -cp out-pr4 org.example.pr4.app.TestTriangle
java -cp out-pr4 org.example.pr4.app.TestComparison
java -cp out-pr4 org.example.pr4.app.TestColorable
java -cp out-pr4 org.example.pr4.app.MonthDaysBasic
java -cp out-pr4 org.example.pr4.app.MonthDays
```

В существующем `pom.xml` указан JDK 25 для всего проекта. Команды выше компилируют только четвёртую практику и работают на JDK 17.

В отчёте оставлены подписанные места для скриншотов кода и консоли. Замени текст в квадратных скобках своими снимками из IDE.
