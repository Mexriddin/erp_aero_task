from datetime import datetime
from typing import Dict
import fitz  # PyMuPDF


class Utils:

    @staticmethod
    def convert_pdf_to_dict(file: str) -> Dict[str, str]:
        data: Dict = {}
        # Open pdf file
        doc = fitz.open(file)
        # Load first page
        page = doc.load_page(0)
        # Extract text from page
        text = page.get_text()

        lines = text.strip().split("\n")
        # Remove the first line from the list and save in data
        data["Company name"] = lines.pop(0)
        for line in lines:
            if ":" in line:
                # If the line has ":" divide into two parts(key, value) and sava in dict
                key, value = line.split(":")
                for i in [".", "/"]:
                    if len(value.split(i)) == 3 and value.count(i) == 2:
                        value = Utils.parser_date(value, i)
                        break
                data[key.strip()] = value.strip()
            elif line.strip() == "":
                # If line empty continue loops
                continue
            else:
                # If value notes empty, add all line without ':'
                if data["NOTES"] == '':
                    data["NOTES"] = line.strip()
        return data

    @staticmethod
    def parser_date(date: str, ch) -> datetime.date:
        # convert data format from "dd.mm.yyyy" to "yyyy-mm-dd"
        p_date = "-".join(i.strip() for i in date.split(ch)[::-1])
        return p_date
