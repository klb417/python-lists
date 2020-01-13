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


spacecraft = [("Akatsuki", "Venus"),
              ("Cassini", "Saturn"), ("Viking", "Mars"), ("2001 Mars Odyssey", "Mars"), ("Mars Express", "Mars"), ("Curiosity", "Mars"), ("Mangalyaan", "Mars"), ("Juno", "Jupiter"), ("Voyager 1", "Jupiter", "Saturn"), ("Voyager 2", "Jupiter", "Saturn", "Uranus", "Neptune")]


for planet in planet_list:
    visited = []
    for voyage in spacecraft:
        for craft in voyage:
            if craft == planet:
                visited.append(voyage[0])
    joinedVisited = ", ".join(visited)
    print(f"{planet}: {joinedVisited}")
