import time
from src.ui import UI
ui = UI()
def _box(text,w=9):
    t=text[:w-2]; pad=w-2-len(t)
    return '['+t+' '*pad+']'
class Visualizer:
    def show_preview(self,level):
        if level==1: self._flex_preview()
        elif level==2: self._nested_flex_preview()
        elif level==3: self._grid_preview_basic()
        elif level==4: self._grid_areas_preview()
        else: ui.print_info('Dev tip: open browser DevTools (F12) to inspect layout.')
    def _flex_preview(self):
        ui.print_info('Flexbox preview (justify-content: center)'); row='   '.join([_box('item1'),_box('item2'),_box('item3')]); print('\n'+row+'\n')
    def _nested_flex_preview(self):
        ui.print_info('Nested Flexbox: outer row, inner column'); left='\n'.join([_box('a'),_box('b')]); right='\n'.join([_box('1'),_box('2'),_box('3')]); print(left+'   '+right+'\n')
    def _grid_preview_basic(self):
        ui.print_info('Grid preview: 3 columns'); row=' '.join([_box('A'),_box('B'),_box('C')]); print('\n'+row+'\n')
    def _grid_areas_preview(self):
        ui.print_info('Grid areas preview (header sidebar main footer)'); header=_box('header',20); print('\n'+header+'\n'); middle=_box('sidebar',12)+' '+_box('main',20); print(middle+'\n'); footer=_box('footer',20); print(footer+'\n')
    def build(self,level):
        if level<=0: return
        ui.print_info('\nBuilding your page layout...'); time.sleep(0.5)
        if level>=1: self._flex_preview(); time.sleep(0.4)
        if level>=2: self._nested_flex_preview(); time.sleep(0.4)
        if level>=3: self._grid_preview_basic(); time.sleep(0.4)
        if level>=4: self._grid_areas_preview(); time.sleep(0.4)
