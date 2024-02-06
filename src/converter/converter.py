"""Converts book.csv to json."""

import json
import pandas as pd

class CSVConverter:
    """Converts book.csv to json."""
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def convert_to_json(self, output_file):
        """Converts the files."""
        df = pd.read_csv(self.csv_file)

        df.columns = df.columns.str.strip()

        books = []
        for _, row in df.iterrows():
            book_dict = {
                "Titel": row["Titel"].strip(),
                "Autor": row["Autor"].strip(),
                "Veröffentlichungsjahr": str(row["Veröffentlichungsjahr"]).strip(),
                "Genre": row["Genre"].strip()
            }
            optional_fields = ["ISBN", "Bewertung"]
            for field in optional_fields:
                if field in df.columns and not pd.isnull(row[field]):
                    if field == "ISBN":
                        book_dict[field] = str(row[field]).strip()
                    else:
                        book_dict[field] = str(row[field]).strip()
            books.append(book_dict)

        json_data = {"Bücher": books}

        with open(output_file, 'w') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
