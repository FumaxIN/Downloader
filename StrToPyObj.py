import json

print("lets get started with JSON")

data = '''
{
    "people":
        [
            {
                "name": "Kalpesh",
                "phone": "8744060207",
                "email": "kalpeshdhoundiyal@gmail.com"
            },
            {
                "name": "Tarun",
                "phone": "9958874044",
                "email": "tarundevrani0712@gmail.com"
            },
            {
                "name": "Paras",
                "phone": "9988776655",
                "email": "paras123@gmail.com"
            }
        ]
}
'''
############################# LOADS: String to JSON(PythonOBJ) #################################

print("\nLOADS: String to JSON\n")

parsed = json.loads(data)
print(type(parsed))
print(type(parsed["people"]))  # "people" in list format

# print(parsed)

for x in parsed["people"]:
    print(x["name"])
print("\nLIST OPERATIONS")
print("\n", parsed["people"][1])  # all list functions are supported
print("\n", parsed["people"][1:])

parsed["people"].pop()
print("\n", parsed)

############################### DUMPS: JSON(PythonOBJ) to String ##################################

print("\nDUMPS: JSON to String\n")

# for y in parsed["people"]:
#     del y["phone"]

new_String = json.dumps(parsed, indent=2)
print("\n", type(new_String))
print("\n", new_String)
