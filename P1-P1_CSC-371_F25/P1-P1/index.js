/*
inPostTree(inOrder, postOrder, inLeft, inRight, postLeft, postRight) -> root
  if (inLeft >= inRight || postLeft >=) postRight: return null

  rootVal <- postOrder[postRight - 1]

  split <- -1
  for (int i = inLeft; i < inRight; i++):
    if inOrder[i] == rootVal:
      split <- i
      break
  if split == -1: return null

  leftSize <- split - inLeft

  root <- new Node(rootVal)
  root.left  <- inPostTree(inOrder, postOrder, inLeft, split, postLeft, postLeft + leftSize)
  root.right <- inPostTree(inOrder, postOrder, split + 1, inRight, postLeft + leftSize, postRight - 1)
  
  return root
*/
