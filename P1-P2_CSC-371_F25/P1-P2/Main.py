import os

def run(path):
  print("Input:")
  for line in open(path):
    print(line.rstrip("\n"))
  print("\nOutput:")

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

  rest = []
  for t in outs.values():
    for j in t:
      if j not in outs and j not in rest:
        rest.append(j)
  
  for j in rest:
    outs[j] = []

  states = sorted(outs)

  def close(t, k):
    if t not in k:
      k.append(t)
      for j in outs[t]:
        close(j, k)

  for s in states:
    k = []
    close(s, k)
    k.sort()

    result = ""
    for i in range(len(k)):
      if i > 0:
        result += ","
      result += str(k[i])
    print("E(" + str(s) + ") = {" + result + "}")

def main():
  files = []
  for n in os.listdir("."):
    if n.endswith(".txt"):
      files.append(n)
  files.sort()

  for name in files:
    print(f"=== {name} ===")
    run(name)
    print()
      
if __name__ == "__main__":
  main()