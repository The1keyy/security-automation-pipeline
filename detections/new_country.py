def detect_new_country(event, known_countries):
    country = event["country"]

    if country not in known_countries:
        return True, country

    return False, country
