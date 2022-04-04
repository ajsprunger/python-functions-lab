def sum_to(n):
  return(n * (n+1) // 2)

print(sum_to(10))

def largest(list):
  return max(list)

print(largest([1, 3, 5, 6, 8]))

def occurences(str1, str2):
  return str1.count(str2)

print(occurences('alasdlf;jklkjasdf', 'a'))

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(3, 2, 2))