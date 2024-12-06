from flask import Flask, render_template, request
import youtube_fetch as YoutubeFetcher
import util as util

app = Flask(__name__)
youtube_videos_fetcher = YoutubeFetcher

@app.route('/')
def home():
    return 'Testing video catalogue'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('scroll.html')

@app.route('/v1/videos', defaults={'req_channel_id': None}, methods=['GET'])
@app.route('/v1/videos/<req_channel_id>', methods=['GET'])
def list_videos(req_channel_id):
    print("Request Channel id =", req_channel_id)
    print("Request param = ", request.args.get('channel') )
    
    channel_id = req_channel_id
    channel = request.args.get('channel')
    default_channel = 'gurudev'
    fetch_single_channel_id = False
    channel_list = []

    if not channel_id and not channel:
        channel_list.append(default_channel)
    elif channel_id and not channel:
        print("Has channel id but not channel name. Will fetch a single channel.")
        fetch_single_channel_id = True
    else:
        channel_list = util.parse_channel_names(channel);
        if not channel_list:
            channel_list.append(default_channel)

    if fetch_single_channel_id:
        channels_details_total = youtube_videos_fetcher.channel_details_from_channel_id(channel_id)
    else:
        channels_details_total = youtube_videos_fetcher.channel_details_from_names(channel_list)

    print("=== Donwloading video details complete.")
    channels_details = channels_details_total[:10]

    #video_ids, error_urls = util.video_ids ( video_urls )
    print("Top 10 Channel details = ", channels_details[:10])

    # Trim video to Top 100
    for channel in channels_details:
        videos_total = channel.get('videos_details');
        channel['videos_details'] = videos_total[:100]

    print("Rendering channel details = ", channels_details)
    return render_template("video-catalogue.html", channels_details=channels_details)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)