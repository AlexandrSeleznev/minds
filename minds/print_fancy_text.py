# Interactive shell prints fancy text

S = " "
S2 = "  "
V2 = "**"
V = "*"

ABC = {
    "a": [[S,V,V2,V,S],
          [V2,S2,V2],
          [V2,V2,V2],
          [V2,S2,V2],
          [V2,S2,V2]],
    "h": [[V2,S2,V2],
          [V2,S2,V2],
          [V2,V2, V2],
          [V2,S2,V2],
          [V2,S2,V2]],
    "e": [[V2,V2,V2],
          [V2,S2,S2],
          [V2,V2,V2],
          [V2,S2,S2],
          [V2,V2,V2]],
    "l": [[V2,S2,S2],
          [V2,S2,S2],
          [V2,S2,S2],
          [V2,S2,S2],
          [V2,V2,V2]],
    "o": [[S,V,V2,V,S],
          [V2,S2,V2],
          [V2,S2,V2],
          [V2,S2,V2],
          [S,V,V2,V,S]],
    "v": [[V2,S2,V2],
          [V2,S2,V2],
          [V2,S2,V2],
          [S,V2,V2,S],
          [S2,V2,S2]],
    "r": [[V2,V2,V,S],
          [V2,S2,V2],
          [V2,V2,V,S],
          [V2,S2,V2,],
          [V2,S2,V2]],
    "d": [[V2,V2,V,S],
          [V2,S2,V2],
          [V2,S2,V2],
          [V2,S2,V2],
          [V2,V2,V,S]],
    " ": [S2, S2, S2, S2, S2], # space between words
}


def build_fancy_grids(user_input):
    fancy_grids = []
    for c in user_input:
        if ABC.get(c.lower()) is None:
            print("Char '%s' is omitted, not implemented yet." % c)
            continue
        fancy_grids.append(ABC.get(c.lower()))
        # append space between letters
        fancy_grids.append([S, S, S, S, S])
    return fancy_grids


def generate_fancy_text(fancy_grids):
    for zipped_list in zip(*fancy_grids):
        fancy_text = []
        [fancy_text.extend(t) for t in zipped_list]
        print(''.join(fancy_text))


if __name__ == "__main__":
    user_input = input(
        "Hi! Type some text using '%s' characters, please.\n" % ",".join(ABC.keys())) 
    while (user_input.lower() != "bye"):
        fancy_grids = build_fancy_grids(user_input)
        generate_fancy_text(fancy_grids)
        user_input = input("Try again or say 'bye'.\n")
    print(user_input)
