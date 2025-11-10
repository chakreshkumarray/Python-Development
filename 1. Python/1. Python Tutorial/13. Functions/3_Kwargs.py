
# **Kwargs

def build_profile(**kwargs):
  print("Building profile..")
  for i, j in kwargs.items():
    print(f"{i}: {j}")

build_profile(name = "CK", age = 23, profession = "SD",hobbies = ["Cricket","Movies","Coding"] , city = "Sultanpur")

# Combined 38:35
def mixed_example():
  print()