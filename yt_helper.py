import pafy
import vlc

def player_build(url):
    # url = "https://www.youtube.com/watch?v=wXxre8J0GcA"
    video = pafy.new(url)
    best = video.getbestaudio()
    playurl = best.url

    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    return player
    # player.play()

def ytdler(url):
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download()
