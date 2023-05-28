import os
from googleapiclient.discovery import build


class Video:
    """Инициализация класса Video по ID видео на youtobe, подтягиваются данные по:
    названию видео - title
    ссылке на видео - url_video
    о количестве просмотров - view_count
    о количестве лайков - like_count
    """
    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.video_response = self.youtube.videos().list(id=video_id, part='snippet,statistics,contentDetails,'
                                                                           'topicDetails').execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url_video = f"https://youtu.be/{self.video_id}"
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    """Инициализация класса PLVideo по ID видео на youtobe и ID канала, подтягиваются данные по:
     названию видео - title
     ссылке на видео - url_video
     о количестве просмотров - view_count
     о количестве лайков - like_count
     """
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f'{self.title}'
