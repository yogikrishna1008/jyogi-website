"""
Jyogi — Pure Vedic Interpretation Engine
All text generated from classical rules — ZERO AI calls.
Sources: Parasara Hora Shastra, Brihat Jataka, traditional Jyotish.
"""

# ── Lagna interpretations ────────────────────────────────────────────────────
LAGNA_DATA = {
    "Aries": {
        "nature": "Cardinal Fire — ruled by Mars (Mangala)",
        "body": "Medium height, athletic build, prominent forehead, sharp eyes, reddish complexion.",
        "personality": "Natural leader with fierce determination. Bold, energetic, and pioneering. You charge ahead where others hesitate. Impatient by nature but your courage inspires those around you.",
        "strengths": "Courage, initiative, directness, physical vitality, leadership ability.",
        "challenges": "Impulsiveness, short temper, tendency to start projects without completing them.",
        "life_path": "You are born to initiate, compete, and conquer. Career in leadership, military, sports, surgery, or entrepreneurship suits your nature.",
        "upaya": "Upaya: Worship Lord Hanuman on Tuesdays. Chant 'Om Angarakaya Namaha' 108 times. Wear Red Coral (Moonga) in gold on the ring finger.",
    },
    "Taurus": {
        "nature": "Fixed Earth — ruled by Venus (Shukra)",
        "body": "Stocky, well-built frame. Thick neck, large eyes, pleasant face, melodious voice.",
        "personality": "Patient, reliable, and deeply sensual. You value comfort, beauty, and stability above all. Exceptionally persistent — once your mind is set, nothing moves you.",
        "strengths": "Patience, loyalty, artistic talent, financial acumen, sensory refinement.",
        "challenges": "Stubbornness, possessiveness, resistance to change, overindulgence in pleasures.",
        "life_path": "You thrive in fields of art, music, finance, agriculture, luxury goods, or any work requiring steady persistence.",
        "upaya": "Upaya: Worship Goddess Lakshmi on Fridays. Donate white sweets. Wear Diamond or White Sapphire in silver on the middle finger.",
    },
    "Gemini": {
        "nature": "Mutable Air — ruled by Mercury (Budha)",
        "body": "Tall, slender build. Quick, expressive eyes. Nimble hands. Youthful appearance throughout life.",
        "personality": "Brilliant communicator with an insatiable curiosity. You can see all sides of every question. Witty, adaptable, and intellectually restless — your mind is always racing.",
        "strengths": "Communication, adaptability, quick learning, networking, wit.",
        "challenges": "Inconsistency, scattered focus, nervousness, difficulty with commitment.",
        "life_path": "Writing, teaching, media, commerce, technology, and all forms of communication are your natural domains.",
        "upaya": "Upaya: Worship Lord Vishnu on Wednesdays. Feed green fodder to cows. Wear Emerald (Panna) in gold on the little finger.",
    },
    "Cancer": {
        "nature": "Cardinal Water — ruled by Moon (Chandra)",
        "body": "Round face, prominent chest, short to medium height, soft eyes, pale complexion.",
        "personality": "Deeply intuitive, nurturing, and emotionally perceptive. You feel everything intensely. Your home and family are your sacred space. Powerfully imaginative with an extraordinary memory.",
        "strengths": "Empathy, nurturing instinct, intuition, loyalty, creative imagination.",
        "challenges": "Moodiness, over-sensitivity, clinging to the past, indirect communication.",
        "life_path": "Healthcare, psychology, hospitality, real estate, food industry, or any nurturing profession fulfils your soul.",
        "upaya": "Upaya: Worship Lord Shiva on Mondays. Offer milk to Shivlinga. Wear Natural Pearl (Moti) in silver on the little finger.",
    },
    "Leo": {
        "nature": "Fixed Fire — ruled by Sun (Surya)",
        "body": "Majestic bearing, broad shoulders, abundant hair, commanding presence, bright eyes.",
        "personality": "Regal, generous, and magnetically charismatic. You were born to lead and to shine. Fiercely proud with a great sense of dignity. Your warmth draws people to you like sunlight.",
        "strengths": "Leadership, generosity, creative expression, dignity, loyalty to loved ones.",
        "challenges": "Pride, need for admiration, authoritarianism, difficulty accepting criticism.",
        "life_path": "Politics, entertainment, administration, medicine, or any stage that demands authority and presence.",
        "upaya": "Upaya: Worship Surya (Sun) at sunrise daily. Offer water mixed with red flowers to the Sun. Wear Ruby (Manikya) in gold on the ring finger.",
    },
    "Virgo": {
        "nature": "Mutable Earth — ruled by Mercury (Budha)",
        "body": "Slender, well-proportioned. Thoughtful eyes, sharp features, graceful walk.",
        "personality": "Analytical, precise, and service-oriented. Your mind is a perfect instrument for discernment. You notice what others miss. Deeply devoted to health, improvement, and helping others.",
        "strengths": "Analytical skill, attention to detail, service orientation, health consciousness, craftsmanship.",
        "challenges": "Over-criticism (of self and others), worry, perfectionism that causes paralysis.",
        "life_path": "Medicine, accounting, research, editing, nutrition, or any field requiring precision and analysis.",
        "upaya": "Upaya: Worship Lord Vishnu on Wednesdays. Keep green plants at home. Wear Emerald (Panna) in gold on the little finger.",
    },
    "Libra": {
        "nature": "Cardinal Air — ruled by Venus (Shukra)",
        "body": "Symmetrical, attractive features. Charming smile, graceful movement, elegant appearance.",
        "personality": "Diplomatic, fair-minded, and deeply relationship-oriented. You have a natural gift for creating harmony. Drawn to beauty in all its forms. A true partner who brings balance wherever you go.",
        "strengths": "Diplomacy, aesthetic sensibility, fairness, social grace, partnership ability.",
        "challenges": "Indecisiveness, people-pleasing, avoidance of conflict, dependency on others' approval.",
        "life_path": "Law, diplomacy, design, fashion, counselling, or any field requiring balance and aesthetic judgment.",
        "upaya": "Upaya: Worship Goddess Lakshmi on Fridays. Donate white clothes. Wear Diamond or White Sapphire in silver on the middle finger.",
    },
    "Scorpio": {
        "nature": "Fixed Water — ruled by Mars (Mangala)",
        "body": "Medium height, magnetic eyes, well-built, commanding presence. Often a memorable face.",
        "personality": "Intensely perceptive, deeply passionate, and psychically gifted. You see through every mask. Transformation is your life theme. Your will is iron, your loyalty absolute — and your enmity equally fierce.",
        "strengths": "Depth of insight, willpower, investigative ability, resilience, transformative power.",
        "challenges": "Jealousy, secretiveness, vindictiveness, power struggles, difficulty trusting.",
        "life_path": "Research, occult sciences, psychology, surgery, intelligence work, or anything involving deep investigation.",
        "upaya": "Upaya: Worship Lord Hanuman on Tuesdays. Offer sindoor and oil to Hanuman. Wear Red Coral (Moonga) in gold on the ring finger.",
    },
    "Sagittarius": {
        "nature": "Mutable Fire — ruled by Jupiter (Brihaspati)",
        "body": "Tall, athletic, expansive gestures. Open face, cheerful expression, strong thighs.",
        "personality": "Philosophical, freedom-loving, and optimistic to the core. You seek truth across cultures, religions, and continents. Your enthusiasm is infectious. Born explorer — of lands, ideas, and consciousness.",
        "strengths": "Optimism, philosophical depth, teaching ability, adventurousness, generosity.",
        "challenges": "Tactlessness, overconfidence, restlessness, difficulty with commitment, preaching.",
        "life_path": "Teaching, philosophy, publishing, law, travel, foreign affairs, or spiritual guidance.",
        "upaya": "Upaya: Worship Lord Vishnu on Thursdays. Feed Brahmins or the poor. Wear Yellow Sapphire (Pukhraj) in gold on the index finger.",
    },
    "Capricorn": {
        "nature": "Cardinal Earth — ruled by Saturn (Shani)",
        "body": "Lean, bony frame. Serious expression, dark features, prominent knees, slow deliberate movement.",
        "personality": "Disciplined, ambitious, and endlessly patient. You understand that true success is built slowly, brick by brick. Deeply responsible — others rely on you. Your early life may be harder, but you age like fine gold.",
        "strengths": "Discipline, ambition, organizational skill, patience, reliability.",
        "challenges": "Excessive caution, pessimism, coldness, overwork, difficulty expressing emotion.",
        "life_path": "Business, government, engineering, mining, real estate, or any field requiring long-term building.",
        "upaya": "Upaya: Worship Lord Shani on Saturdays. Light mustard oil lamp under Peepal tree. Wear Blue Sapphire (Neelam) in silver on the middle finger — only after trial period.",
    },
    "Aquarius": {
        "nature": "Fixed Air — ruled by Saturn (Shani)",
        "body": "Tall, well-proportioned. Broad forehead, prominent calves, unusual or striking appearance.",
        "personality": "Visionary, humanitarian, and brilliantly unconventional. You think decades ahead of your time. Deep concern for collective welfare. Your friendships are sacred to you — yet you need immense inner freedom.",
        "strengths": "Original thinking, humanitarian vision, friendship, innovation, intellectual independence.",
        "challenges": "Emotional detachment, stubbornness in beliefs, unpredictability, eccentricity.",
        "life_path": "Technology, social reform, science, aviation, astrology, or any field that serves humanity at large.",
        "upaya": "Upaya: Worship Lord Shani on Saturdays. Serve the underprivileged. Wear Blue Sapphire (Neelam) in silver — only after careful trial.",
    },
    "Pisces": {
        "nature": "Mutable Water — ruled by Jupiter (Brihaspati)",
        "body": "Medium height, soft eyes, fluid graceful movement, often dreamy or ethereal appearance.",
        "personality": "Compassionate, mystical, and deeply empathic. You feel the pain of others as your own. Extraordinarily creative and spiritually gifted. The boundary between you and the divine is thin.",
        "strengths": "Compassion, spiritual intuition, creativity, healing ability, unconditional love.",
        "challenges": "Over-sensitivity, escapism, lack of boundaries, self-sacrifice to the point of self-destruction.",
        "life_path": "Healing arts, spiritual guidance, music, film, charity work, or any field requiring deep empathy.",
        "upaya": "Upaya: Worship Lord Vishnu on Thursdays. Offer yellow flowers at temple. Wear Yellow Sapphire (Pukhraj) in gold on the index finger.",
    },
}

# ── Mahadasha interpretations ────────────────────────────────────────────────
DASHA_DATA = {
    "Sun": {
        "duration": "6 years",
        "nature": "Authoritative, government, father, soul, vitality",
        "themes": "This is a period of self-assertion and rising authority. Your individuality comes to the forefront. Government matters, career advancement, and relationship with authority figures are highlighted. Questions of ego, power, and recognition define these years.",
        "positive": "Career recognition, government favours, health improvement, self-confidence, leadership opportunities, support from father figures.",
        "challenges": "Ego conflicts, eye and heart health concerns, strained relationship with father, arrogance, excessive pride.",
        "spiritual": "A time for developing soul-consciousness. Surya Sadhana, Gayatri Mantra, and acts of righteous leadership align you with the highest Sun energy.",
        "upayas": [
            "Offer water to the rising Sun every morning — face East, hold copper vessel, chant Gayatri Mantra 3 or 108 times.",
            "Worship Lord Ram on Sundays. Donate wheat, jaggery, or copper to the needy.",
        ],
    },
    "Moon": {
        "duration": "10 years",
        "nature": "Mind, mother, emotions, public, travel, water",
        "themes": "The inner world becomes as important as the outer. Emotions run deep and the mind is highly receptive. This is a period of nurturing, connection, and public interaction. Your relationship with your mother and feminine figures is significant.",
        "positive": "Emotional richness, strong intuition, public popularity, business success, travel, connection with water and nature.",
        "challenges": "Mental fluctuations, anxiety, over-sensitivity, health issues related to lungs or fluids, mother's health concerns.",
        "spiritual": "Chandra energy rewards stillness, receptivity, and devotion. Worship on Mondays, moon gazing, and working with water are powerfully beneficial.",
        "upayas": [
            "Offer milk mixed with water to a Shivlinga on Mondays. Chant 'Om Chandraya Namaha' 108 times.",
            "Wear natural Pearl (Moti) set in silver. Keep fast on Mondays or Purnima (Full Moon).",
        ],
    },
    "Mars": {
        "duration": "7 years",
        "nature": "Energy, courage, siblings, property, conflict",
        "themes": "A period of intense energy, action, and potential conflict. Physical vitality is high. Property matters, legal disputes, and relationships with siblings come into focus. Your will and courage are tested — and strengthened.",
        "positive": "Physical energy, courage, athletic achievement, property gains, ability to overcome obstacles, protection from enemies.",
        "challenges": "Accidents, surgeries, blood disorders, anger issues, conflicts with siblings, property disputes, impulsive decisions.",
        "spiritual": "Channel Mars energy through disciplined physical practice, protection of the vulnerable, and righteous action (Dharma Yudha).",
        "upayas": [
            "Visit Hanuman temple on Tuesdays. Offer sindoor and jasmine oil. Chant Hanuman Chalisa.",
            "Wear Red Coral (Moonga) in gold. Donate red lentils (masoor dal) and jaggery on Tuesdays.",
        ],
    },
    "Rahu": {
        "duration": "18 years",
        "nature": "Illusion, foreign, technology, obsession, karmic amplifier",
        "themes": "Rahu Mahadasha is the great amplifier — it intensifies everything it touches. Foreign connections, unconventional paths, and sudden unexpected events characterise this period. Material desires run strong. This is often a period of great worldly achievement — and inner restlessness.",
        "positive": "Sudden rise in status, foreign opportunities, technological success, material gains, breaking of limitations, out-of-the-box success.",
        "challenges": "Confusion about identity, deception, hidden enemies, mental restlessness, health issues like allergies or nervous disorders, karmic debts surfacing.",
        "spiritual": "Rahu teaches through illusion — ultimately pushing you toward authentic spiritual search. Regular Rahu Shanti puja and ancestor worship (Pitru Tarpan) are essential.",
        "upayas": [
            "Worship Goddess Durga or Lord Bhairav. Offer blue flowers or coconut. Chant 'Om Rahuve Namaha' 108 times on Saturdays.",
            "Donate black sesame seeds, blue cloth, or mustard oil on Saturdays. Keep a Gomed (Hessonite) stone — after consultation.",
        ],
    },
    "Jupiter": {
        "duration": "16 years",
        "nature": "Wisdom, expansion, teacher, children, dharma, wealth",
        "themes": "Jupiter Mahadasha is considered among the most auspicious periods in Vedic astrology. Expansion in all areas of life — wisdom, wealth, family, and spiritual understanding. Guru's blessings flow. Marriage, children, and higher education are frequently blessed during this time.",
        "positive": "Wealth accumulation, marriage, children, higher education, spiritual growth, wisdom, respect in society, guru's grace.",
        "challenges": "Overexpansion, financial complacency, weight gain, liver issues, excessive optimism leading to poor judgment.",
        "spiritual": "This is the period for serious spiritual practice. Study of scriptures, service to teachers (Guru Seva), and building dharmic foundations for life.",
        "upayas": [
            "Worship Lord Vishnu or Brihaspati on Thursdays. Offer yellow flowers, bananas, and turmeric. Chant 'Om Gurave Namaha'.",
            "Donate yellow items — turmeric, yellow clothes, gold — to Brahmins. Wear Yellow Sapphire (Pukhraj) in gold on the index finger.",
        ],
    },
    "Saturn": {
        "duration": "19 years",
        "nature": "Karma, discipline, delays, service, longevity, justice",
        "themes": "Saturn Mahadasha is the great teacher. Nothing comes without effort — but the rewards of sincere work are permanent. This period demands discipline, patience, and service. Karmic accounts are settled. What you have built honestly will endure; what was built on shortcuts will fall.",
        "positive": "Long-lasting achievements through hard work, spiritual maturity, justice, service to the poor, accumulated wisdom, property and land matters.",
        "challenges": "Delays, obstacles, health issues (joints, bones, nervous system), separation, depression, heaviness of spirit, confronting past karma.",
        "spiritual": "Saturn rewards those who serve without ego. Seva (selfless service), simplicity, and acceptance of karma are the highest remedies for Saturn.",
        "upayas": [
            "Light a mustard oil lamp under Peepal tree on Saturday evenings. Chant 'Om Shanaishcharaya Namaha' 108 times.",
            "Donate black sesame, black cloth, or iron items to the poor on Saturdays. Serve elders, the disabled, and underprivileged communities.",
        ],
    },
    "Mercury": {
        "duration": "17 years",
        "nature": "Intelligence, communication, business, learning, youth",
        "themes": "Mercury Mahadasha activates the intellect, sharpens communication, and brings opportunities in business, education, and writing. The mind becomes highly analytical. Younger people, students, and communication fields flourish. A good period for learning new skills and commercial ventures.",
        "positive": "Business success, eloquence, writing and teaching opportunities, analytical sharpness, youthfulness, education, good for traders.",
        "challenges": "Nervous anxiety, skin issues, over-analysis leading to indecision, deception through speech, respiratory issues.",
        "spiritual": "Mercury responds to clarity of speech and purity of thought. Honest communication, mantras, and study of sacred texts are powerful practices.",
        "upayas": [
            "Worship Lord Vishnu on Wednesdays. Offer green mung dal and green cloth. Chant 'Om Budhaya Namaha' 108 times.",
            "Wear Emerald (Panna) in gold on the little finger. Donate green vegetables and books to students.",
        ],
    },
    "Ketu": {
        "duration": "7 years",
        "nature": "Spirituality, liberation, past life, detachment, mysticism",
        "themes": "Ketu Mahadasha is deeply spiritual and often misunderstood. It strips away material attachments to reveal the soul's true nature. Events feel fated — as if karma from past lives is completing itself. Worldly matters may feel hollow, while spiritual experiences intensify.",
        "positive": "Spiritual awakening, liberation from limiting patterns, psychic ability, healing powers, completion of past karma, occult knowledge.",
        "challenges": "Confusion about direction, sudden losses, health issues (viral, mysterious ailments), accidents, feeling of disconnection from the world.",
        "spiritual": "This is the most powerful period for moksha sadhana. Meditation, pilgrimage, study of Vedanta, and service to spiritual teachers bear extraordinary fruit.",
        "upayas": [
            "Worship Lord Ganesha or Lord Dattatreya. Offer flowers and durva grass. Chant 'Om Ketave Namaha' 108 times.",
            "Donate grey or multi-coloured blankets to the poor. Chant Maha Mrityunjaya Mantra regularly for protection.",
        ],
    },
    "Venus": {
        "duration": "20 years",
        "nature": "Relationships, luxury, arts, pleasures, marriage, beauty",
        "themes": "Venus Mahadasha is one of the most pleasurable and productive periods. Relationships, marriage, arts, and material comforts are blessed. Beauty, luxury, and refinement feature prominently. This is a period for enjoying life's gifts — and for deepening the understanding of love.",
        "positive": "Marriage or new relationships, artistic success, financial prosperity, luxurious comforts, vehicles and property, beauty and refinement.",
        "challenges": "Overindulgence in pleasures, relationship conflicts, reproductive health issues, excessive spending, attachment to sensory gratification.",
        "spiritual": "Venus at its highest is divine love — Bhakti. Worship of Lakshmi, devotional music, and cultivation of true beauty (inner and outer) are the highest expressions.",
        "upayas": [
            "Worship Goddess Lakshmi on Fridays. Offer white flowers, milk sweets, and perfume. Chant 'Om Shukraya Namaha' 108 times.",
            "Wear Diamond or White Sapphire in silver on the middle finger. Donate white sweets, silk, or silver to young women.",
        ],
    },
}

# ── Sadhe Sati interpretations ────────────────────────────────────────────────
SADHE_SATI_PHASES = {
    "Rising (12th from Moon)": {
        "heading": "Rising Phase — Preparation & Introspection",
        "description": (
            "Saturn enters the sign just before your natal Moon, beginning the first phase of Sadhe Sati. "
            "This is a period of gradual inner pressure — a calling inward. Sleep may be disturbed, "
            "expenditure rises, and hidden matters surface. Travel, foreign connections, and matters of "
            "loss or letting go become prominent. This phase asks you to release what no longer serves."
        ),
        "areas": "Sleep, subconscious mind, foreign travel, expenses, spiritual retreat, isolation.",
        "duration": "Approximately 2.5 years.",
        "advice": (
            "This is a time for inner work, not outer ambition. Reduce unnecessary expenses. "
            "Spend time in meditation and self-reflection. Be cautious in foreign dealings. "
            "Service to the poor and elderly brings great relief."
        ),
    },
    "Peak (over Moon sign)": {
        "heading": "Peak Phase — The Core Testing",
        "description": (
            "Saturn now transits directly over your natal Moon sign — the most intense phase of Sadhe Sati. "
            "The mind is under pressure. Emotional challenges, health fluctuations, and tests in relationships "
            "and career are common. This is the phase most people fear — but it is Saturn teaching you your "
            "greatest lessons about responsibility, patience, and authentic living."
        ),
        "areas": "Mind, emotions, mother, public image, career stability, health.",
        "duration": "Approximately 2.5 years.",
        "advice": (
            "Patience is your greatest tool now. Do not make hasty decisions. Take care of your health "
            "and your mother's wellbeing. Honest, disciplined effort will be rewarded — shortcuts will backfire. "
            "This phase ultimately builds extraordinary inner strength."
        ),
    },
    "Setting (2nd from Moon)": {
        "heading": "Setting Phase — Reconstruction & Release",
        "description": (
            "Saturn moves to the sign after your natal Moon, beginning the final phase of Sadhe Sati. "
            "Financial matters and family stability are the primary themes. Speech and food habits need "
            "attention. The pressure begins to lighten — but the lessons of the entire 7.5-year journey "
            "must now be integrated into practical life."
        ),
        "areas": "Finances, family, speech, food, accumulated wealth, early childhood matters.",
        "duration": "Approximately 2.5 years.",
        "advice": (
            "Be conservative with finances and investments. Watch your words — harsh speech brings difficulty now. "
            "Family relationships need tender attention. The end of this phase marks a significant turning point "
            "toward greater freedom and achievement."
        ),
    },
}

SADHE_SATI_NOT_ACTIVE = {
    "description": (
        "You are not currently under Sadhe Sati. This is a relatively lighter period of Saturn's influence. "
        "Transit Saturn is not in the 12th, 1st, or 2nd house from your natal Moon sign."
    ),
    "note": (
        "While Sadhe Sati is absent, Saturn still transits all houses and continues its natural karmic work. "
        "Regular Saturn propitiation is always beneficial."
    ),
    "general_upaya": (
        "Upaya (General Saturn): Light a sesame oil lamp on Saturday evenings. "
        "Donate black sesame seeds or black cloth to the poor. Serve elders and the underprivileged."
    ),
}

SADHE_SATI_INTRO = (
    "Sadhe Sati (साढ़े साती) literally means '7 and a half' — the 7.5-year period when Saturn transits "
    "the 12th, 1st, and 2nd signs from the natal Moon. Far from being a curse, this is Saturn's most "
    "direct teaching — a period of karmic reckoning, purification, and ultimately, deep strength. "
    "Those who work with Saturn's energy during this time emerge with extraordinary resilience and wisdom."
)

# ── Public functions ─────────────────────────────────────────────────────────

def interpret_lagna(lagna_sign: str, lord: str, lord_sign: str) -> str:
    """Return full Lagna interpretation as formatted text."""
    data = LAGNA_DATA.get(lagna_sign, {})
    if not data:
        return f"Lagna in {lagna_sign} — ruled by {lord}."

    lines = [
        f"🔱 Lagna (Ascendant): {lagna_sign} / {_sanskrit_sign(lagna_sign)}",
        f"📍 Nature: {data['nature']}",
        f"🪐 Lagna Lord {lord} is placed in {lord_sign}",
        "",
        f"🧬 Physical Constitution",
        data["body"],
        "",
        f"🌟 Core Personality",
        data["personality"],
        "",
        f"✅ Natural Strengths",
        data["strengths"],
        "",
        f"⚠️ Areas of Growth",
        data["challenges"],
        "",
        f"🛤️ Life Direction",
        data["life_path"],
        "",
        f"🕉️ {data['upaya']}",
    ]
    return "\n".join(lines)


def interpret_dasha(lord: str, end_date_str: str) -> str:
    """Return full Mahadasha interpretation as formatted text."""
    data = DASHA_DATA.get(lord, {})
    if not data:
        return f"{lord} Mahadasha — ending {end_date_str}."

    lines = [
        f"🔱 Current Mahadasha: {lord} (ends {end_date_str})",
        f"⏳ Duration: {data['duration']}  |  Nature: {data['nature']}",
        "",
        f"🌊 Key Themes of This Period",
        data["themes"],
        "",
        f"🌟 Blessings & Opportunities",
        data["positive"],
        "",
        f"⚠️ Areas Requiring Care",
        data["challenges"],
        "",
        f"🕉️ Spiritual Guidance",
        data["spiritual"],
        "",
        f"🙏 Upayas (Remedies)",
    ]
    for i, upaya in enumerate(data["upayas"], 1):
        lines.append(f"  {i}. {upaya}")

    return "\n".join(lines)


def interpret_sadhe_sati(sadhe: dict) -> str:
    """Return full Sadhe Sati interpretation as formatted text."""
    active = sadhe.get("active", False)
    moon_sign = sadhe.get("moon_sign", "-")
    saturn_sign = sadhe.get("saturn_sign", "-")
    phase = sadhe.get("phase")
    exp = sadhe.get("expected_signs", {}) or {}

    lines = [
        "═══════════════════════════════════",
        f"🪐 Sadhe Sati Status: {'✅ ACTIVE' if active else '❌ NOT ACTIVE'}",
        f"🌙 Natal Moon Sign  : {moon_sign} / {_sanskrit_sign(moon_sign)}",
        f"🪐 Transit Saturn   : {saturn_sign} / {_sanskrit_sign(saturn_sign)} (Sidereal Lahiri)",
    ]

    if active and phase:
        lines.append(f"📍 Phase            : {phase}")

    lines += ["═══════════════════════════════════", ""]

    lines += [
        f"📖 What is Sadhe Sati?",
        SADHE_SATI_INTRO,
        "",
    ]

    if active and phase:
        phase_data = SADHE_SATI_PHASES.get(phase, {})
        if phase_data:
            lines += [
                f"🔱 Your Phase: {phase_data['heading']}",
                "",
                phase_data["description"],
                "",
                f"⏳ Duration: {phase_data['duration']}",
                f"🎯 Life Areas Affected: {phase_data['areas']}",
                "",
                f"🛤️ Guidance for This Phase:",
                phase_data["advice"],
                "",
                "🙏 Upayas (Remedies for Sadhe Sati):",
                "  1. Recite Shani Chalisa or Hanuman Chalisa every Saturday.",
                "  2. Light mustard oil lamp under Peepal tree on Saturday evenings.",
                "  3. Donate black sesame, black cloth, or iron to the needy on Saturdays.",
                "  4. Chant 'Om Shanaishcharaya Namaha' 108 times daily.",
                "  5. Serve the elderly, disabled, and underprivileged — Saturn is deeply propitiated by sincere service.",
                "",
                "🕉️ Remember: Sadhe Sati is not a punishment but Saturn's most intense teaching.",
                "   Those who face it with courage, discipline, and devotion emerge stronger than ever.",
            ]
    else:
        nd = SADHE_SATI_NOT_ACTIVE
        lines += [
            nd["description"],
            "",
            nd["note"],
            "",
            nd["general_upaya"],
        ]

        if not active and exp:
            rising  = exp.get("rising", "")
            peak    = exp.get("peak", "")
            setting = exp.get("setting", "")
            if rising and peak and setting:
                lines += [
                    "",
                    f"📅 Sadhe Sati will be active when Saturn enters: {rising} (Rising), "
                    f"{peak} (Peak), or {setting} (Setting).",
                ]

    return "\n".join(lines)


def _sanskrit_sign(sign: str) -> str:
    mapping = {
        "Aries": "Mesha", "Taurus": "Vrishabha", "Gemini": "Mithuna",
        "Cancer": "Karka", "Leo": "Simha", "Virgo": "Kanya",
        "Libra": "Tula", "Scorpio": "Vrischika", "Sagittarius": "Dhanu",
        "Capricorn": "Makara", "Aquarius": "Kumbha", "Pisces": "Meena",
    }
    return mapping.get(sign, sign)
