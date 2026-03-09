"""
Jyogi Shop — Inventory, Reviews, Services, Gallery data.
"""

BRACELETS = [
    {
        "id": "pyrite_citrine",
        "name": "Money Magnet",
        "subtitle": "Pyrite & Citrine",
        "tagline": "Attract wealth. Amplify abundance.",
        "price": "₹1,499",
        "original_price": "₹2,000",
        "desc": (
            "Pyrite (Fool's Gold) draws in wealth frequency while Citrine amplifies "
            "your solar-plexus energy. Each bead is hand-selected, cleansed under the "
            "full moon, and charged with Jupiter mantras. Wear on the left wrist every "
            "Tuesday and Thursday for maximum potency."
        ),
        "benefits": ["Wealth & prosperity", "Career growth", "Confidence boost", "Abundance mindset"],
        "ritual": "Wear on left wrist. Chant 'Om Shreem Hreem Kleem' 108 times on Thursdays.",
        "img": "https://images.unsplash.com/photo-1599643478518-17488fbbcd75?w=600&q=80",
        "planet": "Jupiter / Sun",
        "chakra": "Solar Plexus",
        "chakra_color": "#FFD700",
        "stone_color": "#DAA520",
        "badge": "Best Seller",
        "badge_color": "#2B7A0B",
        "whatsapp_msg": "Hi Jyogi! I want to order the Money Magnet bracelet (₹1,499). Please guide me.",
    },
    {
        "id": "rose_quartz",
        "name": "Self-Love Mala",
        "subtitle": "Rose Quartz & Clear Quartz",
        "tagline": "Heal your heart. Open to love.",
        "price": "₹999",
        "original_price": "₹1,400",
        "desc": (
            "Rose Quartz is the stone of unconditional love — it dissolves emotional wounds "
            "and opens the heart chakra to give and receive love freely. Clear Quartz amplifies "
            "your intentions and magnifies the healing energy. Ideal for relationships, "
            "self-worth, and inner peace."
        ),
        "benefits": ["Emotional healing", "Attract love", "Inner peace", "Self-confidence"],
        "ritual": "Hold over your heart each morning. Affirm: 'I am worthy of deep love.'",
        "img": "https://images.unsplash.com/photo-1602173574767-37ac01994b2a?w=600&q=80",
        "planet": "Venus",
        "chakra": "Heart",
        "chakra_color": "#FF69B4",
        "stone_color": "#FFB6C1",
        "badge": "Most Loved",
        "badge_color": "#c9910a",
        "whatsapp_msg": "Hi Jyogi! I want to order the Self-Love Mala (₹999). Please guide me.",
    },
    {
        "id": "black_tourmaline",
        "name": "Protection Shield",
        "subtitle": "Black Tourmaline & Obsidian",
        "tagline": "Block negativity. Ground your aura.",
        "price": "₹1,299",
        "original_price": "₹1,800",
        "desc": (
            "Black Tourmaline is the supreme protector — it creates an energetic shield "
            "against negative energy, psychic attacks, and EMF radiation. Obsidian grounds "
            "the aura deeply into the earth. Together they form an unbreakable shield of "
            "protection. Keep near your workspace or wear daily."
        ),
        "benefits": ["Psychic protection", "EMF shielding", "Grounding", "Removes negativity"],
        "ritual": "Place near your front door or workspace. Cleanse monthly under running water.",
        "img": "https://images.unsplash.com/photo-1615484477780-d3c813346712?w=600&q=80",
        "planet": "Saturn / Ketu",
        "chakra": "Root",
        "chakra_color": "#8B0000",
        "stone_color": "#1a1a1a",
        "badge": "Powerful",
        "badge_color": "#4a4a6a",
        "whatsapp_msg": "Hi Jyogi! I want to order the Protection Shield bracelet (₹1,299). Please guide me.",
    },
    {
        "id": "lapis_amethyst",
        "name": "Third Eye Awakener",
        "subtitle": "Lapis Lazuli & Amethyst",
        "tagline": "Activate intuition. Deepen meditation.",
        "price": "₹1,199",
        "original_price": "₹1,600",
        "desc": (
            "Lapis Lazuli has been revered by mystics for 6,000 years — it activates the "
            "third eye, enhances psychic vision, and connects you to divine wisdom. Amethyst "
            "calms the mental chatter and deepens meditative states. Perfect for spiritual "
            "seekers, healers, and those on a path of awakening."
        ),
        "benefits": ["Psychic intuition", "Deep meditation", "Spiritual wisdom", "Dream clarity"],
        "ritual": "Meditate with bracelet on left wrist. Place on third eye during Shavasana.",
        "img": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=600&q=80",
        "planet": "Ketu / Jupiter",
        "chakra": "Third Eye & Crown",
        "chakra_color": "#6A0DAD",
        "stone_color": "#4169E1",
        "badge": "Spiritual",
        "badge_color": "#5b3f8c",
        "whatsapp_msg": "Hi Jyogi! I want to order the Third Eye Awakener (₹1,199). Please guide me.",
    },
    {
        "id": "green_aventurine",
        "name": "Lucky Charm",
        "subtitle": "Green Aventurine & Jade",
        "tagline": "Invite luck. Seize opportunity.",
        "price": "₹1,099",
        "original_price": "₹1,500",
        "desc": (
            "Green Aventurine is called the 'Stone of Opportunity' — it aligns conditions "
            "so opportunity is inevitable. Jade brings luck, friendship, and good fortune "
            "in business. Together they create a powerful talisman for new ventures, "
            "interviews, and any moment when luck matters."
        ),
        "benefits": ["Good luck", "New opportunities", "Business success", "Positive energy"],
        "ritual": "Wear during important meetings, interviews, and new beginnings.",
        "img": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=80",
        "planet": "Mercury / Venus",
        "chakra": "Heart",
        "chakra_color": "#228B22",
        "stone_color": "#2E8B57",
        "badge": "New",
        "badge_color": "#1a6b8a",
        "whatsapp_msg": "Hi Jyogi! I want to order the Lucky Charm bracelet (₹1,099). Please guide me.",
    },
    {
        "id": "moonstone_pearl",
        "name": "Divine Feminine",
        "subtitle": "Moonstone & Pearl",
        "tagline": "Align with the moon. Embrace your power.",
        "price": "₹1,349",
        "original_price": "₹1,800",
        "desc": (
            "Moonstone is the sacred stone of the goddess — it balances hormones, regulates "
            "cycles, and connects you to lunar energy. Pearl brings purity, wisdom, and "
            "integrity. This combination is especially powerful for women seeking to embrace "
            "their divine feminine nature and heal the mother wound."
        ),
        "benefits": ["Hormonal balance", "Feminine power", "Emotional balance", "Moon connection"],
        "ritual": "Charge under the full moon overnight. Wear during new and full moon days.",
        "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&q=80",
        "planet": "Moon / Venus",
        "chakra": "Sacral & Crown",
        "chakra_color": "#C0C0C0",
        "stone_color": "#E8E8F0",
        "badge": "Sacred",
        "badge_color": "#7a5c8a",
        "whatsapp_msg": "Hi Jyogi! I want to order the Divine Feminine bracelet (₹1,349). Please guide me.",
    },
]

SERVICES = [
    {
        "id": "vedic_reading",
        "name": "Full Vedic Reading",
        "icon": "🪐",
        "price": "₹1,500",
        "duration": "60 min",
        "desc": "Complete birth chart analysis, Dasha periods, Sadhe Sati, planetary remedies, and life predictions. Includes PDF report.",
        "includes": ["Birth chart (Sidereal Lahiri)", "Mahadasha analysis", "Relationship & career insights", "Vedic remedies (Upayas)", "PDF report"],
        "whatsapp_msg": "Hi Jyogi! I'd like to book a Full Vedic Reading (₹1,500). Please let me know your availability.",
    },
    {
        "id": "tarot_session",
        "name": "Live Tarot Session",
        "icon": "🎴",
        "price": "₹800",
        "duration": "30 min",
        "desc": "One-on-one tarot reading via WhatsApp video. Ask your burning question and receive guidance from the Light Seer's deck.",
        "includes": ["3-card or 5-card spread", "Light Seer's Tarot deck", "Voice explanation", "WhatsApp video call", "Recorded session"],
        "whatsapp_msg": "Hi Jyogi! I'd like to book a Live Tarot Session (₹800). Please let me know your availability.",
    },
    {
        "id": "crystal_consult",
        "name": "Crystal Prescription",
        "icon": "💎",
        "price": "₹500",
        "duration": "20 min",
        "desc": "Based on your birth chart and current challenges, Jyogi prescribes the exact crystals and wearing protocol for you.",
        "includes": ["Chart-based crystal selection", "Wearing protocol", "Mantra recommendations", "WhatsApp follow-up", "Discount on purchase"],
        "whatsapp_msg": "Hi Jyogi! I'd like a Crystal Prescription consultation (₹500). Please let me know your availability.",
    },
    {
        "id": "numerology",
        "name": "Numerology Deep-Dive",
        "icon": "🔢",
        "price": "₹699",
        "duration": "30 min",
        "desc": "Your Life Path, Expression, Soul Urge, and Personal Year numbers decoded. Discover your life's blueprint.",
        "includes": ["Life Path analysis", "Expression number", "Soul Urge reading", "Personal Year forecast", "PDF summary"],
        "whatsapp_msg": "Hi Jyogi! I'd like a Numerology Deep-Dive session (₹699). Please let me know your availability.",
    },
]

REVIEWS = [
    {
        "user": "Anjali S.",
        "location": "Pune",
        "rating": 5,
        "product": "Money Magnet Bracelet",
        "text": "Got a promotion I had been waiting two years for — within weeks of wearing this! The energy shift was real and immediate.",
        "avatar": "A",
    },
    {
        "user": "Rahul K.",
        "location": "Delhi",
        "rating": 5,
        "product": "Vedic Reading",
        "text": "Jyogi identified my Saturn transit challenge and gave remedies that actually worked. Her predictions were frighteningly accurate.",
        "avatar": "R",
    },
    {
        "user": "Priya M.",
        "location": "Mumbai",
        "rating": 5,
        "product": "Self-Love Mala",
        "text": "Beautiful quality crystals. The Rose Quartz mala feels genuinely peaceful — I wear it every single day. My relationship with myself transformed.",
        "avatar": "P",
    },
    {
        "user": "Deepak R.",
        "location": "Bangalore",
        "rating": 5,
        "product": "Live Tarot Session",
        "text": "The live tarot reading gave me complete clarity about my career change. Every card spoke directly to my situation. Mind-blowing.",
        "avatar": "D",
    },
    {
        "user": "Meena T.",
        "location": "Hyderabad",
        "rating": 5,
        "product": "Protection Shield",
        "text": "The negative energy in my office genuinely shifted after placing the tourmaline on my desk. My colleagues even noticed the change in atmosphere.",
        "avatar": "M",
    },
    {
        "user": "Sanjay P.",
        "location": "Kolkata",
        "rating": 5,
        "product": "Full Vedic Reading",
        "text": "The PDF report is incredibly detailed. I've referred to it every month for a year and the predictions keep coming true one by one.",
        "avatar": "S",
    },
    {
        "user": "Kavita L.",
        "location": "Jaipur",
        "rating": 5,
        "product": "Third Eye Awakener",
        "text": "Started having vivid dreams and strong gut feelings after wearing this for a week. My meditation practice deepened immediately.",
        "avatar": "K",
    },
    {
        "user": "Arjun N.",
        "location": "Chennai",
        "rating": 5,
        "product": "Crystal Prescription",
        "text": "The personalised crystal prescription was worth every rupee. Jyogi explained exactly which stones suit my chart — no generic advice.",
        "avatar": "A",
    },
    {
        "user": "Sunita V.",
        "location": "Ahmedabad",
        "rating": 5,
        "product": "Lucky Charm",
        "text": "Wore the Lucky Charm to my business pitch and landed a ₹40L contract. Coincidence? I don't think so. Jyogi is the real deal.",
        "avatar": "S",
    },
]

GOD_GALLERY = [
    {
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Shiva_statue_at_Kempfort_Shiva_Temple.jpg/600px-Shiva_statue_at_Kempfort_Shiva_Temple.jpg",
        "deity": "Lord Shiva",
        "mantra": "Om Namah Shivaya",
        "meaning": "The destroyer of ego, the transformer of souls",
        "caption": "🙏",
    },
    {
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Ganesha_Basohli_miniature_circa_1730_Dubost_p73.jpg/600px-Ganesha_Basohli_miniature_circa_1730_Dubost_p73.jpg",
        "deity": "Lord Ganesha",
        "mantra": "Om Gan Ganapataye Namah",
        "meaning": "Remover of obstacles, lord of new beginnings",
        "caption": "🙏",
    },
    {
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Goddess_Lakshmi.jpg/600px-Goddess_Lakshmi.jpg",
        "deity": "Goddess Lakshmi",
        "mantra": "Om Shreem Mahalakshmiyei Namah",
        "meaning": "Goddess of wealth, beauty, and abundance",
        "caption": "🙏",
    },
]

WHATSAPP_NUMBER = "91XXXXXXXXXX"   # ← YOUR 10-digit number after 91, e.g. "919876543210"
