from song import Song

class SongParser:

    def __init__(self, song):
        self.TITLE_SPLIT = 'title: '
        self.song = song

    def parse(self, file):
        with open(file) as f:
            for line in f:
                self.parseLine(line)

    def parseLine(self, line):
        if (line.find(self.TITLE_SPLIT) != -1):
            self.song.title = line.split(self.TITLE_SPLIT)[1]
        else:
            self.song.keys.append(line.split())

