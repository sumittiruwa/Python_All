from moviepy.editor import VideoFileClip

clip = VideoFileClip("test.mp4")

clip.save_frame("ss.jpg", t=1)