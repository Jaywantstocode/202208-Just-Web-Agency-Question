import json
from collections import OrderedDict

class Processor():

    def __init__(self, dir_name:str) -> None:
        """Initialize the Processor class.
        """
        self.dir_name = dir_name
        self.stars = {}
    
    def read_from_json(self) -> None:
        """Read the json file from given path. Store in self.df.
        """
        with open(self.dir_name) as file:
            self.df = json.load(file)
    
    def to_required_table(self) -> None:
        """Populate self.actors with the information in self.df.
        """
        for movie in self.df:
            for star in movie["stars"].split(", "):
                if star not in self.stars:
                    self.stars[star] = {"Movies": 1, "ratings": [float(movie["rating"])]}
                else:
                    self.stars[star]["ratings"].append(float(movie["rating"]))
                    self.stars[star]["Movies"] += 1
        
        # print(self.stars)

    def print(self) -> str:
        """Print stars in an ascending order by the total number of movies they appeared in,
        yet only stars who appeared in equal or more than 2 movies.
        """
        print(self.stars.items())
        for actor in sorted(self.stars.items(), key=lambda x: x[1]["Movies"]):
            # print(actor)
            if actor[1]["Movies"] < 2:
                continue
            avg_rating = round(sum(actor[1]["ratings"])/actor[1]["Movies"], 2)
            print(f"Star Name: '{actor[0]}' | Movies:  {actor[1]['Movies']} | AVG Rating: {str(avg_rating)}")
    
    def run(self) -> str:
        self.read_from_json()
        self.to_required_table()
        self.print()


if __name__ == "__main__":
    processor = Processor(dir_name="data.json")
    processor.run()