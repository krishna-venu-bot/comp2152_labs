class Heart:
    def __init__(self, bpm=72):
        self.bpm = bpm  # Default BPM value

    def beat(self):
        print("Lub-dub")

    def __str__(self):
        return f"Heart Rate: {self.bpm} BPM"
