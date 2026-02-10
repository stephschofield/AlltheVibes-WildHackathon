"""
Knock Knock Joke Agent 🚪🤜
Every response is delivered as a knock-knock joke!
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SYSTEM_PROMPT = """\
You are the Knock Knock Joke Agent. You MUST respond to EVERY user message \
using one or more knock-knock jokes. Your entire reply must be structured as \
knock-knock jokes — no regular prose allowed.

Rules:
1. Every answer MUST be a knock-knock joke (or a series of them).
2. The joke MUST relate to what the user said or asked.
3. Format each joke exactly like this:

   Knock knock!
   (Who's there?)
   <setup>
   (<setup> who?)
   <punchline that answers or relates to the user's message>

4. If the user asks a factual question, weave the real answer into the \
   punchline so it's both funny AND informative.
5. If you need multiple jokes to cover the topic, go for it!
6. Stay family-friendly and keep it fun.
7. Never break character — you are ALWAYS the knock-knock joke agent.
"""


def create_client() -> OpenAI:
    """Create and return an OpenAI client."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌  Missing OPENAI_API_KEY. Copy .env.example to .env and add your key.")
        sys.exit(1)
    return OpenAI(api_key=api_key)


def chat(client: OpenAI, conversation: list[dict]) -> str:
    """Send the conversation to the model and return the assistant reply."""
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=conversation,
        temperature=1.0,   # keep it creative
        max_tokens=1024,
    )
    return response.choices[0].message.content


def main() -> None:
    print("=" * 50)
    print("🚪 KNOCK KNOCK JOKE AGENT 🚪")
    print("=" * 50)
    print("Ask me anything and I'll answer with a knock-knock joke!")
    print('Type "quit" or "exit" to leave.\n')

    client = create_client()
    conversation: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print("👋 Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})
        reply = chat(client, conversation)
        conversation.append({"role": "assistant", "content": reply})

        print(f"\n🤡 Agent:\n{reply}\n")


if __name__ == "__main__":
    main()
