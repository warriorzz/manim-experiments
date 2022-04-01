#!/usr/bin/python3
import os
import glob

scenes = glob.glob("./scenes/*.py")
for i in range(len(scenes)):
    os.system(f"manim -ql --fps 60 --format gif {scenes[i]}")

os.system("mkdir videos; cat ./README-TEMPLATE.md > README.md")
videos = glob.glob("./media/videos/Scene/480p60/*.gif")

for video in videos:
    os.system(f"mv {video} ./videos/{video[29::]}")

videos = glob.glob("./videos/*.gif")
for i in range(len(videos)):
    name = videos[i][9:-4]
    link = f"![{name}](https://github.com/warriorzz/manim-experiments/blob/main/{videos[i][2::]})"
    os.system(f'echo "\n# {name} \n \n{link}" >> README.md')
