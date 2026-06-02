# принимает city, country, и опциональный population
# возвращает строку формата "Santiago, Chile"
# или "Santiago, Chile - population 5000000"

def city_country(country, city, population=''):
    if population:
        location_population = f'{country}, {city}, population - {population}'
    else:
        location_population = f'{country}, {city}'
    return location_population.title()
