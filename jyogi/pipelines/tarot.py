from __future__ import annotations

from jyogi.clients.ai import chat
from jyogi.config import TAROT_PROMPT
from jyogi import tarot_deck


def generate_tarot_report(spread_id: str, user_q: str, client_name: str = "") -> dict:
    spread_data = tarot_deck.pull_spread(spread_id)
    spread_info = tarot_deck.spreads.get(spread_id, tarot_deck.spreads["1"])

    # Build card summary for AI
    # NOTE: client name is NEVER sent to OpenAI — only card positions and question
    card_summary = ""
    affirmations  = ""
    for item in spread_data:
        orientation = "Shadow Seer [Reversed]" if item["Reversed"] else "Light Seer [Upright]"
        card_summary += (
            f"{item['Position']}: {item['BaseName']} ({orientation})\n"
            f"  → {item['Meaning']}\n"
        )
        affirmations += f"• {item['BaseName']}: {item['Affirmation']}\n"

    # Only question + card positions sent to OpenAI — no name, no personal details
    user_msg = (
        f"Spread: {spread_info['name']}\n"
        f"Question: \"{user_q or 'General guidance'}\"\n\n"
        f"Cards drawn (Light Seer's Tarot by Chris-Anne):\n{card_summary}"
    )

    ai_answer = chat(TAROT_PROMPT, user_msg, temperature=0.55, max_tokens=450)

    # PDF still uses the real name locally — only the AI call is anonymised
    sections = [
        ("Reading Details", (
            f"Client   : {client_name}\n"
            f"Question : {user_q}\n"
            f"Spread   : {spread_info['name']}\n"
            f"Deck     : Light Seer's Tarot (Chris-Anne)"
        )),
        ("Cards Drawn", card_summary),
        ("Card Affirmations", affirmations),
        ("Jyogi's Interpretation", ai_answer),
    ]

    return {
        "spread_data":  spread_data,
        "spread_info":  spread_info,
        "card_summary": card_summary,
        "affirmations": affirmations,
        "ai_answer":    ai_answer,
        "sections":     sections,
    }
