def search(
        log,
        terms=(
                "juice",
                "smoothie",
                "drink",
                "milk",
                "bubblywateritem",
                "freshwateritem",
                "coffeeitem",
                "coffeelonlecheitem",
                "teaitem",
                "sodaitem",
                "slushieitem",
                "cocktailitem",
                "latteitem",
                "yogurtitem",
                "tektopia:beer",
                "floatitem",
                "hotcocoaitem",
                "hotchocolateitem",
                "soupitem"
        ),
        start="\"<",
        end=">\"\n"
):
    with open(log, "r") as file:
        dump = file.readlines()

    min_length = len(start) + len(end)
    items = []
    for line in dump:
        if len(line) >= min_length and line[:len(start)] == start and line[-len(end):] == end:
            for term in terms:
                if term in line:
                    items.append(line.replace(start, "").replace(end, ""))

    return items
