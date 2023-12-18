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
    maps = [s2s, s2f, f2w, w2l, l2t, t2h, h2l]
    del splits
    del s2s
    del s2f
    del f2w
    del w2l
    del l2t
    del t2h
    del h2l
    # seeds = seeds[seeds.find(":")+2:].split(" ")
    # seeds = [int(x) for x in seeds]
    seed_range_pairs = seeds[seeds.find(":")+2:].split(" ")
    seed_range_pairs = [int(x) for x in seed_range_pairs]
    seeds = []
    for i in range(0, len(seed_range_pairs), 2):
        # start = seed_range_pairs[i]
        seeds += list(range(seed_range_pairs[i], seed_range_pairs[i]+seed_range_pairs[i+1]))
    source_list = seeds[:]
    dest_list = seeds[:]
    del seeds
    del lines
    del x
    del f
    # now using dynamic programming to find the location of each seed
    for mapping in maps:
        for i in range(len(source_list)):
            for line in mapping.split("\n")[1:]:
                dest, source, length = line.split(" ")
                source = int(source)
                dest = int(dest)
                length = int(length)
                if source_list[i] in range(source, source+length):
                    dest_list[i] = dest+(source_list[i]-source)
                    source_list[i] = dest_list[i]
                    break
                else:
                    dest_list[i] = source_list[i]
        source_list = dest_list[:]
    # for i in range(len(source_list)):
    #     for line in s2s.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if source_list[i] in range(source, source+length):
    #             dest_list[i] = dest+(source_list[i]-source)
    #             source_list[i] = dest_list[i]
    #             break
    
    # for i in range(len(seeds)):
    #     for line in s2f.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    # for i in range(len(seeds)):
    #     for line in f2w.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    # for i in range(len(seeds)):
    #     for line in w2l.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    # for i in range(len(seeds)):
    #     for line in l2t.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    # for i in range(len(seeds)):
    #     for line in t2h.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    # for i in range(len(seeds)):
    #     for line in h2l.split("\n")[1:]:
    #         dest, source, length = line.split(" ")
    #         source = int(source)
    #         dest = int(dest)
    #         length = int(length)
    #         if out[i][0] in range(source, source+length):
    #             out[i][1] = dest+(out[i][0]-source)
    #             out[i][0] = out[i][1]
    #             break
    #         else:
    #             out[i][1] = out[i][0]
    
    return dest_list
def main():
    mappings = read_input_2("input5.txt")
    # print(f"{'Seed':<8}\t{'Soil':<8}\t{'Fertilizer':<12}\t{'Water':<8}\t{'Light':<8}\t{'Temperature':<12}\t{'Humidity':<8}\t{'Location':<8}")
    print(min(mappings))

    # print(lowest)


if __name__ == "__main__":
    main()
