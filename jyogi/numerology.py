def calculate_life_path(date_str: str) -> int:
    # date_str: YYYY-MM-DD
    digits = [int(c) for c in date_str if c.isdigit()]
    s = sum(digits)
    while s > 9 and s not in (11, 22, 33):
        s = sum(int(c) for c in str(s))
    return s

def get_detailed_report(lp: int) -> dict:
    # Minimal defaults. Replace with your full dataset.
    titles = {
        1: "Leader", 2: "Diplomat", 3: "Creator", 4: "Builder", 5: "Explorer",
        6: "Healer", 7: "Seeker", 8: "Executive", 9: "Humanitarian",
        11: "Visionary", 22: "Master Builder", 33: "Master Teacher"
    }
    gems = {
        1: "Ruby", 2: "Pearl", 3: "Yellow Sapphire", 4: "Emerald", 5: "Diamond",
        6: "Opal", 7: "Cat's Eye", 8: "Blue Sapphire", 9: "Red Coral",
        11: "Amethyst", 22: "Topaz", 33: "Aquamarine"
    }
    colors = {
        1: "Red", 2: "White", 3: "Yellow", 4: "Green", 5: "Sky Blue",
        6: "Pink", 7: "Violet", 8: "Navy", 9: "Orange",
        11: "Purple", 22: "Gold", 33: "Teal"
    }
    return {"title": titles.get(lp, "Path"), "lucky_gem": gems.get(lp, "Emerald"), "lucky_color": colors.get(lp, "White")}
