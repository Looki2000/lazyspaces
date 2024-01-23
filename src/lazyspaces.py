import os
import sys
import json
import datetime
import subprocess
import shutil

cwd = os.path.dirname(os.path.realpath(__file__))

# create ../lazyspaces
os.makedirs(os.path.join(cwd, "../lazyspaces"), exist_ok=True)

# go through all json files in /lazy_presets and get their display names

lazy_pres_path = os.path.join(cwd, "../lazy_presets")

presets = []

for file in os.listdir(lazy_pres_path):
    if not file.endswith(".json"):
        continue

    # get display name
    with open(os.path.join(lazy_pres_path, file)) as f:
        display_name = json.load(f)["name"]

    presets.append((display_name, file))

print("What do you want to do today?")

while True:
    for i, preset in enumerate(presets):
        print(f"  {i+1}. {preset[0]}")

    try:
        choice = int(input("> "))
    except ValueError:
        print("\nError! Input must be a number\n")
        continue

    if choice < 1 or choice > len(presets):
        print("\nError! Input must be a number in the list\n")
        continue

    break

pres_display_name = presets[choice-1][0]
pres_file_name = presets[choice-1][1]

print(f"Creating \"{pres_display_name}\"...")

# open entire preset json
with open(os.path.join(lazy_pres_path, pres_file_name)) as f:
    preset = json.load(f)

# check if preset has dir_prefix. if not then use display name
prefix = preset["dir_prefix"] if "dir_prefix" in preset else pres_display_name

# create new folder
lazyspace_path = os.path.join(
    cwd, 
    "../lazyspaces",
    prefix + " " + datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
)

try:
    os.makedirs(lazyspace_path, exist_ok=False)
except FileExistsError:
    raise FileExistsError("Lazyspace folder with the same name already exists!")


# check if preset has procedure. if not then exit
if "procedure" not in preset:
    print("Done!")
    exit()

# go through every procedure element and perform it
for proc_elem in preset["procedure"]:
    key, value = zip(*proc_elem.items())

    match key[0]:
        # create new empty file
        case "file":
            with open(os.path.join(lazyspace_path, value[0]), "w") as f:
                pass

        # execute command
        case "command":
            subprocess.Popen(value[0], cwd=lazyspace_path, shell=True)

        # copy file to destination
        case "copy":
            try:
                #print(key)
                if key[1] == "destination":
                    # destination is specified so we use that
                    destination = value[1]
                else:
                    raise IndexError
            
            # destination is not specified so we use the original file name without path
            except IndexError:
                destination = os.path.basename(value[0])


            shutil.copy(
                os.path.join(lazy_pres_path, value[0]),
                os.path.join(lazyspace_path, destination)
            )

print("Done!")