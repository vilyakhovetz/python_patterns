# A facade is a structural design pattern that provides a simple interface to a complex class system, library,
# or framework.

# Classes of a complex third-party video conversion framework. We have no control over this code, so we cannot
# simplify it.
class VideoFile:
    def __init__(self, filename):
        self.file = filename


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:
    def __init__(self):
        self.file = None

    def extract(self, videofile):
        self.file = videofile
        return self.file


class BitrateReader:
    def __init__(self):
        self.file = None
        self.buffer = None
        self.codec = None

    def read(self, filename, codec):
        self.file = filename
        self.codec = codec
        return self.file.file

    def convert(self, buffer, codec):
        self.buffer = buffer
        self.codec = codec
        return self.buffer


class AudioMixer:
    def __init__(self):
        self.result = None

    def fix(self, result):
        self.result = result
        return self.result


# Instead, we create Facade, a simple interface for working with a complex framework. Facade does not have all
# the functionality of the framework, but hides its complexity from clients.
class VideoConverter:
    def __init__(self):
        self.file = None
        self.format = None
        self.source_codec = None
        self.destination_codec = None
        self.buffer = None
        self.result = None

    def convert(self, filename, fileformat):
        self.file = VideoFile(filename)
        self.format = fileformat
        self.source_codec = CodecFactory().extract(self.file)
        if self.format == 'mp4':
            self.destination_codec = MPEG4CompressionCodec()
        else:
            self.destination_codec = OggCompressionCodec()
        self.buffer = BitrateReader().read(self.file, self.source_codec)
        self.result = BitrateReader().convert(self.buffer, self.destination_codec)
        self.result = AudioMixer().fix(self.result)
        return self.result, self.format


# The application does not depend on a complex video conversion framework. By the way, if you suddenly decide to
# change the framework, you will only need to rewrite Facade.
if __name__ == '__main__':
    convertor = VideoConverter()
    mp4 = convertor.convert("youtubevideo.ogg", "mp4")
    print(mp4)
