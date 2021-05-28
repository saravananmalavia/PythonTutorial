import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

data1 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar1 = pd.DataFrame(data1)

print(myvar1)