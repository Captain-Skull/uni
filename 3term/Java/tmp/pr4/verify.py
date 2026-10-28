from pathlib import Path
import subprocess
cp='tmp/pr4/classes'
checks=0
def run(cls,data='',expected=()):
 global checks
 p=subprocess.run(['java','-cp',cp,'org.example.pr4.app.'+cls],input=data,text=True,capture_output=True,check=True)
 for text in expected: assert text in p.stdout,(cls,data,text,p.stdout)
 checks+=1
 return p.stdout
print(run('TestTriangle','3 4 5\nred\ntrue\n',['Площадь: 6.0','Периметр: 12.0','Цвет: red','Заливка: true']))
for sides in ['1 2 3','1 3 2','3 1 2','-1 2 2','0 1 1','NaN 2 2','Infinity 2 2']:
 run('TestTriangle',sides+'\nred\nfalse\n',['Ошибка: Недопустимые стороны'])
run('TestTriangle','abc\n',['Ошибка ввода'])
run('TestTriangle','3 4 5\nblue\nabc\n',['Ошибка ввода'])
print(run('TestComparison',expected=['радиус = 3.0','ширина = 4.0','радиус = 4.0']))
s=run('TestColorable'); assert s.count('площадь =')==5 and s.count('Раскрасьте')==3;print(s)
for m,days in enumerate([31,28,31,30,31,30,31,31,30,31,30,31],1):
 run('MonthDaysBasic',f'{m}\n',[f'Количество дней: {days}'])
for cls in ['MonthDaysBasic','MonthDays']:
 for m in ['0','13','-1','2147483647','-2147483648']:
  run(cls,m+'\n',['Недопустимое число'])
 run(cls,'abc\n1.5\n3\n',['Допускается только целое число','Месяц: март','Количество дней: 31'])
for year,days in [(2024,29),(2025,28),(1900,28),(2000,29),(2100,28),(2400,29)]:
 run('MonthDays',f'2\n{year}\n',[f'Количество дней: {days}'])
run('MonthDays','2\nabc\n0\n-1\n2024\n',['Введите целый положительный год','Количество дней: 29'])
print('Console scenarios passed:',checks)
Path('tmp/pr4/checks.txt').write_text(f'javac -Xlint:all: no warnings\nConsole scenarios passed: {checks}\n',encoding='utf-8')
