fruits = {"Apple" : "Red", "Banana" : "Yellow"}

print(fruits)
print(fruits["Apple"])

facts = dict()

facts["code"] = "fun"

print(facts["code"])

facts["Bill"] = "Gates"

facts["founded"] = 1776

facts["founded"]

bill = dict({"Bill Gates " : "charitable"})

"Bill Gates" in bill 

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }


n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")