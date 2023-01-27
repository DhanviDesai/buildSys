import os
from pathlib import Path
import json

# I would have to change dir here to the current workspace dir. Get the path of this file and get the path from that
current_workspace = os.getcwd()
os.chdir(current_workspace)

# make src\main a configurable input via build file
src_files = ' '.join([str(u) for u in Path("src\\main").rglob("*.java")])

# build file related stuff
build_directory = os.path.join(current_workspace, 'build')
if not os.path.exists(build_directory):
        os.makedirs(build_directory)

# compilation stuff
os.system("javac -d {0} {1}".format(build_directory,src_files))

# here process the dd file to get the main class and run it using java
with open("build.dd", "r") as f:
        build_logic = json.load(f)
        os.chdir(build_directory)
        os.system("java {0}".format(build_logic["main_class"].replace("//",".")))


