from moviepy.editor import VideoFileClip

name = input("Input location (Just write the name if it's in this folder): ")

try:
    clip = VideoFileClip(name)

    output = input("Name of output file: ")

    if ".gif" not in output:
        output += ".gif"


    clip.write_gif(output)

    print(f"Made {output} successfully.")
    
except Exception as e:
    print(e)
