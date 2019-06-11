import math
from sys import argv

diction = {}
a, b, c, acc = 0, 0, 0, 0

def tester(func, exp, emsg, *ops):
	global diction
	try:
		assert func(*ops) == exp, emsg
	except AssertionError:
		if diction == {}:
			diction.update({"fname": func})
		if diction.get('fname') == func:
			diction.update({ops: (exp, emsg)})

def casestester(a):
			for i in a:
				tester(*i)
			if diction != {}:
				a = list(diction.keys())[1::]
				print(f"\nДля функции {diction.get('fname').__name__} при {len(mda)} тестах {len(a)} ошибок:\n")
				for i in a:
					print(f"Тестовые значения - {i}, ожидаемый результат - {diction.get(i)[0]}, полученные значения - {diction.get('fname')(*i)},текст - {diction.get(i)[1]}\n")

def inp():
	global a
	global b
	global c
	global acc
	a = input("Введите a: ")
	b = input("Введите b: ")
	c = input("Введите c: ")
	print("Введите точность (в виде float через точку)")
	acc = input("(или просто нажмите Enter если нечего вводить): ")
	if acc == '':
		acc = 0.0001


def solvekv(a, b, c, acc=0.0001):
	x1 , x2 = None, None
	disc = float(b ** 2 - 4 * a * c)
	if a == 0:
		return "Вычислить x не представляется возможным (a = 0)"
	if disc >= 0 :
		x1 = (-b - math.sqrt(disc))/(2 * a)
		x2 = (-b + math.sqrt(disc))/(2 * a)
	else:
		return('Дискриминант меньше нуля')
	return (round(x1, len(str(acc))-2),round(x2, len(str(acc))-2))

mda = [(solvekv, (3.0, 3.0), "Проблема с отрицательными числами", -1,3,0), (solvekv, (0.0, 1.0), "Что-то неверно", 1,0,0), (solvekv, (1.7, -1.7), "Проблема с нулевым b", -1,0,3,0.1),(solvekv, "Дискриминант меньше нуля", "Ошибка в реакции на отрицательный дискриминант", 1,1,2), (solvekv, "Вычислить x не представляется возможным (a = 0)", "Ошибка реакции на нулевой a", 0,3,0)]

if len(argv) == 1:
	inp()
	print(solvekv(int(a),int(b),int(c),float(acc)))
if len(argv) > 1:
	if argv[1] == 'test':
		mda1 = [argv[2], argv[3], argv[4], argv[5], argv[6]]
		mda = [[solvekv, "Вычислить x не представляется возможным (a = 0)", "test", 0, 0, 0]]
		for i in mda1:
			if 'exp' in i:
				mda[0][1] = (float(i[5:7:]), float(i[10:12:]))
			elif i[0] == 'a':
				mda[0][3] = int(i[2::])
			elif i[0] == 'b':
				mda[0][4] = int(i[2::])
			elif i[0] == 'c':
				mda[0][5] = int(i[2::])
			elif 'emsg' in i:
				mda[0][2] = i[5::]
		casestester(mda)


if __name__ == '__main__':
	assert solvekv(1,0,0) == (0.0, 0.0), "Что-то неверно"
	assert solvekv(-1,3,0) == (3.0, 0.0), "Проблема с отрицательными числами"
	assert solvekv(-1,0,3,0.1) == (1.7, -1.7), "Проблема с нулевым b"
	assert solvekv(1,1,2) == 'Дискриминант меньше нуля', "Ошибка в реакции на отрицательный дискриминант"
	assert solvekv(0,5,2) == "Вычислить x не представляется возможным (a = 0)", "Ошибка реакции на нулевой a"
