LESSONS = {
 1: {'title':'Flexbox Basics', 'lesson':(
    "Flexbox is a one-dimensional layout system for arranging items in a row or a column.\n"
    "Key properties:\n  display: flex  -> enable flexbox\n  justify-content -> main axis alignment\n  align-items -> cross-axis alignment\n"
    "Example:\n  .container { display: flex; justify-content: center; align-items: center; }\n"
 ), 'answer':'display: flex', 'hints':['Property enabling layout mode.','It uses the word display and value flex.']},
 2: {'title':'Nested Flexbox', 'lesson':(
    "Flex containers can be inside other flex containers.\n"
    "Use flex-direction to switch row/column.\n"
    "Example:\n  .inner { display:flex; flex-direction:column }\n"
 ), 'answer':'flex-direction', 'hints':['Sets row or column','Values: row or column']},
 3: {'title':'CSS Grid Basics', 'lesson':(
    "Grid is two-dimensional. Use grid-template-columns to make columns.\n"
    "Example:\n  .grid { display:grid; grid-template-columns: 1fr 1fr 1fr; gap:8px }\n"
 ), 'answer':'grid-template-columns', 'hints':['Property name contains "columns"','Defines columns']},
 4: {'title':'Advanced Grid', 'lesson':(
    "Grid areas let you name regions using grid-template-areas then assign grid-area to children.\n"
    "Example:\n  grid-template-areas: 'header header' 'sidebar main' 'footer footer'\n"
 ), 'answer':'grid-template-areas', 'hints':['Defines named regions','Uses string rows to map areas']},
 5: {'title':'Dev Tools & Workflow', 'lesson':(
    "Dev tips:\n - Use browser DevTools (F12) to inspect layout.\n - Start mobile-first.\n - Combine grid for layout and flex for components.\n"
 ), 'answer':'devtools', 'hints':['Opened with F12','Browser developer tools']}
}

class LessonManager:
    def __init__(self): self.lessons = LESSONS
    def get(self, level): return self.lessons.get(level)
    def title(self, level): L=self.get(level); return L['title'] if L else 'Unknown'
    def check_answer(self, level, ans):
        L=self.get(level)
        if not L: return False
        a=(ans or '').strip().lower(); target=L['answer'].strip().lower()
        aliases=[target]
        if target=='display: flex': aliases += ['flex','display:flex','display flex']
        if target=='devtools': aliases += ['developer tools','dev tools','devtool','devtools']
        return any(a==x for x in aliases)
    def hint(self, level):
        L=self.get(level)
        if not L: return ''
        return L.get('hints',[None])[0]
    def max_level(self): return max(self.lessons.keys())
