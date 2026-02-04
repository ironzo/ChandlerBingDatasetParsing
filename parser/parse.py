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
def find_THE_lines(text, character="Chandler", prior_amount=3):
    "Returns pairs of context and response as flat dictionaries"
    pairs = []
    text_lines = text.split("\n")
    for i in range(len(text_lines)):
        if text_lines[i].startswith(f"{character}: "):
            start_idx = max(0, i - prior_amount)
            prior_context = " ".join([line.strip() for line in text_lines[start_idx:i]])
            entry = {
                "context": prior_context,
                "response": text_lines[i].replace(f"{character}:", "").strip()
            }
            pairs.append(entry)
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