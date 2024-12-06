import os 
import googleapiclient.discovery
import util as util

API_KEY = "AIzaSyBENe49iIPLLAKqGeLYOy_ut9WMSPIwH2U" 
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)
max_playlist_result = util.max_playlist_result()
max_video_count = util.max_video_count() 

def channel_details_from_channel_id(channel_id):
    if not channel_id:
        return None
    
    total_channel_details = []
    channel_details = channel_video_urls(channel_id)
    total_channel_details.append(channel_details)
    return total_channel_details

def channel_details_from_names(channel_names):
    if not channel_names:
        channel_names = util.default_channel_names()
    
    total_channel_details = []
    for channel_name in channel_names:
        channel_id = util.channel_id_for_name(channel_name)
        channel_details = channel_video_urls(channel_id)
        total_channel_details.append(channel_details)
    return total_channel_details

def channel_video_urls(channel_id):  
    channels_response = youtube.channels().list( 
        part="snippet,contentDetails", 
        id=channel_id 
    ).execute() 

    channel_title = channels_response["items"][0]["snippet"]["title"]
    channel_description = channels_response["items"][0]["snippet"]["description"]
    channel_custom_url = channels_response["items"][0]["snippet"]["customUrl"]
    print("Channel title = ", channel_title, ". Channel response = ", channels_response)

    uploads_playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"] 
 
    #video_urls = []
    videos_details = []
    channel_details = {}
    next_page_token = None 
    video_count = 0
 
    while True: 
        if video_count >= max_video_count:
            break
        playlist_items_response = youtube.playlistItems().list( 
            part="snippet,contentDetails", 
            playlistId=uploads_playlist_id, 
            maxResults=int(max_playlist_result), 
            pageToken=next_page_token 
        ).execute() 

        #print("Playlist response = ", playlist_items_response)
         
        for item in playlist_items_response["items"]: 
            video_id = item["snippet"]["resourceId"]["videoId"] 
            video_url = f"https://www.youtube.com/watch?v={video_id}" 
            #video_urls.append(video_url) 
            publishedAt = item["snippet"]["publishedAt"]
            view_count, like_count, dislike_count = fetch_video_stats(video_id)
            
            detail = detail_dict(video_id, video_url, publishedAt, view_count, like_count, dislike_count)
            videos_details.append(detail)
            video_count = video_count + 1
            print("Adding. Video count = ", video_count)
            #break

        #break
        next_page_token = playlist_items_response.get("nextPageToken") 
        if not next_page_token: 
            break 
 
    channel_details['title'] = channel_title
    channel_details['description'] = channel_description
    channel_details['custom_url'] = channel_custom_url
    channel_details['videos_details'] = videos_details
    return channel_details 
 
def fetch_video_stats(video_id):
    video_data = youtube.videos().list(part="statistics", id=video_id).execute()
    #print("====\n\n===Video data = ", video_data)
    view_count = video_data['items'][0]['statistics'].get('viewCount')
    like_count = video_data['items'][0]['statistics'].get('likeCount')
    dislike_count = video_data['items'][0]['statistics'].get('dislikeCount')
    
    return view_count, like_count, dislike_count

def detail_dict(video_id, video_url, publishedAt, view_count, like_count, dislike_count):
    detail = {}
    detail['video_id'] = video_id
    detail['video_url'] = video_url, 
    detail['published_date'] = publishedAt
    detail['views'] = view_count
    detail['likes'] = like_count
    detail['dislikes'] = dislike_count
    #print("\n\n===Detail = ", detail)
    return detail
            
if __name__ == "__main__": 
    CHANNEL_ID = "UCs6nmQViDpUw0nuIx9c_WvA"
    channel_name = "ProgrammingKnowledge"

    saana_channel_id = "UCQDHdtIUvUd-4FF8cwtPhDg"
    saana_channel_name = "@dancewithsaana"

    Gurudev_channel_id = "UC4qz5w2M-Xmju7WC9ynqRtw"
     
    video_details = channel_video_urls(Gurudev_channel_id)
    print("Total videos= ", len(video_details)) 
    for detail in video_details[:10]: 
        print( detail['video_url'] ) 