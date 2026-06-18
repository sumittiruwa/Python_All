  #dictionaries: key -value structure
  
  # create a dictionary 
  
student  = {
    "name" : "Messi",
    "age" : 38,
    "scores": [1,1,1],
    "active": True
}

# Access 
print(student["name"])  # direct access
print(student.get("grade", "N/A"))  # safe access


# add / update

student["grade"]  = "A"
student["age"] = 23



# Nested dict

db = {"u1": {"name":"MESSI","score":100},
      "u2":{"name":"GOAT","score":100}}

print(db["u1"]["score"])