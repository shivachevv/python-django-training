from typing import List
from .models import Reaction


class BlogPostUtils:
    @classmethod
    def prettify_reactions(self, reactions: List[Reaction]):
        return {
            'thumb_up': len([reaction for reaction in reactions if reaction['name'] == "thumb_up"]),
            'thumb_down': len(
                [reaction for reaction in reactions if reaction['name'] == "thumb_down"])
        }
