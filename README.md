# Text2SQL

A natural language to SQL query conversion tool built with LangChain and OpenAI.

## Description

Text2SQL is a tool that allows users to query a database using natural language. It uses LangChain with OpenAI's language models to convert plain English questions into SQL queries, execute them against a database, and return the results.

## Features

- Convert natural language queries to SQL
- Execute SQL queries against a SQLite database
- Simple API for integrating into applications

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/text2sql.git
cd text2sql
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install langchain langchain-openai langchain-community python-dotenv
```

4. Set up environment variables
Create a `.env` file in the root directory with the following content:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Ensure your database is set up in the `db/` directory
2. Run the main script:
```bash
python main.py
```

3. Modify the query in `main.py` to ask different questions about your data

## Example

```python
# Define a natural language query
query = "List all users who signed up in the past 7 days."

# Run the agent to convert text to SQL and execute
result = agent_executor.invoke(query)

# Output the result
print(result)
```

## Project Structure

```
text2sql/
├── .venv/              # Virtual environment
├── db/                 # Database files
│   └── users.db        # SQLite database
├── .env                # Environment variables (not tracked in git)
├── .gitignore          # Git ignore file
├── main.py             # Main application file
└── README.md           # This file
```

## Requirements

- Python 3.9+
- OpenAI API key
- LangChain
- SQLite database

## License

[MIT](LICENSE) 