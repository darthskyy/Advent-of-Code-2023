def read_input(file_name: str):
    lines = []
    splits =[]
    with open(file_name) as f:
        x = f.read()
        splits = x.split("\n\n")
        for line in f:
            lines.append(line.strip())
    
    """
    seeds and seed-to-soil, soil-to-fertilizer, fertilizer-to-water, water-to-light, light-to-temperature, temperature-to-humidity, humidity-to-location maps
    """
    seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l = splits

    s2s_map = {}
    s2f_map = {}
    f2w_map = {}
    w2l_map = {}
    l2t_map = {}
    t2h_map = {}
    h2l_map = {}

    for line in s2s.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            s2s_map[source+i] = dest+i
    
    for line in s2f.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            s2f_map[source+i] = dest+i
    
    for line in f2w.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            f2w_map[source+i] = dest+i
    
    for line in w2l.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            w2l_map[source+i] = dest+i
    
    for line in l2t.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            l2t_map[source+i] = dest+i
    
    for line in t2h.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            t2h_map[source+i] = dest+i
    
    for line in h2l.split("\n")[1:]:
        dest, source, length = line.split(" ")
        source = int(source)
        dest = int(dest)
        length = int(length)
        for i in range(length):
            h2l_map[source+i] = dest+i
    

    
    seeds = seeds[seeds.find(":")+2:].split(" ")
    seeds = [int(x) for x in seeds]

    
    return [seeds, s2s_map, s2f_map, f2w_map, w2l_map, l2t_map, t2h_map, h2l_map]


def get_map(seed: int, s2s_map: dict, s2f_map: dict, f2w_map: dict, w2l_map: dict, l2t_map: dict, t2h_map: dict, h2l_map: dict):
    soil = s2s_map[seed] if seed in s2s_map else seed
    fertilizer = s2f_map[soil] if soil in s2f_map else soil
    water = f2w_map[fertilizer] if fertilizer in f2w_map else fertilizer
    light = w2l_map[water] if water in w2l_map else water
    temperature = l2t_map[light] if light in l2t_map else light
    humidity = t2h_map[temperature] if temperature in t2h_map else temperature
    location = h2l_map[humidity] if humidity in h2l_map else humidity
    return [soil, fertilizer, water, light, temperature, humidity, location]
def main():
    seeds, s2s_map, s2f_map, f2w_map, w2l_map, l2t_map, t2h_map, h2l_map = read_input("input5_demo.txt")
    # print(f"{'Seed':<8}\t{'Soil':<8}\t{'Fertilizer':<12}\t{'Water':<8}\t{'Light':<8}\t{'Temperature':<12}\t{'Humidity':<8}\t{'Location':<8}")
    lowest = 10000000000000000000000000000000000000000
    for seed in seeds:
        soil, fertilizer, water, light, temperature, humidity, location = get_map(seed, s2s_map, s2f_map, f2w_map, w2l_map, l2t_map, t2h_map, h2l_map)
        lowest = min(lowest, location)
        # print(f"{seed:<8}\t{soil:<8}\t{fertilizer:<12}\t{water:<8}\t{light:<8}\t{temperature:<12}\t{humidity:<8}\t{location:<8}")

    print(lowest)


if __name__ == "__main__":
    main()
