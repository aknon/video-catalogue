from pytube import Channel 
from pytube import YouTube
from pytube import Playlist

def video_info(video_url):
    yt = YouTube(video_url, use_oauth=False)
    title = yt.title
    print("Video url = ", video_url, ". Title = ", title)
    return title

def channel_video_urls(channel_url):
    channel = Channel(channel_url)
    video_urls = channel.video_urls
    # Get the channel's videos 
    #videos = yt.get_videos() 
    print(video_urls)
    return video_urls

def print_channel_video_urls(channel_url):
    video_urls = channel_video_urls(channel_url)
    print("Channel url = ", channel_url, ". Video urls =", video_urls)
    for url in video_urls:
        print("Video url =", url)


def playlist(playlist_url):
    play = Playlist(playlist_url)
    urls = play.video_urls;
    videos = play.videos
    print("Playlist url =", urls[0], ". Videos = ", videos[0])
    return [urls, videos]

def playlist_videos(playlist_url):
    urls, videos = playlist(playlist_url)
    for video in videos:
        print("Downloading video =", video)
        video.streams.first().download()
        break


def main(channel_url, video_url, playlist_url):
    print_channel_video_urls(channel_url)
    #video_info(video_url)
    playlist_videos(playlist_url)


if __name__ == "__main__":
    
    channel_url1 = "https://www.youtube.com/channel/UCq-Fj5jknLsUf-MWSy4_brA"
    channel_url = "https://www.youtube.com/c/ProgrammingKnowledge"
    sample_video1 = "http://youtube.com/watch?v=2lAe1cqCOXo"
    sample_video = "https://www.youtube.com/watch?v=y41nwoG8em8"
    playlist_url = "https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n";

    main(channel_url, sample_video, playlist_url)
    