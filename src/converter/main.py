"""Sample Use of the CSVConverter"""
from converter import CSVConverter

csv_converter = CSVConverter('books.csv')
csv_converter.convert_to_json('books.json')
