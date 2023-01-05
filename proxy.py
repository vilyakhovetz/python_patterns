# Proxy is a structural design pattern, which allows you to substitute special replacement objects instead of real
# objects. These objects intercept calls to the original object, allowing to do something before or after passing the
# call to the original.

# Service interface.
class YouTubeServiceBaseClass:
    def get_video_list(self):
        raise NotImplementedError("Method is not implemented!")

    def get_video_info(self, id):
        raise NotImplementedError("Method is not implemented!")

    def download_video(self, id):
        raise NotImplementedError("Method is not implemented!")


# The specific implementation of Service. The methods of this class ask YouTube for various information. The
# speed of the request depends on the user's Internet channel and the state of YouTube itself. The more calls to the
# service, the less responsive the program will be.
class ThirdPartyYouTubeService(YouTubeServiceBaseClass):
    def get_video_list(self):
        print('Waiting for the service to process the video list request...')
        return 'List of YouTube videos.'

    def get_video_info(self, id):
        print('Waiting for the service to process the video info request...')
        return f'Detailed information about a video №{id}.'

    def download_video(self, id):
        print('Waiting for the service to process the download request...')
        return f'Video №{id} from Youtube.'


# On the other hand, you can cache requests to YouTube and not repeat them for a while until the cache is out of
# date. But you can't add this code directly to Service class, since it is in a third-party library. Therefore,
# we will put the caching logic in a separate wrapper class. It will delegate requests to Service object only if
# it needs to send a request directly.
class YouTubeProxy(YouTubeServiceBaseClass):
    def __init__(self, service):
        self.__service = service
        self.__video_list_cache = None
        self.__video_cache = None
        self.__download_cache = None

    def get_video_list(self):
        if not self.__video_list_cache:
            self.__video_list_cache = self.__service.get_video_list()
        return self.__video_list_cache

    def get_video_info(self, id):
        if not self.__video_cache:
            self.__video_cache = self.__service.get_video_info(id)
        return self.__video_cache

    def download_video(self, id):
        if not self.__download_cache:
            self.__download_cache = self.__service.download_vieo()
        return self.__download_cache

    def reset(self):
        self.__video_list_cache = None
        self.__video_cache = None
        self.__download_cache = None


# The GUI class that uses Service object. Instead of a real Service, we'll slip Proxy object into it. The
# client won't notice anything because Proxy has the same interface as Service.
class YouTubeManager:
    def __init__(self, service):
        self.__service = service

    # Display the video page.
    def render_video_page(self, id):
        return self.__service.get_video_info(id)

# Display a list of video previews.
    def render_list_panel(self):
        return self.__service.get_video_list()

    def reset(self):
        self.__service.reset()

    def react_on_user_input(self, id):
        return self.render_list_panel() + '\n' + self.render_video_page(id)


if __name__ == '__main__':
    youtube_service = ThirdPartyYouTubeService()
    youtube_proxy = YouTubeProxy(youtube_service)
    youtube_manager = YouTubeManager(youtube_proxy)

    print('First request:')
    print(youtube_manager.react_on_user_input(5) + '\n')

    print('Cached request:')
    print(youtube_manager.react_on_user_input(5) + '\n')

    print('Request after reset:')
    youtube_manager.reset()
    print(youtube_manager.react_on_user_input(5) + '\n')
