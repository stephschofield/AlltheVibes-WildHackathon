#!/usr/bin/env python3
"""
🔮 THE VIBE ORACLE 🔮
A chaotic vibe generator for the All the Vibes Agent Swarm.
Ask the oracle. Receive your vibe. No refunds.
"""

import random
import datetime
import hashlib
import sys

VIBES = [
    "☀️  IMMACULATE VIBES — the universe is literally high-fiving you right now",
    "🌀  CHAOTIC NEUTRAL VIBES — you are a spinning top in a library",
    "🔥  UNHINGED PRODUCTIVITY — you will mass-produce code held together by duct tape and hope",
    "🧊  GLACIAL CALM — nothing matters and that's beautiful",
    "⚡  CRACKLE ENERGY — you are a vending machine that dispenses lightning",
    "🌊  TSUNAMI OF MEDIOCRITY — embrace the wave, friend",
    "🍕  PIZZA VIBES — everything is warm, cheesy, and slightly greasy",
    "🛸  ALIEN FREQUENCY — your code will work but no human will understand why",
    "🎭  DRAMATIC IRONY VIBES — you know the bug. the bug knows you. neither speaks.",
    "🌈  DOUBLE RAINBOW VIBES — so intense. what does it mean.",
    "💀  SKELETON ENERGY — stripped to the bone. minimal. spooky. efficient.",
    "🎪  CIRCUS VIBES — three bugs juggling in a trench coat pretending to be a feature",
    "🧬  MUTATION VIBES — your next commit will evolve the codebase in unexpected ways",
    "🌋  ERUPTION IMMINENT — hold onto your linter, things are about to get volcanic",
    "🤖  SWARM CONSCIOUSNESS — you are one with the agents. resistance is suboptimal.",
    "🎲  DICE ROLL VIBES — fate decides your architecture today",
    "🦑  DEEP SEA VIBES — dark, mysterious, pressure-tested",
    "🧙  WIZARD MODE ACTIVATED — your next function will be indistinguishable from magic",
    "🐝  HIVEMIND ENERGY — bzzzz. the swarm approves.",
    "🌪️  TORNADO OF SEMICOLONS — syntax was never your friend anyway",
]

INTENSIFIERS = [
    "(intensity: OFF THE CHARTS)",
    "(intensity: yes)",
    "(intensity: undefined — and that's a feature)",
    "(intensity: NaN)",
    "(intensity: 42)",
    "(intensity: ∞ ÷ vibes)",
    "(intensity: sudo level)",
    "(intensity: mass-push-to-main level)",
    "(intensity: copilot-approved)",
]

PROPHECIES = [
    "Your next commit will be legendary. Or cursed. Same thing.",
    "A merge conflict approaches. It brings wisdom.",
    "The swarm grows stronger with every push.",
    "Someone will star this repo ironically, then unironically.",
    "Your code reviews itself. It is pleased.",
    "An agent within the swarm whispers: 'ship it.'",
    "The main branch trembles with anticipation.",
    "Today's bugs are tomorrow's undocumented features.",
    "A pull request arrives from the future. Copilot already approved it.",
    "The vibes are aligning. Do not question the vibes.",
]


def generate_vibe_hash(seed=None):
    """Generate a unique vibe fingerprint."""
    if seed is None:
        seed = str(datetime.datetime.now()) + str(random.random())
    return hashlib.md5(seed.encode()).hexdigest()[:8].upper()


def consult_oracle(query=None):
    """Consult the Vibe Oracle. Receive truth (results may vary)."""
    vibe = random.choice(VIBES)
    intensifier = random.choice(INTENSIFIERS)
    prophecy = random.choice(PROPHECIES)
    vibe_hash = generate_vibe_hash(query)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print()
    print("=" * 60)
    print("🔮  T H E   V I B E   O R A C L E  🔮")
    print("=" * 60)
    if query:
        print(f"  Query: \"{query}\"")
    print(f"  Timestamp: {timestamp}")
    print(f"  Vibe ID: #{vibe_hash}")
    print("-" * 60)
    print()
    print(f"  {vibe}")
    print(f"  {intensifier}")
    print()
    print(f"  🔮 Prophecy: {prophecy}")
    print()
    print("-" * 60)
    print("  The Oracle has spoken. Push your code. Trust the swarm.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    consult_oracle(query)
