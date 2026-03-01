from typing import Dict, List

class ModelState:
    def __init__(self):
        self.user_stories: List[str] = []
        self.actors: List[str] = []
        self.entities: List[str] = []
        self.relationships: List[Dict] = []

    def add_story(self, story: str):
        self.user_stories.append(story)

    def update_from_extraction(self, data: Dict):
        self.actors = list(set(self.actors + data.get("actors", [])))
        self.entities = list(set(self.entities + data.get("entities", [])))
        self.relationships.extend(data.get("relationships", []))

model_state = ModelState()