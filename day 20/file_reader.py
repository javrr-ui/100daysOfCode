class FileReader:
    def get_high_score(self):
        with open("data.txt") as file:
            high_score = file.read()
            if high_score:
                return high_score
            else:
                return 0

    def set_high_score(self, new_high_score):
        with open("data.txt", mode="w") as file:
            file.write(new_high_score)
