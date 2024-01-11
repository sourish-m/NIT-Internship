import os
import re

files = os.listdir(".")
c_files = [filename for filename in files if os.path.splitext(filename)[1] == ".c"]

for input_filename in c_files:
    output_filename = os.path.splitext(input_filename)[0] + "_output.txt"

    with open(input_filename, "r") as file, open(output_filename, "w") as output:
        for line in file:
            tokens = re.findall(r"\b0x(..)\b", line)
            output.write("".join(tokens))

            if line.strip() == "};":
                output.write("\n")
