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

def main():
	rows = parse_csv("gett.csv")
	f = parse_format("gett.json")

	if not check_header:
		print("Wrong header!")
		return

	correct_rows = [r for r in rows if check_nullable(r, f['fields']) and check_types(r, f['fields'])]
	incorrect_rows = [r for r in rows if not check_nullable(r, f['fields']) or not check_types(r, f['fields'])]


if __name__ == '__main__':
	main()