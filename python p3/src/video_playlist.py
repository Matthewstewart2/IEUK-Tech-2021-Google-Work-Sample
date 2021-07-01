"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        """Initialise playlist"""
        self.playlist_name = playlist_name
        self.playlist_videos = []
        self.playlist_video_ids = []

    def add_video(self, video):
        """Adds video to playlist"""
        self.playlist_videos.append(video)
        self.playlist_video_ids.append(video._video_id)

    def remove_video(self, video):
        """Removes video from playlist"""
        video_i = self.playlist_video_ids.index(video._video_id)
        self.playlist_videos.pop(video_i)
        self.playlist_video_ids.pop(video_i)

    def clear_videos(self):
        """Removes all videos from playlist"""
        self.playlist_videos.clear()
        self.playlist_video_ids.clear()

    def print_playlist(self):
        """Prints title (video_id) [tags]"""
        if len(self.playlist_videos) > 0:
            for video in self.playlist_videos:
                tags_string = ' '.join(video._tags)
                print("  %s (%s) [%s]" % (video._title, video._video_id, tags_string))
        else:
            print("  No videos here yet")
