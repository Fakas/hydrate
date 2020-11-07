def generate_drinks(names, thirst=6, hydration=0.7, poison_chance=0.0):
    drinks = []
    for name in names:
        drinks.append({
            "item": {
                "name": name,
                "metadata": 0
            },
            "thirst": thirst,
            "hydration": hydration,
            "poisonChance": poison_chance
        })

    return drinks
