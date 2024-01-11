import csv

input_file = "data.txt"
tokensize = 32
slide = 16


def tokenizer(line, tokensize):
    length = len(line)

    return [line[i : i + tokensize] for i in range(0, length, slide)]


with open(input_file, "r") as input, open("data.csv", "w", newline="") as csvfile:
    output = csv.writer(csvfile, delimiter=",")
    # , quoting=csv.QUOTE_NONE, escapechar='\n', lineterminator='')

    for line in input:
        token_list = tokenizer(line, tokensize)
        token_list = [x for x in token_list if "\n" not in x]
        output.writerow(token_list)
        # print(tokenizer(line, tokensize))
