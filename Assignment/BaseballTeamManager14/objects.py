from dataclasses import dataclass

@dataclass
class Player():
    first_name = ""
    last_name = ""
    position = ""
    at_bats = 0
    hits = 0

    def fullName(self):
        return self.first_name + " " + self.last_name
    
    def battingAvg(self):
        avg = int(self.hits) / int(self.at_bats)
        return round(avg, 3)

def main():
    pass

if __name__ == "__main__":
    main()