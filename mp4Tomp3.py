from moviepy.editor import VideoFileClip
import glob

for file in glob.glob("*.mp4"):
	print(file)
	videoclip = VideoFileClip(file)
	audioclip = Videoclip.audio
	audioclip.write_audiofile(file[:-3]+'mp3')


