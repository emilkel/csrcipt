import csv

def parse_csv(filepath: str) -> list:
	rows = []
	with open(filepath) as csv_file:
		rows = [r for r in csv.reader(csv_file)]

	return rows


def parse_format(filepath: str) -> dict:
	"""Парсит файл с форматом и возвращает словарь"""
	return {'fields': []}


def check_header(header: list, fields: dict) -> bool:
	"""Проверяет, соответствует ли header формату"""
	return True


def check_nullable(row: list, fields: dict) -> bool:
	"""Проверяет, что пропущены только допустимые поля"""
	return True


def check_types(row: list, fields: dict) -> bool:
	"""Проверяет, что типы полей в строке соответствует полям в формате"""
	return True


def correct_row(row: list, fields: dict) -> bool:
	return check_nullable(row, fields) and check_types(row, fields)


def main():
	all_rows = parse_csv("gett.csv")
	
	header = all_rows[0]
	rows = all_rows[1:]

	f = parse_format("gett.json")

	if not check_header(header, f['fields']):
		print("Wrong header!")
		return

	correct_rows = [r for r in rows if correct_row(r, f['fields'])]
	incorrect_rows = [r for r in rows if not correct_row(r, f['fields'])]

	print(correct_rows)
	print(incorrect_rows)


if __name__ == '__main__':
	main()