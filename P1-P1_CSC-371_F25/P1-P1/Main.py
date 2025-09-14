import sys

def add_once(i, item):
    if item not in i:
        i.append(item)

def union(a, b):
    out = []
    for i in a:
        add_once(out, i)
    for i in b:
        add_once(out, i)
    return out

def concat(a, b):
    result = []
    for i in a:
        for k in b:
            add_once(result, i + k)
    return result

def power(a, i):
    if i == 0:
        return [""]
    out = a[:]
    count = 1
    while count < i:
        out = concat(out, a)
        count += 1
    return out

def display_set(items):
    return "{" + ", ".join("ε" if s == "" else s for s in items) + "}"

def read(line):
    line = line.strip().replace("{", "").replace("}", "")
    words = []
    for i in line.split(","):
        k = i.strip()
        if k and k not in words:
            words.append(k)
    return words

def run_each(path, k):
    a_line = ""
    b_line = ""
    with open(path) as f:
        for j in f:
            line = j.strip()
            if not line:
                continue
            if a_line == "":
                a_line = line
            elif b_line == "":
                b_line = line
                break

    print(f"\nResults for {path} below:")

    if a_line == "" or b_line == "":
        print("Needs two non-empty lines (A then B).")
        return

    A = read(a_line)
    B = read(b_line)

    print("A U B =", display_set(union(A, B)))
    print("A o B =", display_set(concat(A, B)))
    print(f"A^{k} =", display_set(power(A, k)))

def main():
    paths = sys.argv[1:]
    if not paths:
        line = input("Enter .txt paths separated each with space: ").strip()
        paths = line.split() if line else []
    if not paths:
        print("No files.")
        return

    k_str = input("Enter k (0 or more): ").strip()
    if not k_str.isdigit():
        print("k must be 0 or more.")
        return
    k = int(k_str)

    for p in paths:
        try:
            run_each(p, k)
        except FileNotFoundError:
            print(f"\n{p} not found.")

if __name__ == "__main__":
    main()
