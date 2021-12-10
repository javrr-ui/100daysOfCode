class FileReader:
    @staticmethod
    def get_high_score():
        with open("data.txt") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0

    @staticmethod
    def set_high_score(new_high_score):
        with open("data.txt", mode="w") as file:
            file.write(new_high_score)
