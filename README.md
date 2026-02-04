# Friends Script Dataset - Chandler Bing Lines

A dataset of Chandler Bing's dialogue lines from the TV show "Friends" (all 10 seasons), extracted from the complete script PDF. Each entry includes contextual prior dialogue, making it suitable for training conversational AI models or studying Chandler's iconic comedic timing and wit.

## Dataset Overview

- **Source**: Friends TV Show Scripts (All 10 Seasons)
- **Character**: Chandler Bing
- **Format**: JSONL (JSON Lines)
- **Total Lines**: 7,697 dialogue entries
- **Context**: Each line includes 3 preceding dialogue lines for context

## Data Format

Each line in `ChandlerBINGLines.jsonl` is a flat JSON object:

```json
{"context": "Prior dialogue joined as a single string", "response": "Chandler's response"}
```

| Field | Description |
|-------|-------------|
| `context` | Up to 3 preceding dialogue lines joined into a single string |
| `response` | Chandler's response (without the "Chandler:" prefix) |

## Examples

### Example 1: Classic Chandler Sarcasm
```json
{"context": "Monica: There's nothing to tell! He's just some guy I work with! Joey: C'mon, you're going out with the guy! There's gotta be something wrong with him!", "response": "All right Joey, be nice. So does he have a hump? A hump and a hairpiece?"}
```

### Example 2: Deadpan Humor
```json
{"context": "Monica: Are you okay, sweetie? Ross: I just feel like someone reached down my throat, grabbed my small intestine, pulled it out of my mouth and tied it around my neck...", "response": "Cookie?"}
```

### Example 3: Self-Deprecating Wit
```json
{"context": "Joey: And you never knew she was a lesbian... Ross: No!! Okay?! Why does everyone keep fixating on that? She didn't know, how should I know?", "response": "Sometimes I wish I was a lesbian... (They all stare at him.) Did I say that out loud?"}
```

### Example 4: Quick Comeback
```json
{"context": "Joey: Strip joint! C'mon, you're single! Have some hormones! Ross: I don't want to be single, okay? I just... I just- I just wanna be married again! (Rachel enters in a wet wedding dress and starts to search the room.)", "response": "And I just want a million dollars! (He extends his hand hopefully.)"}
```

### Example 5: Observational Humor
```json
{"context": "Rachel: Isn't this amazing? I mean, I have never made coffee before in my entire life.", "response": "That is amazing."}
```

## Usage

### Loading the Dataset (Python)

```python
import json

# Load all lines
with open("ChandlerBINGLines.jsonl", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

# Access individual entries
for entry in data[:5]:
    context = entry["context"]
    response = entry["response"]
    print(f"Context: {context}")
    print(f"Chandler: {response}\n")
```

### Regenerating the Dataset

If you want to regenerate the dataset from the source PDF:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with the path to the PDF:
   ```
   PDF_PATH=Friends_Script_All_Ten_Season.pdf
   ```

3. Run the parser:
   ```bash
   python parser/parse.py
   ```

## Project Structure

```
FriendsScript/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── ChandlerBINGLines.jsonl      # The dataset
├── Friends_Script_All_Ten_Season.pdf  # Source PDF
└── parser/
    ├── __init__.py
    └── parse.py                 # Parser script
```

## Potential Use Cases

- **Conversational AI**: Train chatbots with Chandler's comedic style
- **NLP Research**: Study humor patterns, sarcasm detection, or dialogue generation
- **Fine-tuning LLMs**: Create a Chandler-style response generator
- **Text Analysis**: Analyze comedic timing and response patterns

## Notes

- Some lines may contain stage directions in parentheses (e.g., `(deadpan)`, `(sarcastically)`)
- Scene descriptions are included in `[brackets]`
- The prior context helps understand the setup for Chandler's punchlines

## License

This dataset is created for educational and research purposes. Friends is owned by Warner Bros. Television.
