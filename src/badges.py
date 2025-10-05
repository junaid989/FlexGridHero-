BADGES = {1:'Flex Beginner',2:'Nested Flex Explorer',3:'Grid Apprentice',4:'Grid Architect',5:'Dev Tools Pro'}

class BadgeManager:
    def maybe_award(self, level, attempts):
        if attempts <= 2 and level in BADGES: return BADGES[level]
        return None
