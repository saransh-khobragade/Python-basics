import re

shakes = open("beats.txt", "r")
love = open("love.txt", "w")

for line in shakes:
    if re.match("(.*)(L|l)ove(.*)", line):
        print("love>", line)
