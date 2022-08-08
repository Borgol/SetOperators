"""Performs Set-based operations following a specific
syntax.

I'm aware the set type and its functions exits, but am not
allowed to use them.
"""

FILE_PATH = "input.txt"


def make_faux_set(l: list) -> list:
    """Creates a fake set from the provided list."""
    final = []
    for i in l:
        if i not in final:
            final.append(i)
    return final


def do_cartesian_product(a: list, b: list) -> list:
  final = []
  for x in a:
    for y in b:
      final.append((x, y))
  return make_faux_set(final)
    


def execute_funny_input(lines: list) -> None:
    instr_count = int(lines[0])
    del lines[0]
    if len(lines) < instr_count * 3:
        raise SyntaxError(
            "File contains less instructions than instr_count.")

    for i in range(0, len(lines), 3):
        instr = lines[i][0]
        set_a = make_faux_set(lines[i + 1][:-1].split(","))
        set_b = make_faux_set(lines[i + 2][:-1].split(","))
      
        result = []
        r_char = ""
      
        if instr == "U":
            result = make_faux_set(set_a + set_b)
            r_char = "\u222A"
        elif instr == "I":
            result = make_faux_set([i for i in set_a if i in set_b])
            r_char = "\u2229"
        elif instr == "D":
            result = make_faux_set([i for i in set_a if i not in set_b])
            r_char = "-"
        elif instr == "C":
            result = do_cartesian_product(set_a, set_b)
            r_char = "\u2A2F"
          
        print(f"{set_a} {r_char} {set_b} = {result}")


def main():
    with open(FILE_PATH) as f:
        t = f.readlines()
        if not t[-1].endswith("\n"):
            t[-1] += "\n"
        execute_funny_input(t)


if __name__ == "__main__":
    main()