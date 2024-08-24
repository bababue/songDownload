from pytubefix import YouTube
import os


with open("in.txt", "r") as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)


yts = []
for r in lines:
    yt = YouTube(r)
    stream = yt.streams.filter(only_audio=True).first()
    yts.append(stream)



print("Following songs will be downloaded:")

print("-----")
for r in yts:
    print(r.title)
print("-----")
confirm = input("Continue? (y)")

if confirm in ["y", "Y"]:
    for r in yts:
        output_file = r.download(output_path="./out")

        base, ext = os.path.splitext(output_file)
        new_file = base + ".mp3"
        os.rename(output_file, new_file)

    print("All files have been downloaded!")
else:
    quit()
