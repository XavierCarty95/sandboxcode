mydic = { "Height" : "5'11", 
          "Weight" : "220" , 
          "Color" : "red" , 
          "Head-First" :"Java" }

answer = input("Type Height , Weight, or Color")
if answer in mydic:
    result = mydic[answer]
    print(result)

mydict = { "musicians" : 
            ["Kayne" , "John P kEE " , "iDDRIS"],
            
            "song" : ["That which dont " , "MAKES ME"],
            
            "diction" : {
                "Apple":"red" , "keys" : "blue",
            }
}


print(mydict["diction"]["Apple"])