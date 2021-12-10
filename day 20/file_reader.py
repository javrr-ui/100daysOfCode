class FileReader:
    def get_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
            if high_score:
                return high_score
            else:
                return 0
