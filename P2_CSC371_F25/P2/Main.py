import os

def f1(c):
  if c >= "A":
    if c <= "Z":
      return 1
  return 0

def f2(a, b):
  for y in a:
    if y == b:
      return 1
  return 0

def run(path):
  g = {}
  s = ""

  print("Input:")
  for l in open(path):
    t = l.rstrip("\n")
    print(t)

    x = t.strip()
    q = x.split("-", 1)
    if x != "":
      if len(q) == 2:
        a = q[0].strip()
        b = q[1].strip()
        if s == "":
          s = a
        u = []
        for w in b.split("|"):
          u.append(w.strip())
        g[a] = u

  print("\nOutput:")

  if s == "":
    return

  n = []
  while 1:
    c = 0
    for a in g:
      if a not in n:
        u = g[a]
        for w in u:
          if w == "0":
            n.append(a)
            c = 1
            break
          if w != "":
            j = 0
            k = 1
            while j < len(w):
              d = w[j]
              if f1(d) == 1:
                if d in n:
                  j = j + 1
                else:
                  k = 0
                  break
              else:
                k = 0
                break
            if k == 1:
              n.append(a)
              c = 1
              break
    if c == 0:
      break

  h = {}
  for a in g:
    u = g[a]
    v = []
    for w in u:
      if w != "0":
        z = [""]
        i = 0
        while i < len(w):
          d = w[i]
          p = []
          if f1(d) == 1 and d in n:
            j = 0
            while j < len(z):
              x = z[j]
              p.append(x + d)
              p.append(x)
              j = j + 1
          else:
            j = 0
            while j < len(z):
              x = z[j]
              p.append(x + d)
              j = j + 1
          z = p
          i = i + 1
        i = 0
        while i < len(z):
          t = z[i]
          if t != "":
            if f2(v, t) == 0:
              v.append(t)
          i = i + 1
    if len(v) > 0:
      h[a] = v

  g = h

  q = []
  while 1:
    c = 0
    for a in g:
      if a not in q:
        u = g[a]
        for w in u:
          j = 0
          b = 0
          while j < len(w):
            d = w[j]
            if f1(d) == 1:
              if d not in q:
                b = 1
                break
            j = j + 1
          if b == 0:
            q.append(a)
            c = 1
            break
    if c == 0:
      break

  h = {}
  for a in g:
    if a in q:
      u = g[a]
      v = []
      for w in u:
        j = 0
        b = 0
        while j < len(w):
          d = w[j]
          if f1(d) == 1:
            if d not in q:
              b = 1
              break
          j = j + 1
        if b == 0:
          if f2(v, w) == 0:
            v.append(w)
      if len(v) > 0:
        h[a] = v

  g = h

  x = []

  def f3(a):
    if a in x:
      return
    if a not in g:
      return
    x.append(a)
    u = g[a]
    i = 0
    while i < len(u):
      w = u[i]
      j = 0
      while j < len(w):
        d = w[j]
        if f1(d) == 1:
          if d not in x:
            f3(d)
        j = j + 1
      i = i + 1

  f3(s)

  h = {}
  for a in g:
    if a in x:
      h[a] = g[a]

  g = h

  h = {}
  for a in g:
    u = g[a]
    v = []
    for w in u:
      k = 1
      if len(w) == 1:
        if f1(w[0]) == 1:
          if w[0] == a:
            k = 0
      if k == 1:
        v.append(w)
    if len(v) > 0:
      h[a] = v

  g = h

  y = []
  for a in g:
    y.append(a)
  y.sort()

  if s in y:
    y.remove(s)
    y.insert(0, s)

  for a in y:
    u = g[a]
    l = a + "-"
    i = 0
    while i < len(u):
      if i > 0:
        l = l + "|"
      l = l + u[i]
      i = i + 1
    print(l)

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
