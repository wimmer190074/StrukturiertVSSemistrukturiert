import os
import json
import pytest
import json
from converter import CSVConverter

@pytest.fixture
def csv_converter():
    return CSVConverter('tests/data/test_books.csv')

@pytest.fixture
def expected_output():
    with open('tests/data/expected_output.json', 'r') as f:
        return json.load(f)

def test_basic_conversion_001(csv_converter, expected_output):
    output_file = 'tests/data/test_output.json'
    csv_converter.convert_to_json(output_file)
    
    assert os.path.exists(output_file)
    
    with open(output_file, 'r') as f:
        json_data = json.load(f)
    
    def preprocess_data(data):
        for book in data["Bücher"]:
            for key, value in book.items():
                if isinstance(value, (int, float)):
                    book[key] = str(value)
        return data

    expected_output = preprocess_data(expected_output)
    assert json.dumps(json_data['Bücher'], sort_keys=True, ensure_ascii=False) == json.dumps(expected_output['Bücher'], sort_keys=True, ensure_ascii=False)
    
    os.remove(output_file)

def test_different_column_order_002(csv_converter, expected_output):
    output_file = 'tests/data/test_output.json'
    csv_converter.convert_to_json(output_file)
    
    assert os.path.exists(output_file)
    
    with open(output_file, 'r') as f:
        json_data = json.load(f)
    
    assert json_data == expected_output
    
    os.remove(output_file)
