import random

# ── Light Seer's Tarot — Full 78-Card Deck ────────────────────────────────
# Meanings sourced from lightseerstarot.com (Chris-Anne)
# Light Seer = Upright | Shadow Seer = Reversed
# ─────────────────────────────────────────────────────────────────────────

deck = [
    # ── MAJOR ARCANA ────────────────────────────────────────────────────────
    {
        "name": "0_The_Fool",
        "meaning": "New beginnings, enthusiasm, adventures, fresh opportunities, the potential to bring your dreams to life, having faith, a transitional period of awakening, optimism, innocence, light-heartedness and being spontaneous",
        "shadow": "Naivety, assuming you already have the answer, rash or overly impulsive choices, lacking experience, analysis-paralysis, being bogged down, foolishness, jumping before you look",
        "affirmation": "I embrace the unknown with an open heart and trust the Universe to catch me.",
    },
    {
        "name": "1_The_Magician",
        "meaning": "Inspired action, willpower, manifestation, resourcefulness, desire, creation, the power to bring your visions into reality, harnessing your skills and talents",
        "shadow": "Manipulation, out-of-alignment desires, greed, trickery, illusions, not using your gifts, untapped potential, deceit",
        "affirmation": "I have all the tools I need. I create my reality with intention and will.",
    },
    {
        "name": "2_The_High_Priestess",
        "meaning": "Intuition, sacred feminine wisdom, higher powers, the subconscious, mystery, deep knowing, psychic ability, the power of the inner voice, patience and stillness",
        "shadow": "Secrets, hidden agendas, disconnected from your intuition, a need to listen more deeply, repressed feelings, gossip",
        "affirmation": "I trust my inner knowing. My intuition is my greatest guide.",
    },
    {
        "name": "3_The_Empress",
        "meaning": "Abundance, femininity, fertility, nurturing, the earth, creativity, sensuality, beauty, pregnancy, motherhood, the fullness of life",
        "shadow": "Creative block, dependence, smothering, neglecting self-care, not nurturing yourself or others, feeling disconnected from the earth",
        "affirmation": "I am abundant, creative, and deeply connected to the flow of life.",
    },
    {
        "name": "4_The_Emperor",
        "meaning": "Authority, structure, stability, leadership, fatherhood, discipline, establishment, logic, power and control used for good",
        "shadow": "Domination, rigidity, inflexibility, abuse of power, an overbearing authority figure, lack of discipline, control issues",
        "affirmation": "I lead with wisdom, discipline, and compassion.",
    },
    {
        "name": "5_The_Hierophant",
        "meaning": "Tradition, spiritual wisdom, religious institutions, conformity, establishment, a spiritual mentor or teacher, conventional paths, shared beliefs, ceremony",
        "shadow": "Dogma, challenging tradition, feeling restricted by convention, a need to find your own path, corruption, rebellion",
        "affirmation": "I honor the wisdom of tradition while staying true to my own soul path.",
    },
    {
        "name": "6_The_Lovers",
        "meaning": "Love, harmony, relationships, alignment of values, choices, soulmate connections, union, attraction, partnerships built on mutual respect",
        "shadow": "Disharmony, imbalance in relationships, misaligned values, difficult choices, a love triangle, broken communication",
        "affirmation": "I choose love. I attract relationships that reflect my highest values.",
    },
    {
        "name": "7_The_Chariot",
        "meaning": "Willpower, determination, victory, ambition, control, success, overcoming obstacles, forward momentum, the drive to achieve your goals",
        "shadow": "Lack of control, aggression, opposition, scattered energy, no clear direction, forcing outcomes",
        "affirmation": "I move forward with focused intention and unstoppable determination.",
    },
    {
        "name": "8_Strength",
        "meaning": "Courage, inner strength, compassion, patience, soft power, influence, taming the ego, resilience, the power of love over force",
        "shadow": "Self-doubt, weakness, giving in to fear, lack of self-discipline, raw emotion overtaking reason, insecurity",
        "affirmation": "My greatest strength comes from love, patience, and compassion.",
    },
    {
        "name": "9_The_Hermit",
        "meaning": "Soul-searching, introspection, solitude, inner wisdom, a spiritual guide, a period of withdrawal for self-discovery, enlightenment, being a light for others",
        "shadow": "Isolation, loneliness, withdrawn too far from the world, reclusive behaviour, refusing guidance, loss of direction",
        "affirmation": "I find wisdom in stillness and carry my light to illuminate the path for others.",
    },
    {
        "name": "10_Wheel_of_Fortune",
        "meaning": "Fate, karma, turning points, good luck, life cycles, destiny, unexpected change, the flow of the Universe, what goes around comes around",
        "shadow": "Bad luck, resistance to change, feeling out of control, a negative cycle, clinging to the past",
        "affirmation": "I flow with life's cycles with grace. Every turn brings new opportunity.",
    },
    {
        "name": "11_Justice",
        "meaning": "Truth, fairness, cause and effect, law, accountability, balance, integrity, honesty, karmic justice, decisions made with clear logic",
        "shadow": "Injustice, dishonesty, lack of accountability, unfair treatment, avoiding consequences, biased decisions",
        "affirmation": "I act with integrity. The Universe always returns truth and fairness.",
    },
    {
        "name": "12_The_Hanged_Man",
        "meaning": "Surrender, pause, new perspectives, sacrifice, suspension, letting go of control, enlightenment through release, a different point of view",
        "shadow": "Stalling, martyrdom, indecision, delay, refusing to let go, a period of stagnation, wasted potential",
        "affirmation": "I surrender to the divine flow and find wisdom in the pause.",
    },
    {
        "name": "13_Death",
        "meaning": "Transformation, endings, new beginnings, transition, letting go, change, the cycle of life, metamorphosis, releasing what no longer serves",
        "shadow": "Resistance to change, inability to move on, stagnation, holding on too tightly, fear of the unknown",
        "affirmation": "I release what no longer serves me and welcome beautiful transformation.",
    },
    {
        "name": "14_Temperance",
        "meaning": "Balance, patience, moderation, purpose, harmony, alchemy, inner peace, a middle path, healing, the blending of opposites",
        "shadow": "Imbalance, excess, a lack of long-term vision, impatience, discord, extremes, misalignment",
        "affirmation": "I bring balance and harmony to every area of my life.",
    },
    {
        "name": "15_The_Devil",
        "meaning": "Bondage, shadow self, materialism, addiction, unhealthy attachments, restriction, patterns that keep you trapped, facing your darker nature",
        "shadow": "Detachment, breaking free, releasing chains, reclaiming power, the beginning of recovery, awareness of limiting beliefs",
        "affirmation": "I recognise my shadows with compassion and choose freedom over fear.",
    },
    {
        "name": "16_The_Tower",
        "meaning": "Sudden upheaval, chaos, revelation, awakening, the crumbling of false structures, radical change, a breakthrough disguised as a breakdown",
        "shadow": "Avoiding disaster, delaying the inevitable, fear of change, resisting necessary disruption, clinging to broken structures",
        "affirmation": "Even in chaos, I trust that what falls was never meant to stand.",
    },
    {
        "name": "17_The_Star",
        "meaning": "Hope, renewal, serenity, inspiration, faith, healing, a guiding light, calm after the storm, the promise of better things to come, spiritual connection",
        "shadow": "Despair, hopelessness, disconnection from faith, feeling lost, a lack of inspiration, disappointment",
        "affirmation": "I am filled with hope. The Universe is always working in my favour.",
    },
    {
        "name": "18_The_Moon",
        "meaning": "Illusion, fear, the subconscious, intuition, dreams, hidden truths, the shadow self, anxiety, mystery, what lies beneath the surface",
        "shadow": "Confusion lifting, fears releasing, repressed emotions coming to light, unhealthy coping mechanisms, misunderstanding",
        "affirmation": "I navigate the unknown with trust. My intuition lights the way through illusion.",
    },
    {
        "name": "19_The_Sun",
        "meaning": "Joy, success, vitality, optimism, clarity, warmth, abundance, positivity, childhood innocence, a radiant YES from the Universe",
        "shadow": "Pessimism, temporary sadness, blocked joy, inner child wounds, unrealistic expectations, arrogance",
        "affirmation": "I radiate joy, warmth, and gratitude. Life is beautiful.",
    },
    {
        "name": "20_Judgement",
        "meaning": "Reflection, reckoning, inner calling, awakening, absolution, a significant transition, hearing a higher calling, rebirth, evaluation",
        "shadow": "Self-doubt, ignoring your calling, fear of being judged, inability to forgive yourself, an inability to move forward",
        "affirmation": "I answer my highest calling with courage and open my heart to rebirth.",
    },
    {
        "name": "21_The_World",
        "meaning": "Completion, accomplishment, wholeness, integration, travel, the end of one cycle and the beginning of another, fulfilment, success",
        "shadow": "Incompletion, stagnation, a lack of closure, shortcuts taken, not fully integrating lessons before moving on",
        "affirmation": "I am whole. I celebrate my journey and step forward with wisdom.",
    },

    # ── WANDS ────────────────────────────────────────────────────────────────
    {
        "name": "Ace_of_Wands",
        "meaning": "Inspiration, new opportunities, growth, passion, potential, a creative spark, the beginning of something exciting, energy and enthusiasm",
        "shadow": "Delays, lack of passion, creative block, an idea that hasn't fully formed, false starts, lost motivation",
        "affirmation": "I seize this spark of inspiration and channel it into bold, creative action.",
    },
    {
        "name": "Two_of_Wands",
        "meaning": "Future planning, progress, decisions, courage, stepping outside comfort zone, long-term vision, a world of possibilities",
        "shadow": "Fear of the unknown, indecision, playing it too safe, lack of planning, feeling trapped in one place",
        "affirmation": "I plan boldly, trust my vision, and step forward into my expansive future.",
    },
    {
        "name": "Three_of_Wands",
        "meaning": "Expansion, foresight, overseas opportunities, preparation, looking ahead, growth already in motion, awaiting results of past efforts",
        "shadow": "Delays, obstacles to travel or expansion, a lack of foresight, plans falling through, impatience",
        "affirmation": "My horizons are expanding. What I have planted is growing beautifully.",
    },
    {
        "name": "Four_of_Wands",
        "meaning": "Celebration, joy, harmony, home, community, milestones, relaxation, weddings and happy events, a stable foundation",
        "shadow": "Instability at home, cancelled celebrations, lack of support, family conflicts, transition periods",
        "affirmation": "I celebrate how far I have come and cherish the community that surrounds me.",
    },
    {
        "name": "Five_of_Wands",
        "meaning": "Conflict, disagreements, competition, creative tension, diversity of opinions, healthy debate, challenges that lead to growth",
        "shadow": "Avoiding conflict, suppressed tension, a need for compromise, unnecessary aggression, chaos",
        "affirmation": "I rise above conflict with grace and find the wisdom in differing perspectives.",
    },
    {
        "name": "Six_of_Wands",
        "meaning": "Victory, success, public recognition, progress, self-confidence, acclaim, achievement after hard work, leadership",
        "shadow": "Ego, a fall from grace, lack of recognition, self-doubt, seeking validation from others, short-lived success",
        "affirmation": "I embrace my victory with humility and gratitude.",
    },
    {
        "name": "Seven_of_Wands",
        "meaning": "Perseverance, defending your position, challenge, competition, holding your ground, courage under pressure, standing up for your beliefs",
        "shadow": "Exhaustion, giving up, feeling overwhelmed, paranoia, not picking your battles wisely",
        "affirmation": "I stand my ground with confidence. I am worth defending.",
    },
    {
        "name": "Eight_of_Wands",
        "meaning": "Fast-paced change, movement, swift action, communication, travel, things suddenly accelerating, alignment, momentum",
        "shadow": "Delays, frustration, scattered energy, miscommunication, being overwhelmed by speed of change",
        "affirmation": "I embrace the beautiful momentum carrying me towards my goals.",
    },
    {
        "name": "Nine_of_Wands",
        "meaning": "Resilience, courage, persistence, last push, boundaries, grit, the strength to continue when you are almost at the finish line",
        "shadow": "Exhaustion, giving up too soon, paranoia, excessive defensiveness, not asking for help when needed",
        "affirmation": "I am resilient. I have the strength to see this through to the end.",
    },
    {
        "name": "Ten_of_Wands",
        "meaning": "Burden, responsibility, overcommitment, hard work, carrying too much, the need to delegate or release some weight",
        "shadow": "Inability to delegate, martyrdom, carrying others' burdens, burnout, refusing help",
        "affirmation": "I release what is not mine to carry and ask for help without guilt.",
    },
    {
        "name": "Page_of_Wands",
        "meaning": "Inspiration, discovery, an adventurous spirit, curiosity, a new creative path, enthusiasm, a message of exciting news, potential",
        "shadow": "Immaturity, a lack of direction, unfocused energy, too many ideas and not enough action, restlessness",
        "affirmation": "I explore with curiosity and follow my creative spark wherever it leads.",
    },
    {
        "name": "Knight_of_Wands",
        "meaning": "Energy, passion, adventure, impulsiveness, action, confidence, a fearless pursuit of goals, daring and bold energy",
        "shadow": "Recklessness, hot-headed behaviour, scattered focus, impulsivity without planning, burnout from moving too fast",
        "affirmation": "I pursue my passions boldly while tempering my fire with wisdom.",
    },
    {
        "name": "Queen_of_Wands",
        "meaning": "Courage, confidence, determination, warmth, independence, charisma, a natural leader, someone who uplifts others, creative power",
        "shadow": "Jealousy, manipulation, demanding behaviour, burned out confidence, feeling unheard",
        "affirmation": "I radiate warmth and confidence. My fire inspires everyone around me.",
    },
    {
        "name": "King_of_Wands",
        "meaning": "Natural leader, vision, honour, entrepreneurial spirit, big-picture thinking, inspiration, boldness, a successful and charismatic authority",
        "shadow": "Impulsiveness, overbearing behaviour, unrealistic expectations, arrogance, ruthlessness",
        "affirmation": "I lead with vision, honour, and inspire others to reach their highest potential.",
    },

    # ── CUPS ─────────────────────────────────────────────────────────────────
    {
        "name": "Ace_of_Cups",
        "meaning": "New love, compassion, creativity, emotional abundance, the beginning of a deep emotional journey, a new relationship or spiritual connection, joy",
        "shadow": "Emotional blockage, repressed feelings, a relationship that isn't growing, creative drought, sadness",
        "affirmation": "I open my heart fully to love, compassion, and creative abundance.",
    },
    {
        "name": "Two_of_Cups",
        "meaning": "Unified love, partnership, mutual attraction, harmony, the meeting of two souls, a deep soulmate connection, balance in relationship",
        "shadow": "Imbalance in a relationship, a broken connection, lack of communication, codependency, separation",
        "affirmation": "I attract and nurture relationships built on mutual love, respect, and harmony.",
    },
    {
        "name": "Three_of_Cups",
        "meaning": "Celebration, friendship, community, creativity, joy, abundance, coming together, support, sisterhood and brotherhood",
        "shadow": "Overindulgence, gossip, third-party interference, cliques, celebrations gone wrong, isolation",
        "affirmation": "I celebrate life with my community and cherish the bonds that lift me higher.",
    },
    {
        "name": "Four_of_Cups",
        "meaning": "Contemplation, meditation, apathy, boredom, re-evaluation, a period of withdrawal, not seeing the opportunities before you",
        "shadow": "New awareness, motivation returning, accepting an offer, emerging from a period of stagnation",
        "affirmation": "I look within for answers and open my eyes to the gifts already around me.",
    },
    {
        "name": "Five_of_Cups",
        "meaning": "Loss, grief, disappointment, focusing on the negative, regret, mourning, the need to process sadness before moving on",
        "shadow": "Acceptance, moving on, finding hope after loss, forgiveness, turning towards what remains",
        "affirmation": "I honour my grief, then gently turn to face the blessings that remain.",
    },
    {
        "name": "Six_of_Cups",
        "meaning": "Nostalgia, childhood memories, innocence, revisiting the past, comfort, reunion, generosity, simple joys, healing the inner child",
        "shadow": "Stuck in the past, idealising old times, refusing to grow, an unhealthy attachment to how things were",
        "affirmation": "I honour my past with gratitude while standing fully present in today's gifts.",
    },
    {
        "name": "Seven_of_Cups",
        "meaning": "Choices, fantasy, illusion, wishful thinking, imagination, having many options, searching for purpose, daydreaming",
        "shadow": "Clarity returning, cutting through illusion, making a decision, aligning with reality, facing the truth",
        "affirmation": "I see through illusion and choose my path with clarity, wisdom, and intention.",
    },
    {
        "name": "Eight_of_Cups",
        "meaning": "Walking away, disillusionment, leaving behind what no longer serves, a brave exit, seeking deeper meaning, spiritual quest",
        "shadow": "Fear of change, staying in a situation past its time, inability to walk away, clinging to the familiar",
        "affirmation": "I have the courage to walk away from what no longer serves my highest good.",
    },
    {
        "name": "Nine_of_Cups",
        "meaning": "Contentment, satisfaction, gratitude, emotional fulfilment, wishes granted, happiness, pleasure, the dream made real",
        "shadow": "Overindulgence, superficiality, complacency, inner emptiness beneath outward success, unfulfilled wishes",
        "affirmation": "I am grateful for the abundance in my life. My heart is full.",
    },
    {
        "name": "Ten_of_Cups",
        "meaning": "Divine love, blissful relationships, family harmony, deep contentment, a joyful home life, alignment with your heart's desire",
        "shadow": "Broken family, unhappy home, disconnected relationships, values out of alignment, a gap between the dream and reality",
        "affirmation": "I am surrounded by love, harmony, and the warmth of deep connection.",
    },
    {
        "name": "Page_of_Cups",
        "meaning": "Creative opportunities, intuitive messages, emotional sensitivity, dreams, a gentle and curious heart, unexpected news, artistic beginnings",
        "shadow": "Emotional immaturity, daydreaming without action, vulnerability used against you, naivety in relationships",
        "affirmation": "I trust the whispers of my heart and follow my creative intuition with joy.",
    },
    {
        "name": "Knight_of_Cups",
        "meaning": "Romance, charm, imagination, following the heart, an invitation or offer, the pursuit of dreams, a creative and idealistic soul",
        "shadow": "Moodiness, unrealistic expectations, over-romanticism, emotional manipulation, scattered dreams",
        "affirmation": "I follow my heart with courage, charm, and an open spirit.",
    },
    {
        "name": "Queen_of_Cups",
        "meaning": "Compassion, deep intuition, emotional wisdom, nurturing, empathy, a caring presence, inner emotional knowing, healing",
        "shadow": "Emotional dependency, martyrdom, being overwhelmed by emotions, codependency, suppressed feelings",
        "affirmation": "I nurture myself and others from a place of deep compassion and wisdom.",
    },
    {
        "name": "King_of_Cups",
        "meaning": "Emotional balance, wisdom, diplomacy, compassion, generosity, a calm and steady presence, mastery of the emotional world",
        "shadow": "Emotional manipulation, moodiness, repressed emotions, using feelings as weapons, cold behaviour",
        "affirmation": "I lead with emotional intelligence, compassion, and steady inner calm.",
    },

    # ── SWORDS ────────────────────────────────────────────────────────────────
    {
        "name": "Ace_of_Swords",
        "meaning": "Breakthrough, new ideas, mental clarity, truth, justice, clarity of thought, cutting through confusion, a moment of sharp realisation",
        "shadow": "Confusion, brutal honesty used as a weapon, chaos, scattered thinking, miscommunication",
        "affirmation": "I cut through confusion with clarity and speak my truth with courage.",
    },
    {
        "name": "Two_of_Swords",
        "meaning": "A difficult decision, weighing options, a stalemate, avoiding the truth, being at a crossroads, a need to look within for answers",
        "shadow": "Indecision ending, information coming to light, seeing clearly after confusion, breaking a stalemate",
        "affirmation": "I trust my intuition to guide me through difficult decisions with clarity.",
    },
    {
        "name": "Three_of_Swords",
        "meaning": "Heartbreak, emotional pain, grief, sorrow, betrayal, loss, the clearing of old pain, a necessary wound that allows healing",
        "shadow": "Recovery, healing, releasing pain, forgiveness, the beginning of moving forward after grief",
        "affirmation": "I allow myself to grieve and trust that healing is already underway.",
    },
    {
        "name": "Four_of_Swords",
        "meaning": "Rest, recovery, contemplation, sanctuary, a needed break, stillness, withdrawal from conflict, healing through rest",
        "shadow": "Restlessness, refusing to rest, burnout from overactivity, being forced to slow down",
        "affirmation": "I give myself permission to rest. Stillness is where I restore my power.",
    },
    {
        "name": "Five_of_Swords",
        "meaning": "Conflict, defeat, hollow victory, tension, disagreements, a battle where everyone loses something, knowing when to walk away",
        "shadow": "Reconciliation, moving past conflict, releasing the need to win, forgiving and letting go",
        "affirmation": "I choose peace over victory and release what no longer needs to be fought.",
    },
    {
        "name": "Six_of_Swords",
        "meaning": "Transition, moving on, calmer waters ahead, rite of passage, leaving turbulence behind, travel, healing through change",
        "shadow": "Resistance to change, unable to move on, carrying old baggage into a new situation, unresolved grief",
        "affirmation": "I move towards calmer waters, releasing the past with grace.",
    },
    {
        "name": "Seven_of_Swords",
        "meaning": "Deception, strategy, stealth, getting away with something, cunning, avoiding confrontation, keeping secrets",
        "shadow": "Being caught, coming clean, realising deception, guilt, the consequences of dishonest behaviour",
        "affirmation": "I act with honesty and integrity. The truth always serves my highest good.",
    },
    {
        "name": "Eight_of_Swords",
        "meaning": "Self-imposed restriction, negative thoughts, feeling trapped, victim mentality, a situation that feels like no way out — but there is",
        "shadow": "Liberation, removing the blindfold, taking back your power, a shift in perspective that sets you free",
        "affirmation": "I am free. I release the thoughts that bind me and step into my power.",
    },
    {
        "name": "Nine_of_Swords",
        "meaning": "Anxiety, worry, nightmares, fear, sleepless nights, catastrophising, a mind in turmoil, deep-seated fears surfacing",
        "shadow": "Hope returning, fears releasing, reaching out for help, the worst is over, healing from anxiety",
        "affirmation": "I release my fears and breathe in peace. The worst exists only in my mind.",
    },
    {
        "name": "Ten_of_Swords",
        "meaning": "Painful endings, betrayal, a crisis point, rock bottom, an unavoidable conclusion, the darkest moment before the dawn",
        "shadow": "Recovery, rising again, refusing to be a victim, the turn-around after hitting bottom, resilience",
        "affirmation": "I have survived this. I rise from the ashes with hard-won wisdom.",
    },
    {
        "name": "Page_of_Swords",
        "meaning": "Curiosity, new ideas, thirst for knowledge, enthusiasm for truth, a quick mind, messages and communication, a watchful observer",
        "shadow": "Gossip, haste, scattered ideas, impulsive speech, cutting words, unreliable information",
        "affirmation": "I seek truth with curiosity and speak with clarity and kindness.",
    },
    {
        "name": "Knight_of_Swords",
        "meaning": "Ambitious, action-oriented, determined, swift movement towards goals, defending beliefs, a fast-moving situation",
        "shadow": "Recklessness, rushing in without thinking, aggression, impatience, verbal conflict",
        "affirmation": "I pursue my goals with focus and temper my ambition with wisdom.",
    },
    {
        "name": "Queen_of_Swords",
        "meaning": "Independent, sharp mind, clear boundaries, unbiased judgement, wisdom from experience, direct communication, seeing through facades",
        "shadow": "Overly critical, cold, isolation, cutting people off harshly, using intellect to wound",
        "affirmation": "I speak my truth with clarity and compassion. My mind is sharp, my heart is open.",
    },
    {
        "name": "King_of_Swords",
        "meaning": "Mental clarity, intellectual power, authority, truth, decisive leadership, a brilliant strategist, integrity in decision-making",
        "shadow": "Tyranny, manipulation, cold logic without heart, using intellect to control, ruthlessness",
        "affirmation": "I lead with clear thought, fair judgement, and unwavering integrity.",
    },

    # ── PENTACLES ─────────────────────────────────────────────────────────────
    {
        "name": "Ace_of_Pentacles",
        "meaning": "A new financial or career opportunity, abundance, prosperity, manifestation, a seed of material potential, grounded beginnings",
        "shadow": "Missed opportunity, poor financial planning, greed, a venture that won't grow, not valuing what you have",
        "affirmation": "I welcome abundance into my life and plant seeds that will flourish.",
    },
    {
        "name": "Two_of_Pentacles",
        "meaning": "Balance, adaptability, time management, juggling multiple priorities, flexibility, playfulness amid challenges",
        "shadow": "Overwhelmed, poor time management, financial instability, dropping the ball, inability to prioritise",
        "affirmation": "I balance my responsibilities with ease, grace, and a sense of play.",
    },
    {
        "name": "Three_of_Pentacles",
        "meaning": "Teamwork, collaboration, skill development, learning, building something together, recognition for your craft, mastery through effort",
        "shadow": "Lack of teamwork, poor communication, disorganisation, mediocrity, conflicts in a group project",
        "affirmation": "I build success through collaboration, dedication, and the mastery of my craft.",
    },
    {
        "name": "Four_of_Pentacles",
        "meaning": "Financial security, saving, stability, a cautious approach to money, holding on, the desire to protect what you have built",
        "shadow": "Greed, hoarding, scarcity mindset, excessive control, blocking the flow of abundance",
        "affirmation": "I am secure in my abundance and trust in the flow of prosperity.",
    },
    {
        "name": "Five_of_Pentacles",
        "meaning": "Financial hardship, poverty consciousness, isolation, feeling left out in the cold, material loss, a call to seek help",
        "shadow": "Recovery, help available if you ask, turning hardship into resilience, community support, finding your way back",
        "affirmation": "Even in difficulty, support is available. I reach out and trust that help is near.",
    },
    {
        "name": "Six_of_Pentacles",
        "meaning": "Generosity, giving and receiving, sharing wealth and resources, charity, gratitude, a kind and balanced exchange",
        "shadow": "Strings attached to generosity, power imbalance in giving, charity that disempowers, debt and obligation",
        "affirmation": "I give and receive with an open heart, knowing abundance flows both ways.",
    },
    {
        "name": "Seven_of_Pentacles",
        "meaning": "Long-term vision, patience, sustainable results, a pause to assess your progress, investment, the fruits of your labour beginning to show",
        "shadow": "Impatience, poor investment, working hard without results, lack of vision, giving up too soon",
        "affirmation": "I trust in the process and know that my patient efforts will bear beautiful fruit.",
    },
    {
        "name": "Eight_of_Pentacles",
        "meaning": "Diligence, skill-building, mastery, commitment to craft, hard work, attention to detail, becoming an expert through practice",
        "shadow": "Perfectionism, lack of ambition, doing work that doesn't align with your passion, boredom, mediocre effort",
        "affirmation": "I dedicate myself to mastering my craft with love, focus, and devotion.",
    },
    {
        "name": "Nine_of_Pentacles",
        "meaning": "Abundance, luxury, self-sufficiency, financial independence, enjoying the fruits of your labour, refinement, confidence",
        "shadow": "Overindulgence, dependence on others, not enjoying what you have, hollow success, reckless spending",
        "affirmation": "I enjoy the beautiful abundance I have created through my own effort.",
    },
    {
        "name": "Ten_of_Pentacles",
        "meaning": "Legacy, family wealth, long-term security, inheritance, tradition, the culmination of material success, a stable and loving home",
        "shadow": "Family conflict over money, financial instability, broken legacy, disputes over inheritance",
        "affirmation": "I build a legacy of love and abundance that will bless generations after me.",
    },
    {
        "name": "Page_of_Pentacles",
        "meaning": "Manifestation, a new financial or educational opportunity, ambition, practicality, skill development, a studious and grounded energy",
        "shadow": "Lack of focus, procrastination, poor planning, a missed opportunity, unrealistic dreams with no action",
        "affirmation": "I take practical steps every day to bring my dreams into beautiful, grounded reality.",
    },
    {
        "name": "Knight_of_Pentacles",
        "meaning": "Hardworking, reliable, methodical, committed, efficient, responsible, a steady and trustworthy approach to goals",
        "shadow": "Stubbornness, stuck in routine, overly conservative, boring, resistance to change",
        "affirmation": "Through steady effort and reliability, I build the life I truly desire.",
    },
    {
        "name": "Queen_of_Pentacles",
        "meaning": "Nurturing, practical, financially savvy, warm and homely, a caretaker of others, creating comfort and security, resourceful",
        "shadow": "Neglecting self-care, overworking, smothering, financial insecurity, putting others first to your own detriment",
        "affirmation": "I nurture my world with practicality and love, beginning always with myself.",
    },
    {
        "name": "King_of_Pentacles",
        "meaning": "Wealth, abundance, business leadership, discipline, stability, a successful and generous authority, the master of material affairs",
        "shadow": "Stubbornness, materialism, obsession with status, using wealth as control, rigidity",
        "affirmation": "I lead with wisdom and generosity, building an empire rooted in integrity.",
    },
]

# ── Spread Definitions ─────────────────────────────────────────────────────
spreads = {
    "1": {
        "name": "Daily Guidance (1 Card)",
        "cards": 1,
    },
    "2": {
        "name": "Past, Present, Future (3 Cards)",
        "cards": 3,
    },
    "3": {
        "name": "The Celtic Cross (10 Cards - Deep Insight)",
        "cards": 10,
    },
    "4": {
        "name": "Love & Relationship (Burning Heart - 5 Cards)",
        "cards": 5,
    },
    "5": {
        "name": "Career & Finance Path (5 Cards)",
        "cards": 5,
    },
    "6": {
        "name": "Decision Maker (Option A vs Option B - 5 Cards)",
        "cards": 5,
    },
    "7": {
        "name": "Chakra Balancing (7 Cards)",
        "cards": 7,
    },
}

# ── Pull Spread ────────────────────────────────────────────────────────────
def get_spread_options():
    return spreads


def pull_spread(spread_id):
    spread_info = spreads.get(spread_id, spreads["1"])
    count = min(spread_info["cards"], len(deck))
    drawn = random.sample(deck, k=count)

    # Position names per spread
    positions_map = {
        "1": ["Today's Guidance"],
        "2": ["Past Influence", "Current Situation", "Future Outcome"],
        "3": [
            "Present Situation", "Crossing Energy", "Root Cause",
            "Recent Past", "Possible Future", "Near Future",
            "Your Attitude", "External Influences", "Hopes & Fears", "Final Outcome",
        ],
        "4": ["You", "Them", "Relationship Dynamics", "Hidden Challenge", "Outcome"],
        "5": ["Current Energy", "Opportunities Ahead", "Hidden Obstacle", "Best Action", "Likely Outcome"],
        "6": ["Current State", "Pros of Option A", "Cons of Option A", "Pros of Option B", "Cons of Option B"],
        "7": [
            "Root — Security (Muladhara)",
            "Sacral — Creativity (Svadhisthana)",
            "Solar Plexus — Power (Manipura)",
            "Heart — Love (Anahata)",
            "Throat — Expression (Vishuddha)",
            "Third Eye — Intuition (Ajna)",
            "Crown — Consciousness (Sahasrara)",
        ],
    }
    positions = positions_map.get(spread_id, [f"Card {i+1}" for i in range(count)])

    result = []
    for i, card in enumerate(drawn):
        is_reversed = random.random() < 0.20      # 20% reversal (Light Seer's style)
        display_name = card["name"].replace("_", " ")
        card_label   = f"{display_name} [REVERSED]" if is_reversed else display_name
        meaning      = f"Shadow Seer: {card['shadow']}" if is_reversed else card["meaning"]

        result.append({
            "Position":    positions[i] if i < len(positions) else f"Card {i+1}",
            "Card":        card_label,
            "BaseName":    display_name,
            "RawName":     card["name"],
            "Meaning":     meaning,
            "Affirmation": card["affirmation"],
            "Reversed":    is_reversed,
            "LightMeaning": card["meaning"],
            "ShadowMeaning": card["shadow"],
        })
    return result


# ── Image Finder ────────────────────────────────────────────────────────────
def find_card_image(raw_name: str, cards_folder: str = "cards"):
    import os
    if not os.path.isdir(cards_folder):
        return None
    clean_search = raw_name.lower().replace("_", "").replace("-", "").replace(" ", "")
    for filename in os.listdir(cards_folder):
        stem = os.path.splitext(filename)[0]
        clean_file = stem.lower().replace("_", "").replace("-", "").replace(" ", "")
        if clean_search == clean_file or clean_search in clean_file or clean_file in clean_search:
            return os.path.join(cards_folder, filename)
    return None
