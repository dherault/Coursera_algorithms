#!/usr/bin/python3.5
# import sys

def merge_sort(array):
  n = len(array)

  if n <= 1: return array

  n_by_2 = int(n / 2)

  A = merge_sort(array[:n_by_2])
  B = merge_sort(array[n_by_2:])
  C = []
  i = 0
  j = 0
  # len_A = n_by_2
  len_B = n - n_by_2

  for k in range(n):
    if j >= len_B or (i < n_by_2 and A[i] <= B[j]):
      C.append(A[i])
      i += 1
    else:
      C.append(B[j])
      j += 1

  return C

def main():
  # input = sys.argv[1:]

  input1 = [1, 5, 12, 2, 3, 4, 11, 8, 9, 10, 7, 6]
  input2 = [1, 1, 1]
  input3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

  print('input', input1)
  print('output', merge_sort(input1))
  print('input', input2)
  print('output', merge_sort(input2))
  print('input', input3)
  print('output', merge_sort(input3))

if __name__ == '__main__': main()
