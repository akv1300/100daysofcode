travel_log = [
{
    "country" : "France",
    "visits" : 12,
    "cities" : ["Paris", "Lille", "Dijon"]
},
{
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berlin", "Hamburg", "Stuttgart"]
}]


def add_new_country (country, visit, cities):
    travel_log.append( {
        "country" : country,
        "visits" : visit,
        "cities" : cities
    })
add_new_country("India", 13, "Delhi")
print(travel_log)
