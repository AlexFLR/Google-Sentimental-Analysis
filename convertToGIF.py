from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("chatbotGif.mp4")

videoClip.write_gif("chatbotFinalGif.gif")