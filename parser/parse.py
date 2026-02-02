# IMPORTS
import pymupdf as parser
import os
from dotenv import load_dotenv
from pathlib import Path
import json

# CONSTANTS
load_dotenv()
pdf_dir = Path(os.getenv("PDF_PATH"))

# HELPER FUNCTIONS
def find_THE_lines(text, character="Chandler", prior_amount = 3):
    "Returns pairs"
    pairs = []
    text_lines = text.split("\n")
    for i in range(len(text_lines)):
        if text_lines[i].startswith(f"{character}: "):
            character_line = text_lines[i]
            prior_lines = [text_lines[i-prior] for prior in range(prior_amount,0, -1) if i-prior >=0]
            pairs.append(({"prior": prior_lines}, {"character_line":character_line}))
    return pairs

# PUBLIC FUNCTIONS
def parse(file_path):
    "Parse Chandler's Lines (answer) and Line before it (question)"
    doc = parser.open(file_path)
    data = []
    for page in doc:
        text = page.get_text()
        data.extend(find_THE_lines(text))
    return data

if __name__ == "__main__":
    parsed_lines = parse(pdf_dir)
    filename = "ChandlerBINGLines.jsonl"
    with open(filename, "w", encoding="utf-8") as f:
        for line in parsed_lines:
            f.write(json.dumps(line) + "\n")