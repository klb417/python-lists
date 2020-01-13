planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del(planet_list[8])

# rocky_planets = planet_list[0:4]
# rocky_planets = planet_list[1:4]
# rocky_planets = planet_list[3:]
# rocky_planets = planet_list[:3]
# rocky_planets = planet_list[4:-1]
