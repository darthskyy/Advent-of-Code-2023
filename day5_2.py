def read_input_2(file_name: str):
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

    # seeds = seeds[seeds.find(":")+2:].split(" ")
    # seeds = [int(x) for x in seeds]
    seed_range_pairs = seeds[seeds.find(":")+2:].split(" ")
    seed_range_pairs = [int(x) for x in seed_range_pairs]
    seeds = []
    for i in range(0, len(seed_range_pairs), 2):
        # start = seed_range_pairs[i]
        seeds += list(range(seed_range_pairs[i], seed_range_pairs[i]+seed_range_pairs[i+1]))
    out = []
    
    for i, seed in enumerate(seeds):
        out.append([seed, "", "", "", "", "", "", ""])
        for line in s2s.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if seed in range(source, source+length):
                out[i][1] = dest+(seed-source)
                break
            else:
                out[i][1] = seed
    
    for i in range(len(seeds)):
        for line in s2f.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][1] in range(source, source+length):
                out[i][2] = dest+(out[i][1]-source)
                break
            else:
                out[i][2] = out[i][1]
    
    for i in range(len(seeds)):
        for line in f2w.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][2] in range(source, source+length):
                out[i][3] = dest+(out[i][2]-source)
                break
            else:
                out[i][3] = out[i][2]
    
    for i in range(len(seeds)):
        for line in w2l.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][3] in range(source, source+length):
                out[i][4] = dest+(out[i][3]-source)
                break
            else:
                out[i][4] = out[i][3]
    
    for i in range(len(seeds)):
        for line in l2t.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][4] in range(source, source+length):
                out[i][5] = dest+(out[i][4]-source)
                break
            else:
                out[i][5] = out[i][4]
    
    for i in range(len(seeds)):
        for line in t2h.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][5] in range(source, source+length):
                out[i][6] = dest+(out[i][5]-source)
                break
            else:
                out[i][6] = out[i][5]
    
    for i in range(len(seeds)):
        for line in h2l.split("\n")[1:]:
            dest, source, length = line.split(" ")
            source = int(source)
            dest = int(dest)
            length = int(length)
            if out[i][6] in range(source, source+length):
                out[i][7] = dest+(out[i][6]-source)
                break
            else:
                out[i][7] = out[i][6]
    
    return out
def main():
    mappings = read_input_2("input5.txt")
    print(f"{'Seed':<8}\t{'Soil':<8}\t{'Fertilizer':<12}\t{'Water':<8}\t{'Light':<8}\t{'Temperature':<12}\t{'Humidity':<8}\t{'Location':<8}")
    lowest = 10000000000000000000000000000000000000000
    for mapping in mappings:
        print(f"{mapping[0]:<8}\t{mapping[1]:<8}\t{mapping[2]:<12}\t{mapping[3]:<8}\t{mapping[4]:<8}\t{mapping[5]:<12}\t{mapping[6]:<8}\t{mapping[7]:<8}")
        lowest = min(lowest, mapping[7])

    print(lowest)


if __name__ == "__main__":
    main()
