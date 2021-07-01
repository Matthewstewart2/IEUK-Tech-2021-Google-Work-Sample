"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_id_list = []
        for video in self._video_library.get_all_videos():
            self.video_id_list.append(video._video_id)
        self.playing = False
        self.current_video = None
        self.paused = False

        self.playlists = []
        self.playlist_names = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        orderless_output = []
        for video in self._video_library.get_all_videos():
            tags_string = ' '.join(video._tags)
            orderless_output.append("%s (%s) [%s]" % (video._title, video._video_id, tags_string))
        alphabet_output = sorted(orderless_output)
        for item in alphabet_output:
            print("  " + item)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if video_id in self.video_id_list and not self.playing:
            self.current_video = self._video_library.get_video(video_id)
            self.playing = True
            self.paused = False
            print("Playing video: " + self.current_video._title)
        elif video_id in self.video_id_list and self.playing:
            print("Stopping video: " + self.current_video._title)
            self.current_video = self._video_library.get_video(video_id)
            self.playing = True
            self.paused = False
            print("Playing video: " + self.current_video._title)
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.playing:
            print("Stopping video: " + self.current_video._title)
            self.playing = False
            self.paused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        random_video_id = self.video_id_list[random.randint(0, len(self.video_id_list) - 1)]
        self.play_video(random_video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.playing and not self.paused:
            self.paused = True
            print("Pausing video: " + self.current_video._title)
        elif self.playing and self.paused:
            print("Video already paused: " + self.current_video._title)
            self.paused = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.paused and self.playing:
            print("Continuing video: " + self.current_video._title)
            self.paused = False
        elif not self.paused and self.playing:
            print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing:
            paused_status = ""
            if self.paused:
                paused_status += " - PAUSED"
            tags_string = ' '.join(self.current_video._tags)
            print("Currently playing: %s (%s) [%s]%s" % (self.current_video._title, self.current_video._video_id, tags_string, paused_status))
        else:
            print("No video is currently playing")

    def create_playlist(self, new_playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if new_playlist_name.upper() not in self.playlist_names:
            new_playlist = Playlist(new_playlist_name)
            self.playlists.append(new_playlist)
            self.playlist_names.append(new_playlist.playlist_name.upper())
            print("Successfully created new playlist: " + new_playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.upper() in self.playlist_names and video_id in self.video_id_list:
            playlist_i = self.playlist_names.index(playlist_name.upper())
            if video_id not in self.playlists[playlist_i].playlist_video_ids:
                new_video = self._video_library.get_video(video_id)
                self.playlists[playlist_i].add_video(new_video)
                print("Added video to %s: %s" % (playlist_name, new_video.title))
            else:
                print("Cannot add video to %s: Video already added" % (playlist_name))
        elif playlist_name.upper() not in self.playlist_names:
            print("Cannot add video to %s: Playlist does not exist" % (playlist_name))
        else:
            print("Cannot add video to %s: Video does not exist" % (playlist_name))

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.playlists) > 0:
            orderless_output = []
            for i in range(len(self.playlists)):
                orderless_output.append(self.playlists[i].playlist_name)
            alphabet_output = sorted(orderless_output)
            print("Showing all playlists:")
            for line in alphabet_output:
                print("  " + line)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist_names:
            playlist_i = self.playlist_names.index(playlist_name.upper())
            print("Showing playlist: " + playlist_name)
            self.playlists[playlist_i].print_playlist()
        else:
            print("Cannot show playlist %s: Playlist does not exist" % (playlist_name))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.upper() in self.playlist_names and video_id in self.video_id_list:
            playlist_i = self.playlist_names.index(playlist_name.upper())
            if video_id in self.playlists[playlist_i].playlist_video_ids:
                new_video = self._video_library.get_video(video_id)
                self.playlists[playlist_i].remove_video(new_video)
                print("Removed video from %s: %s" % (playlist_name, new_video.title))
            else:
                print("Cannot remove video from %s: Video is not in playlist" % (playlist_name))
        elif playlist_name.upper() not in self.playlist_names:
            print("Cannot remove video from %s: Playlist does not exist" % (playlist_name))
        else:
            print("Cannot remove video from %s: Video does not exist" % (playlist_name))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist_names:
            playlist_i = self.playlist_names.index(playlist_name.upper())
            self.playlists[playlist_i].clear_videos()
            print("Successfully removed all videos from " + playlist_name)
        else:
            print("Cannot clear playlist %s: Playlist does not exist" % (playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() in self.playlist_names:
            playlist_i = self.playlist_names.index(playlist_name.upper())
            self.playlists.pop(playlist_i)
            self.playlist_names.pop(playlist_i)
            print("Deleted playlist: " + playlist_name)
        else:
            print("Cannot delete playlist %s: Playlist does not exist" % (playlist_name))

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        orderless_output = []
        for video in self._video_library.get_all_videos():
            if search_term.upper() in video._title.upper():
                tags_string = ' '.join(video._tags)
                orderless_output.append("%s (%s) [%s]" % (video._title, video._video_id, tags_string))
            alphabet_output = sorted(orderless_output)
        if len(alphabet_output) > 0:
            print("Here are the results for " + search_term + ":")
            for i in range(len(alphabet_output)):
                print(str(i + 1) + ") " + alphabet_output[i])
            #video_num = input("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.\n")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            video_num = input("")
            try:
                video_num = int(video_num)
            except:
                pass
            if isinstance(video_num, int) and video_num > 0 and video_num <= len(alphabet_output):
                start = alphabet_output[video_num - 1].find("(")
                end = alphabet_output[video_num - 1].find(")")
                chosen_video_id = alphabet_output[video_num - 1][start + 1:end]
                self.play_video(chosen_video_id)
        else:
            print("No search results for " + search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        orderless_output = []
        for video in self._video_library.get_all_videos():
            upper_tags = []
            for tag in video._tags:
                upper_tags.append(tag.upper())
            if video_tag.upper() in upper_tags:
                tags_string = ' '.join(video._tags)
                orderless_output.append("%s (%s) [%s]" % (video._title, video._video_id, tags_string))
            alphabet_output = sorted(orderless_output)
        if len(alphabet_output) > 0:
            print("Here are the results for " + video_tag + ":")
            for i in range(len(alphabet_output)):
                print(str(i + 1) + ") " + alphabet_output[i])
            #video_num = input("Would you like to play any of the above? If yes, specify the number of the video.\nIf your answer is not a valid number, we will assume it's a no.\n")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            video_num = input("")
            try:
                video_num = int(video_num)
            except:
                pass
            if isinstance(video_num, int) and video_num > 0 and video_num <= len(alphabet_output):
                start = alphabet_output[video_num - 1].find("(")
                end = alphabet_output[video_num - 1].find(")")
                chosen_video_id = alphabet_output[video_num - 1][start + 1:end]
                self.play_video(chosen_video_id)
        else:
            print("No search results for " + video_tag)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
