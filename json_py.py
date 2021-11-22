import json

with open("states_data.json") as f:
    parsed = json.load(f)

# state_info = parsed["states"]

for data in parsed["states"]:
    print(data["name"], "\t\t", data["abbreviation"])

# Creating new JSON file with Abbreviations removed

for temp in parsed["states"]:
    del temp["abbreviation"]

with open("edited.json", "w") as new_f:
    json.dump(parsed, new_f, indent=2)