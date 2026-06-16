"""Deterministic AI-flavoured itinerary, packing, budget and journal generators (no LLM needed)."""
import random
from datetime import date, timedelta

# ---------------- Itinerary ----------------
EXPERIENCES = {
    "Mountains": [
        "sunrise viewpoint walk", "ridge-line trek", "local monastery visit",
        "alpine café morning", "starlight stargazing dinner", "village homestay tea ritual",
        "snowline drive", "yak / shepherd encounter", "high-altitude lake picnic",
    ],
    "Beaches": [
        "sunrise yoga on the sand", "secret cove kayak", "shack seafood lunch",
        "sunset cruise with dolphins", "tide-pool exploration", "beach bonfire & live music",
        "fishing village photo walk", "scuba intro dive", "candlelit beach dinner",
    ],
    "Heritage": [
        "guided fort sunrise tour", "old-city heritage walk", "block-print workshop",
        "step-well photography", "royal palace courtyard breakfast", "puppet folk show evening",
        "haveli rooftop dinner", "artisan bazaar visit", "carriage / vintage car ride",
    ],
    "Wildlife": [
        "dawn jeep safari", "naturalist-led bird walk", "river dolphin or croc spotting",
        "elephant interaction (ethical)", "night-jungle stay", "tribal village visit",
        "tracking pugmarks with a guide", "canopy walk", "conservation centre tour",
    ],
    "Spiritual": [
        "predawn aarti by the river", "temple corridor walk", "meditation under a banyan",
        "ashram tea conversation", "lamp-lit evening puja", "sacred chant session",
        "vegetarian thali at the langar", "candle-float on the holy waters", "monastery stay",
    ],
    "Adventure": [
        "river rafting half-day", "paragliding from the ridge", "rock climbing session",
        "via ferrata or canyoning", "mountain biking downhill", "bungee jump",
        "wild camping under stars", "multi-pitch trek", "ice skating / skiing",
    ],
    "Cities": [
        "coffee crawl through hip neighbourhoods", "rooftop bar sunset", "design district walk",
        "Michelin-style tasting dinner", "vintage market hunt", "local art-gallery hop",
        "live music venue night", "metro photo walk", "speakeasy cocktail tasting",
    ],
    "Hidden Gems": [
        "uncrowded viewpoint hike", "village homestay dinner", "secret waterfall plunge",
        "tribal craft workshop", "abandoned monastery exploration", "wild-camp by a lake",
        "local market without a single tourist", "shepherd's tea on a cliff",
    ],
}

VIBES = {
    "Slow & Romantic": ["candlelit dinner", "spa massage", "lake-side breakfast"],
    "Adventure & Adrenaline": ["adrenaline activity", "high-altitude trek", "river expedition"],
    "Heritage & Culture": ["heritage walk", "museum visit", "folk performance"],
    "Foodie": ["street-food tour", "cooking class", "spice market visit"],
    "Wellness & Spiritual": ["yoga session", "meditation hour", "Ayurveda consult"],
    "Family Fun": ["amusement park", "boat ride", "wildlife park"],
}


def generate_itinerary(destination_name: str, category: str, days: int, vibes: list[str], budget_total: int, interests: list[str]) -> list[dict]:
    rnd = random.Random(hash(destination_name) ^ days ^ len(vibes))
    cat_pool = list(EXPERIENCES.get(category, EXPERIENCES["Heritage"]))
    rnd.shuffle(cat_pool)
    vibe_acts = []
    for v in vibes:
        vibe_acts.extend(VIBES.get(v, []))
    rnd.shuffle(vibe_acts)
    interest_acts = [f"deep dive into {i.lower()}" for i in interests]
    rnd.shuffle(interest_acts)

    per_day_budget = max(1500, budget_total // max(1, days))

    plan = []
    for d in range(1, days + 1):
        if d == 1:
            theme = "Arrival & First Impressions"
        elif d == days:
            theme = "Farewell & Final Memories"
        elif d == 2 and days >= 4:
            theme = "Adventure & Discovery"
        elif d == days - 1 and days >= 4:
            theme = "Culture, Cuisine & Calm"
        else:
            theme = rnd.choice(["Exploration & Wonder", "Hidden Trails", "Local Soul", "Slow Indulgence"])

        morning = cat_pool[(d - 1) % len(cat_pool)].title()
        afternoon = (vibe_acts[(d - 1) % len(vibe_acts)] if vibe_acts else cat_pool[d % len(cat_pool)]).title()
        evening = (interest_acts[(d - 1) % len(interest_acts)] if interest_acts else rnd.choice([
            "rooftop dinner with city lights", "live folk music gathering", "stargazing with hot chocolate",
            "old town night walk", "boutique boutique shopping",
        ])).title()

        plan.append({
            "day": d,
            "theme": theme,
            "morning": morning,
            "afternoon": afternoon,
            "evening": evening,
            "budget_inr": per_day_budget,
            "stay": _stay_for(category, rnd),
            "food": _food_for(destination_name, category, rnd),
        })
    return plan


def _stay_for(cat: str, rnd) -> str:
    options = {
        "Mountains": ["timber-and-stone lodge", "alpine boutique hotel", "homestay with valley view"],
        "Beaches": ["beachfront villa", "boho ocean shack", "coral-stone boutique"],
        "Heritage": ["restored haveli", "heritage palace hotel", "old-city courtyard stay"],
        "Wildlife": ["jungle eco-lodge", "tented river camp", "tree-house retreat"],
        "Spiritual": ["riverside ashram cottage", "monastery guesthouse", "yoga retreat villa"],
        "Adventure": ["climbing base camp", "cliff-edge tents", "rafting riverside lodge"],
        "Cities": ["design boutique hotel", "rooftop loft", "heritage townhouse"],
        "Hidden Gems": ["family homestay", "off-grid eco-cabin", "shepherd's stone cottage"],
    }
    return rnd.choice(options.get(cat, options["Heritage"]))


def _food_for(dest: str, cat: str, rnd) -> str:
    base = {
        "Mountains": ["thukpa & momos", "trout grill", "wood-fired pizza at the ridge", "Tibetan butter tea"],
        "Beaches": ["grilled prawns", "fish thali", "coconut curry with rice", "feni cocktail tasting"],
        "Heritage": ["royal thali platter", "kebab tasting", "rooftop biryani", "saffron rasgulla"],
        "Wildlife": ["village kitchen meal", "campfire BBQ", "tribal foraged greens", "spiced chai under stars"],
        "Spiritual": ["temple langar lunch", "satvik thali", "lemon-rice & curd", "kahwa or filter coffee"],
        "Adventure": ["high-protein adventure bowl", "campfire stew", "energy parathas", "post-trek hot chocolate"],
        "Cities": ["chef's tasting menu", "craft beer & food pairing", "midnight street-food crawl", "speakeasy cocktail"],
        "Hidden Gems": ["village family dinner", "foraged-greens curry", "fresh river fish", "homemade rice wine"],
    }
    return rnd.choice(base.get(cat, base["Heritage"]))


# ---------------- Packing ----------------
PACKING_TEMPLATES = {
    "base": [
        "Photo ID + passport + visa printout",
        "Comfortable walking shoes",
        "Refillable steel water bottle",
        "Universal power adapter (Type C/D/M)",
        "Power bank 10,000 mAh+",
        "Sunscreen SPF 50",
        "Sunglasses (UV-protected)",
        "Personal medicines + ORS sachets",
        "Hand sanitizer + wet wipes",
        "Reusable cloth bag",
    ],
    "Mountains": [
        "Thermal innerwear top & bottom",
        "Fleece mid-layer",
        "Down jacket / heavy puffer",
        "Waterproof shell",
        "Woollen socks (3 pairs)",
        "Gloves + woollen cap",
        "Trekking shoes with grip",
        "Lip balm + heavy moisturiser",
        "Diamox (consult doctor) for altitude",
    ],
    "Beaches": [
        "Swimwear (2 sets)",
        "Quick-dry towel",
        "Flip-flops + light sandals",
        "Wide-brim hat",
        "Reef-safe sunscreen",
        "Dry-bag for electronics",
        "Light cotton dresses / shorts",
        "Mosquito repellent (DEET 20%+)",
    ],
    "Heritage": [
        "Modest clothing (shoulders/knees covered for temples)",
        "Scarf / dupatta for religious sites",
        "Comfortable walking shoes (lots of walking)",
        "Light layers (warm days, cool evenings)",
        "Camera + extra battery",
    ],
    "Wildlife": [
        "Earth-tone clothing (avoid bright colours)",
        "Long sleeves + trousers (mosquito protection)",
        "Closed shoes",
        "Binoculars",
        "Mosquito repellent",
        "Cap + sunscreen",
        "Quiet zip pouches (no rustling on safari)",
    ],
    "Spiritual": [
        "Modest cotton clothing",
        "Scarf / shawl",
        "Easy slip-on footwear (frequent removal)",
        "Notebook / journal",
        "Light meditation cushion (optional)",
    ],
    "Adventure": [
        "Sport sandals + grippy shoes",
        "Quick-dry sports clothing",
        "Compression base layers",
        "Compact rain shell",
        "Personal first-aid kit",
        "Action camera mount",
        "Energy bars / dry fruit",
    ],
    "Cities": [
        "Smart casual outfits (2–3)",
        "Comfortable sneakers",
        "Light jacket",
        "Crossbody bag (anti-theft)",
        "Cards + small cash mix",
    ],
    "Hidden Gems": [
        "Compact daypack",
        "Headlamp + spare batteries",
        "Multi-tool / pocket knife",
        "Extra cash (ATMs scarce)",
        "Offline maps downloaded",
        "Lightweight sleeping bag liner",
    ],
}


def generate_packing(category: str, days: int, season: str = ""):
    items = list(PACKING_TEMPLATES["base"])
    items += PACKING_TEMPLATES.get(category, [])
    # Add clothing count based on days
    items.append(f"{min(days, 7)} top layers (cotton tees / shirts)")
    items.append(f"{max(2, days // 2)} bottoms (trousers / shorts)")
    items.append(f"{max(3, days)} sets of inner-wear & socks")
    if "Dec" in season or "Jan" in season or "Feb" in season:
        items.append("Extra warm layer for winter nights")
    if "Jul" in season or "Aug" in season or "Sep" in season:
        items.append("Compact umbrella / rain poncho")
    return items


# ---------------- Budget ----------------
def budget_breakdown(total: int, days: int, style: str = "Mid-range"):
    weights = {
        "Backpacker":   {"Stay": 0.25, "Food": 0.20, "Transport": 0.25, "Activities": 0.15, "Shopping": 0.05, "Buffer": 0.10},
        "Mid-range":    {"Stay": 0.35, "Food": 0.20, "Transport": 0.18, "Activities": 0.15, "Shopping": 0.05, "Buffer": 0.07},
        "Premium":      {"Stay": 0.45, "Food": 0.18, "Transport": 0.15, "Activities": 0.12, "Shopping": 0.05, "Buffer": 0.05},
        "Luxury":       {"Stay": 0.55, "Food": 0.15, "Transport": 0.12, "Activities": 0.10, "Shopping": 0.04, "Buffer": 0.04},
    }
    w = weights.get(style, weights["Mid-range"])
    return {k: int(total * v) for k, v in w.items()}


def affordability_score(total: int, days: int, style: str):
    daily = total / max(1, days)
    benchmark = {"Backpacker": 1500, "Mid-range": 3500, "Premium": 7500, "Luxury": 15000}[style]
    ratio = daily / benchmark
    score = max(0, min(100, int(60 + (ratio - 1) * 50)))
    if ratio < 0.8:
        verdict = "Tight — consider hostels, sleeper trains and street food."
    elif ratio < 1.2:
        verdict = "Comfortable mid-range — well balanced budget."
    elif ratio < 2.0:
        verdict = "Generous — room for boutique stays and signature meals."
    else:
        verdict = "Luxurious — palaces, private tours and Michelin-style dining."
    return score, verdict


# ---------------- Journal ----------------
def journal_story(title: str, location: str, body: str) -> str:
    """Compose an editorial-style narrative without any external LLM."""
    if not body.strip():
        return "Tell me what happened, what you saw, what surprised you — and I'll weave it into a story."
    sentences = [s.strip() for s in body.replace("\n", " ").split(".") if s.strip()]
    opening = f"In {location}, time wore a different fabric." if location else "Somewhere along the way, time wore a different fabric."
    middle = " ".join(sentences[:3])
    feeling = "What lingers now is not the geography but the texture of the day — the light, the laughter, the small details that refused to be forgotten."
    closing = (
        "This is the kind of memory that doesn't ask to be remembered. "
        "It simply finds you, years later, on an ordinary afternoon — and brings you back."
    )
    return (
        f"**{title}**\n\n"
        f"*{opening}*\n\n"
        f"{middle}{'.' if middle and not middle.endswith('.') else ''}\n\n"
        f"{feeling}\n\n"
        f"_{closing}_"
    )


# ---------------- Misc helpers ----------------
def date_range(start: date, days: int):
    return [start + timedelta(days=i) for i in range(days)]
