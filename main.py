#!/usr/bin/env python3
import os, sys, json, time
from src.ui import UI
from src.lessons import LessonManager
from src.visualizer import Visualizer
from src.badges import BadgeManager
from src.editor import css_challenge

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR=os.path.join(ROOT,'data'); PROGRESS_FILE=os.path.join(DATA_DIR,'progress.json')

def ensure_data():
    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE,'w') as f: json.dump({"level":1,"badges":[]},f)

def load_progress():
    with open(PROGRESS_FILE,'r') as f: return json.load(f)
def save_progress(p): 
    with open(PROGRESS_FILE,'w') as f: json.dump(p,f)

def cyber_intro(ui):
    # Fast Cyber Scan + Neon Typewriter hybrid
    scan = ['[====        ]','[========    ]','[============]']
    for s in scan:
        ui.clear(); ui.header('FlexGrid Hero+ — Cyber Neon'); print(); print('Initializing: '+s); time.sleep(0.18)
    # typewriter reveal
    ui.clear(); ui.header('FlexGrid Hero+ — Cyber Neon'); ui.type_writer('Welcome to FlexGrid Hero+ — Learn Flexbox, Nested Flexbox & Grid', speed=0.01)
    ui.type_writer('Created by @muhjunaid_123 & @sys_adminshadow', speed=0.01)
    ui.pause(0.8)

def main():
    ensure_data()
    ui=UI(); lm=LessonManager(); vz=Visualizer(); bm=BadgeManager()
    prog=load_progress(); level=prog.get('level',1); badges=set(prog.get('badges',[]))
    ui.clear(); cyber_intro(ui)
    while level <= lm.max_level():
        ui.clear(); ui.header('FlexGrid Hero+ — Cyber Neon')
        ui.section_title(f"Level {level}: {lm.title(level)}")
        lesson=lm.get(level)
        ui.type_writer(lesson['lesson'])
        vz.show_preview(level)
        attempts=0
        while True:
            attempts+=1
            ans=ui.prompt('Your answer (type hint/skip)')
            if ans.strip().lower()=='hint':
                ui.print_info(lm.hint(level)); continue
            if ans.strip().lower()=='skip':
                ui.print_warn('Skipping level (no badge)'); level+=1; break
            if lm.check_answer(level, ans):
                ui.print_good('Correct!')
                badge=bm.maybe_award(level, attempts)
                if badge and badge not in badges:
                    ui.print_badge(badge); badges.add(badge)
                level+=1; prog['level']=level; prog['badges']=list(badges); save_progress(prog); break
            else:
                ui.print_bad('Not correct. Try again.')
                if attempts>=3: ui.print_info('Tip: type hint for a hint or skip to continue.')
        vz.build(level-1); ui.pause(0.6)
        # after level 3 offer mini editor
        if level>3 and level-1==3:
            ui.print_info('\nSpecial Challenge unlocked: Mini Editor (type a CSS rule)') 
            ok=css_challenge(ui)
            if ok:
                b='Editor Challenger'; if b not in badges: badges.add(b); ui.print_badge(b); prog['badges']=list(badges); save_progress(prog)
    ui.section_title('🎉 Completion'); ui.type_writer('You finished FlexGrid Hero+! Well done.')
    if badges: ui.print_info('Badges: '+', '.join(sorted(badges)))
    ui.print_info('Progress saved to data/progress.json'); ui.prompt('Press Enter to exit')

if __name__=='__main__':
    try: main()
    except KeyboardInterrupt:
        print('\nBye — keep building!'); sys.exit(0)
