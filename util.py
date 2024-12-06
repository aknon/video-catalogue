import os
from dotenv import load_dotenv

load_dotenv()

channel_vs_names = {}

channel_vs_names['srisrischoolofyoga'] = os.getenv('channel_id_srisrischoolofyoga')
channel_vs_names['meditationsbygurudev'] = os.getenv('channel_id_MeditationsByGurudev')
channel_vs_names['artofliving'] = os.getenv('channel_id_artofliving')
channel_vs_names['gurudev'] = os.getenv('channel_id_Gurudev')
channel_vs_names['artoflivingproductions'] = os.getenv('channel_id_ArtOfLivingProductions')

channel_vs_names['dancewithsaana'] = os.getenv('channel_id_dancewithsaana')
channel_vs_names['programmingknowledge'] = os.getenv('channel_id_ProgrammingKnowledge')

channel_vs_names['welovesrisri'] = os.getenv('channel_id_welovesrisri')
channel_vs_names['pranithar'] = os.getenv('channel_id_aka_GurudevWorld_pranithar')

default_channel_name = 'gurudev'
default_channel_id = channel_vs_names[default_channel_name]

def default_channel_names():
	return ["gurudev", "dancewithsaana"]

def max_video_count():
	return int(os.getenv('max_video_download_count'))

def max_playlist_result():
	return os.getenv('max_playlist_result')

def channel_id_for_name(channel_name):
	try:
		if not channel_name:
			return default_channel_id
		return channel_vs_names[channel_name]

	except ValueError as ve:
		print("Value error finding channel name for : ", channel_name)
		return None


def parse_channel_names(channel_names_str):
	if not channel_names_str or (channel_names_str.strip() == ""):
		return None
	channel_list =  [ e.strip() for e in channel_names_str.split(",") if e.strip() != "" ]
	#channel_list = [ int(e) if digit(e) else e for e in str.split() ]
	return channel_list

def get_video_id(video_url):
	if video_url is None:
		return None
	first = video_url.find("v=")
	print(first)
	if first == -1:
		return None
	last = video_url.find("&")
	print(last)
	video_id = None

	if last == -1:
		video_id = video_url[first+2:]
	else:
		video_id = video_url[first+2: last]
	print(video_id)
	return video_id

def video_ids(video_urls):
	if not video_urls:
		return None

	video_ids = []
	error_urls = []
	for url in video_urls:
		id = get_video_id(url)
		if id is not None:
			video_ids.append(id)
		else:
			error_urls.append(url)

	return (video_ids, error_urls)

if __name__ == '__main__':
	str1 = "gurudev, abc"
	list1 = parse_channel_names(str1)
	print(list1)

	str1 = "gurudev"
	list1 = parse_channel_names(str1)
	print(list1)

	str1 = "gurudev, abc,   "
	list1 = parse_channel_names(str1)
	print(list1)

	str1 = ""
	list1 = parse_channel_names(str1)
	print(list1)

	v = "https://www.youtube.com/watch?v=bZ6NL59FMoc"
	v_id = get_video_id( v )
	video_urls = ['https://www.youtube.com/watch?v=i41VU2d1Emk', 'https://www.youtube.com/watch?v=fF-07yFTq5o', 'https://www.youtube.com/watch?v=c_VFpEec5C4', 'https://www.youtube.com/watch?v=gFVK-FH-z90', 'https://www.youtube.com/watch?v=-lT6apvG46Y', 'https://www.youtube.com/watch?v=vulFdi-U5hU', 'https://www.youtube.com/watch?v=wvAqie4soNc', 'https://www.youtube.com/watch?v=SNgaUYu5o1o', 'https://www.youtube.com/watch?v=X4mtsWfhNzw', 'https://www.youtube.com/watch?v=a3HJnbYhXUc']
	print(len(video_urls))
	(video_ids, error_urls) = video_ids( video_urls)
	if not error_urls:
		print("No error")
		print("Assert lens ", len(video_urls), len(video_ids))
	print("Video ids = ", video_ids)

	c_id = channel_id_for_name('gurudev')
	print(c_id)

