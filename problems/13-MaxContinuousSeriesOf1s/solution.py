def find_flip_index(array, m):
  curr_length = max_length = 0
  flip_idx = sol = []
  first_zero_idx = next_zero_idx = None
  if m <= 0:
    return None
  for idx, item in enumerate(array):
    if item == 0 and m>0:
      m -= 1
      curr_length += 1
      flip_idx.append(idx)
      if first_zero_idx:
        next_zero_idx = idx
      else:
        first_zero_idx = idx

    elif item == 0 and m<=0:
      curr_length = idx - (first_zero_idx)
      flip_idx.append(idx)
      flip_idx = flip_idx[1:]
      if next_zero_idx:
        first_zero_idx = next_zero_idx
      if curr_length > max_length:
        max_length = curr_length
        sol = flip_idx[:]
    else:
      curr_length += 1
  return flip_idx

print(find_flip_index([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 2))