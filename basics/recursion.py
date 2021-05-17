def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# 6 = 6 + fun(5) = 6 + 15 = 21
# 5 = 5 + fun(4) = 5 + 10 = 15
# 4 = 4 + fun(3) = 4 + 6 = 10
# 3 = 3 + fun(2) = 3 + 3 = 6
# 2 = 2 + fun(1) = 2 + 1 = 3
# 1 = 1 + fun(0) = 1 + 0 = 1
# 0 = 0