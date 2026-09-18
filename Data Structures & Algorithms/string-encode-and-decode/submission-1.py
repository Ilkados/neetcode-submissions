class Solution:
  def encode(self, strs: List[str]) -> str:
    encoded_string = ""
    for st in strs:
      len_st = len(st)
      result = str(len_st) + "#" + st
      encoded_string += result
    return encoded_string

  def decode(self, s: str) -> List[str]:

    result = []
    i = 0
    while i < len(s):
      j = i + 1
      while s[j] != "#":
        j += 1

      lenght = int(s[i:j])

      start = j + 1
      end = start + lenght

      word = s[start:end]
      i = end
      result.append(word)
    return result
