# OSRS Minions

A Personal OSRS bot and/or helper that assists you in leveling up your in-game skills.

## Setting Up Python and Virtual Environment

### Clone the Repository

1. Open a terminal and navigate to the directory where you want to clone the project.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/hraza01/osrs_minions.git
   ```
3. Navigate into the project directory:
   ```bash
   cd osrs_minions
   ```

### Python Version

Ensure you have Python 3.10.2 installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Virtual Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the bot, use the following example command:

### Getting Cursor Position

Use the `--track` flag to enable live coordinate tracking mode:

```bash
python main.py --track
```

<br/>

Once you have your coordinates then start the bot:

```bash
python main.py -b magic
```

- Replace `magic` with the desired bot type (e.g., `thieving`, `woodcutting`, `agility`).
- You can provide arguments for primary and secondary coordinates using `-p <x1> <y1>` and `-s <x2> <y2>` flags.

### Example

```bash
python main.py -b magic -p 100 200 -s 300 400
```
