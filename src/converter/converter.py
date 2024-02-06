import pandas as pd
import json
import numpy as np

class CSVConverter:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def convert_to_json(self, output_file):
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(self.csv_file)
        
        # Clean column names (remove any leading/trailing whitespaces)
        df.columns = df.columns.str.strip()
        
        # Convert DataFrame to list of dictionaries (JSON-like structure)
        books = []
        for _, row in df.iterrows():
            book_dict = {
                "Titel": row["Titel"].strip(),
                "Autor": row["Autor"].strip(),
                "Veröffentlichungsjahr": str(row["Veröffentlichungsjahr"]).strip(),
                "Genre": row["Genre"].strip()
            }
            # Check for optional fields and include them if present and not NaN
            optional_fields = ["ISBN", "Bewertung"]
            for field in optional_fields:
                if field in df.columns and not pd.isnull(row[field]):
                    if field == "ISBN":
                        # Convert ISBN to string and strip leading/trailing spaces
                        book_dict[field] = str(row[field]).strip()
                    else:
                        # Strip leading/trailing spaces for other optional fields
                        book_dict[field] = str(row[field]).strip()
            books.append(book_dict)
        
        # Create JSON data
        json_data = {"Bücher": books}
        
        # Write JSON data to output file
        with open(output_file, 'w') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

# Example usage
if __name__ == "__main__":
    csv_converter = CSVConverter('books.csv')
    csv_converter.convert_to_json('books.json')
