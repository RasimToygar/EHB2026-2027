my_dict = {"Vendor": "Cisco", "Device": "3750", "Ports": "24", "IOS": "13"}
print(type(my_dict))
print(len(my_dict))
del my_dict["Ports"]
print(my_dict)
my_dict["RAM"] = 256
print(my_dict)
print("Vendor" in my_dict)
print("vendor" in my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.pop("Device")
print(my_dict)
my_dict.update({"Speed": "1Gb"})
print(my_dict)
scripting_languages = {1: "python", 2: "ruby", 3: "javascript", 4: "PHP", 5: "perl"}
ide_programs = {"ide_atom": "atom", "ide_vs": "visual_studio", "ide_pv": "py_dev", "ide_pc":
"pyCharm"}
print(type(scripting_languages))
print(type(ide_programs))
print(scripting_languages[3])
print(ide_programs["ide_pv"])
print(scripting_languages.get(1))
print(ide_programs.get("ide_pc"))
scripting_languages[4] = "Bash"
print(scripting_languages)
ide_programs["ide_rm"] = "rubeMine"
print(ide_programs)
del ide_programs["ide_vs"]
print(ide_programs)
scripting_languages.pop(5)
print(scripting_languages)
scripting_values = scripting_languages.values()
print(scripting_values)
scripting_values = list(scripting_values)
print(type(scripting_values))
program_keys = ide_programs.keys()
print(program_keys)
print(type(program_keys))
program_keys=list(program_keys)
print(program_keys)
print(type(program_keys))