import random as rand


transitions = {"<BOL>": []}
corpus = ""

with open("author-quotes.txt", "r") as cct:
    corpus = cct.read()
    cct.seek(0)
    for line in cct.readlines():
        words = line[:-1].split(" ") #.split("\t")[1]
        words.append("<EOL>")
        transitions["<BOL>"] += [words[0]]
        # print(words[0])
        words = ["<BOL>"] + words
        for i in range(1, len(words) - 1):
            index = f"{words[i-1]} {words[i]}"
            # print(index)
            transitions[index] = (transitions.get(index) or []) + [words[i+1]]


def generate(prune_duplicates=True):
    retval = None
    while retval is None:
        first_word = rand.choice(transitions["<BOL>"])
        words = [first_word, rand.choice(transitions[f"<BOL> {first_word}"])]
        while not words[-1] == "<EOL>":
            # print(words)
            windex = f"{words[-2]} {words[-1]}"
            words += [rand.choice(transitions[windex])]
        text = " ".join(words[:-1])
        rtvl = text.replace(" \\n\\n ", "\n\n").replace(" \\n ", "\n")
        # runs += 1
        if text not in corpus or prune_duplicates is False:
            # dups += 1
            retval = rtvl
    return retval


if __name__ == "__main__":
    print(generate())
