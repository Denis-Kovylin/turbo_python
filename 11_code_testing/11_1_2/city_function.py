def city_country(country, city, population=""):
    """Возвращает строку формата 'Country, City' или 'Country, City, Population - N'."""
    if population:
        location_population = f"{country}, {city}, population - {population}"
    else:
        location_population = f"{country}, {city}"
    return location_population.title()
