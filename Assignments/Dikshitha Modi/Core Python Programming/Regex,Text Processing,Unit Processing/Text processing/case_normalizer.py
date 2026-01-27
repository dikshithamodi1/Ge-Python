def case_normalizer(text):
   return " ".join(text.lower().split())#split is used to remove extra whitespace
print(case_normalizer("  HELLO    World!  " ))