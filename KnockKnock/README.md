# 🚪 Knock Knock Joke Agent

An AI agent that responds to **everything** with knock-knock jokes!

## Setup

1. **Clone the repo** and `cd` into it.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and replace `sk-your-key-here` with your real key.

5. **Run the agent**:
   ```bash
   python knock_knock_agent.py
   ```

## Configuration

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | *(required)* | Your OpenAI API key |
| `OPENAI_MODEL` | `gpt-4o-mini` | Model to use for responses |

Set these in your `.env` file.

## Example

```
You: What is the capital of France?

🤡 Agent:
Knock knock!
(Who's there?)
Paris.
(Paris who?)
Paris is the capital of France — now lettuce in, it's cold out here! 🥶
```

## License

MIT
