import os

def run(path):
  outs = {}
  for line in open(path):
    a, b = line.strip().split(",", 1)
    a = int(a)
    b = b.strip()
    if b.lower() == "empty":
      outs[a] = []
    else:
      vals = []
      for x in b.strip("{}").split(","):
        x = x.strip()
        if x:
          vals.append(int(x))
      outs[a] = vals

  for t in outs.values():
    for j in t:
      if j not in outs:
        outs[j] = []

  states = sorted(outs)

  def fill(t, k):
    if t not in k:
      k.append(t)
      for j in outs[t]:
        fill(j, k)

  for s in states:
    k = []
    fill(s, k)
    k.sort()

    result = ""
    for i in range(len(k)):
      if i > 0:
        result += ","
      result += str(k[i])
    print("E(" + str(s) + ") = {" + result + "}")

def main():
  for name in sorted(n for n in os.listdir(".") if n.endswith(".txt")):
    print(f"=== {name} ===")
    run(name)
    print()

if __name__ == "__main__":
  main()