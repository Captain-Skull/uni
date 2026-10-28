from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from hashlib import sha256
from copy import deepcopy
from lxml import etree as E
import json

root=Path('/Users/georgemk/Projects/uni/3term/Java')
ref=Path('/Users/georgemk/Downloads/Работа3_Мкртчян.docx')
out=root/'output/Работа4_Мкртчян.docx'
out.parent.mkdir(exist_ok=True)
w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns={'w':w}
def el(name,**attrs):
 x=E.Element('{'+w+'}'+name)
 for k,v in attrs.items(): x.set('{'+w+'}'+k,str(v))
 return x
with ZipFile(ref) as z:
 parts={n:z.read(n) for n in z.namelist()}
doc=E.fromstring(parts['word/document.xml']);body=doc.find('w:body',ns)
section=deepcopy(body.find('w:sectPr',ns))
# Retain the original cover and its actual table, image, and run formatting.
for child in list(body)[6:]: body.remove(child)
for t in body[3].xpath('.//w:t',namespaces=ns):
 if t.text=='3': t.text='4'
for t in body[5].xpath('.//w:t',namespaces=ns):
 if t.text=='5': t.text='6'

def para(text,style=None,new_page=False,placeholder=False):
 p=el('p');pr=el('pPr');p.append(pr)
 if style: pr.append(el('pStyle',val=style))
 if new_page: pr.append(el('pageBreakBefore'))
 if placeholder:
  pr.append(el('shd',val='clear',fill='F2F2F2'))
  pr.append(el('spacing',before=120,after=160,line=280,lineRule='auto'))
  pr.append(el('keepLines'))
 else:
  pr.append(el('spacing',after=100))
 r=el('r');p.append(r)
 if placeholder:
  rp=el('rPr');r.append(rp);rp.append(el('i'));rp.append(el('color',val='666666'))
 t=el('t');t.text=text;r.append(t);body.append(p)

def shot(n,text): para(f'[Скриншот {n}: {text}]',placeholder=True)
def start(num,desc):
 para('Задача '+num,'1',new_page=True)
 para('Описание задачи, цель','2');para(desc)
 para('Ход работы','2')
def end(text):para('Результаты и выводы','2');para(text)

start('4.1.1','Создать класс Triangle, который наследуется от GeometricObject. Добавить три стороны со значениями по умолчанию 1.0, два конструктора, getter-методы, вычисление площади и периметра и метод toString(). Написать программу для ввода сторон, цвета и заливки. Цель: научиться создавать подклассы и использовать унаследованные свойства.')
para('Создаем пакет org.example.pr4. В классе GeometricObject определяем цвет color, заливку filled и дату создания dateCreated. Добавляем методы для чтения и изменения свойств.')
shot('1','GeometricObject.java — поля, конструкторы и методы доступа')
para('Создаем Triangle с полями side1, side2 и side3. Периметр находим как сумму сторон, площадь — по формуле Герона: s = (side1 + side2 + side3) / 2; area = √(s · (s − side1) · (s − side2) · (s − side3)). Метод toString() возвращает описание сторон.')
shot('2','Triangle.java — конструкторы, getArea(), getPerimeter() и toString()')
para('В TestTriangle вводим стороны 3, 4, 5, цвет red и заливку true. После создания объекта выводим его свойства. Получаем площадь 6.0 и периметр 12.0.')
shot('3','консоль TestTriangle — ввод 3 4 5, red, true и результат')
end('Создали треугольник и программу для работы с ним. Научились использовать наследование, конструкторы и методы доступа. В итоговом коде также учтены доработки из следующих заданий.')

start('4.1.2','Создать класс IllegalTriangleException. Изменить конструктор Triangle так, чтобы при нарушении неравенства треугольника выбрасывалось это исключение. Цель: научиться создавать и обрабатывать собственные исключения.')
para('Создаем класс IllegalTriangleException, который наследуется от Exception. В сообщение передаем значения сторон, при которых не удалось создать треугольник.')
shot('4','IllegalTriangleException.java — объявление класса и конструктор')
para('В конструкторе Triangle проверяем, что стороны положительные и сумма любых двух больше третьей. Если проверка не пройдена, выполняем throw new IllegalTriangleException(side1, side2, side3). В сигнатуру конструктора добавляем throws IllegalTriangleException.')
shot('5','Triangle.java — проверка сторон и выбрасывание исключения')
para('В TestTriangle оборачиваем создание объекта в try и обрабатываем исключение в catch. Для проверки вводим стороны 1, 2, 3, цвет red и false. Сумма первых двух сторон равна третьей, поэтому получаем сообщение об ошибке. Стороны 3, 4, 5 проходят проверку.')
shot('6','консоль TestTriangle — сообщение об ошибке для сторон 1 2 3')
end('Добавили проверку существования треугольника. Научились использовать throw, throws и try-catch. При неверных сторонах объект не создается, а программа выводит понятное сообщение.')

start('4.1.3','Сделать GeometricObject абстрактным классом, от которого наследуется Triangle. Реализовать Comparable и статический метод max(). Проверить сравнение двух кругов, двух прямоугольников, двух ComparableCircle, а также круга и прямоугольника. Цель: освоить абстрактные классы и сравнение объектов.')
para('Объявляем GeometricObject абстрактным, а getArea() и getPerimeter() — абстрактными методами. В Triangle, Circle и Rectangle задаем свои формулы. Ввод сторон, цвета и заливки проверяем через TestTriangle.')
shot('7','абстрактный GeometricObject и реализации методов в подклассах')
para('Добавляем Comparable<GeometricObject>. В compareTo() сравниваем площади с помощью Double.compare(). В max() возвращаем объект с большей площадью. При равенстве площадей возвращаем первый объект.')
shot('8','GeometricObject.java — compareTo() и max(); ComparableCircle.java')
para('ComparableCircle наследуется от Circle и получает Comparable через базовый класс. Его compareTo() принимает GeometricObject, поэтому позволяет сравнить круг с прямоугольником. Запускаем TestComparison.')
para('Для кругов с радиусами 2 и 3 выбирается радиус 3; для прямоугольников 3 × 4 и 4 × 5 — второй. Из ComparableCircle с радиусами 2 и 4 выбирается радиус 4. Между кругом радиуса 2 и прямоугольником 4 × 5 выбирается прямоугольник с площадью 20.0.')
shot('9','консоль TestComparison — результаты четырех сравнений')
end('Научились работать с абстрактными методами и интерфейсом Comparable. Реализовали единое сравнение фигур по площади и проверили max() и compareTo().')

start('4.1.4','Создать интерфейс Colorable с методом howToColor(). Класс Square должен наследоваться от GeometricObject и реализовывать Colorable. Создать массив из пяти фигур, вывести площадь каждой и вызвать howToColor(), если фигуру можно раскрасить. Цель: закрепить работу с интерфейсами и полиморфизмом.')
para('Создаем интерфейс Colorable с методом void howToColor(). В Square добавляем поле side, getter и setter, конструктор без параметров со стороной 0 и конструктор с указанной стороной.')
shot('10','Colorable.java и Square.java — поле, конструкторы и методы доступа')
para('Площадь квадрата вычисляем как side * side, периметр — как 4 * side. Метод howToColor() выводит сообщение «Раскрасьте все четыре стороны.».')
shot('11','Square.java — getArea(), getPerimeter() и howToColor()')
para('В TestColorable создаем массив GeometricObject[]: Square(2), Circle(3), Rectangle(3, 4), Square(5) и Square(). Для каждой фигуры выводим площадь. Через instanceof Colorable проверяем, можно ли вызвать howToColor().')
para('Получаем площади 4.0, примерно 28.2743, 12.0, 25.0 и 0.0. Сообщение о раскрашивании выводится для трех квадратов.')
shot('12','TestColorable.java и консоль — пять фигур и подсказки для квадратов')
end('Создали интерфейс и реализовали его в классе Square. Научились хранить разные фигуры в одном массиве и вызывать дополнительные методы после проверки типа.')

start('4.2.1','С помощью двух массивов написать программу, которая принимает целое число от 1 до 12 и выводит месяц и количество дней. Недопустимый номер обработать через ArrayIndexOutOfBoundsException. Предотвратить ввод значений, которые не являются целыми числами. Цель: научиться обрабатывать ошибки при работе с массивами и вводом.')
para('Создаем MonthDaysBasic. В массив months записываем названия месяцев, в массив dom — количество дней. В базовой версии для февраля используем 28 дней.')
shot('13','MonthDaysBasic.java — массивы months и dom')
para('Перед чтением номера проверяем scanner.hasNextInt(). Если введено слово или дробное число, пропускаем неверное значение через scanner.next() и предлагаем повторить ввод.')
shot('14','MonthDaysBasic.java — проверка целого числа и блок try-catch')
para('Обращаемся к массивам по индексу month - 1. Если номер выходит за диапазон, перехватываем ArrayIndexOutOfBoundsException и выводим «Недопустимое число». Проверяем номер 3: получаем март и 31 день. При вводе 13 выводится сообщение об ошибке. При вводе abc программа просит целое число.')
shot('15','консоль MonthDaysBasic — правильный номер, номер 13 и ввод abc')
end('Научились сопоставлять данные двух массивов и перехватывать выход за их границы. Добавили проверку типа ввода, чтобы программа не принимала дробные числа и текст вместо целого номера.')

start('4.2.2','Дополнить программу из предыдущего задания: при выборе февраля запросить год. Добавить метод для определения високосного года и изменить число дней в феврале. Цель: научиться выделять проверку в отдельный метод и использовать ее результат.')
para('Создаем расширенную версию MonthDays. После ввода номера месяца проверяем, выбран ли февраль. Только в этом случае дополнительно запрашиваем целый положительный год.')
shot('16','MonthDays.java — ввод месяца и запрос года для февраля')
para('Добавляем метод isLeapYear(int year). Год считается високосным, если делится на 400 или делится на 4, но не делится на 100. Условие: year % 400 == 0 || (year % 4 == 0 && year % 100 != 0).')
shot('17','MonthDays.java — isLeapYear() и выбор между 28 и 29 днями')
para('Если isLeapYear() возвращает true, задаем 29 дней, иначе 28. Проверяем февраль 2024 года: получаем 29 дней; 2025 года — 28. Отдельно проверяем 1900 год — 28 дней и 2000 год — 29 дней. Для остальных месяцев ввод года не требуется.')
shot('18','консоль MonthDays — февраль для 2024, 2025, 1900 и 2000 годов')
end('Добавили расчет високосного года и корректное количество дней в феврале. Научились выносить повторяемую проверку в отдельный метод и учитывать исключения из общего правила делимости на 4.')

body.append(section)
parts['word/document.xml']=E.tostring(doc,encoding='UTF-8',xml_declaration=True,standalone=True)
with ZipFile(out,'w',ZIP_DEFLATED) as z:
 for name,data in parts.items(): z.writestr(name,data)
with ZipFile(ref) as z,ZipFile(out) as q:
 changed=[n for n in z.namelist() if z.read(n)!=q.read(n)]
 assert changed==['word/document.xml'],changed
manifest={n:{'size':len(data),'sha256':sha256(data).hexdigest()} for n,data in parts.items()}
(root/'tmp/pr4/package-inventory.json').write_text(json.dumps(manifest,indent=2))
(root/'tmp/pr4/artifact.md').write_text(f'''# Reference contract\nReference: {ref}\nSHA256: {sha256(ref.read_bytes()).hexdigest()}\nReference rendered pages: 8; sections: 1. Render: reference/.\nA4 portrait; margins top/bottom 2 cm, left 3 cm, right 1.5 cm.\nNormal: Times New Roman 12 pt. Heading 1: source style 1, 16 pt bold. Heading 2: source style 2, 14 pt bold.\nCover: retain body children 0–5 including two tables, emblem, author, group and teacher. Editable slots: report number 3 to 4; city year 2025 to 2026.\nBody after child 5: replace with six task sections numbered 4.1.1–4.1.4 and 4.2.1–4.2.2. Roles: task Heading 1, description/work/results Heading 2, short Normal paragraphs, named screenshot slots. Each task starts on a fresh page. Source 1 section and section XML preserved.\nSource screenshots and task-specific body tables replaced by screenshot placeholders at user request. Placeholders: Normal, italic gray on F2F2F2, same 12 pt family.\nPackage: every part except word/document.xml is byte-identical to source, including relationships, styles, numbering, header/footer and media. Inventory: package-inventory.json. Original reference unchanged.\nFinal gates: all six tasks, eighteen screenshot slots, same cover identity, no old task body, seven clean pages, unchanged geometry and package parts.\n''',encoding='utf-8')
print(out)
