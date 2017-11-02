from itertools import cycle
import curses
import re

#This is presently buggy as hell.

def typer(debug=False):
  stdscr=curses.initscr()
  curses.start_color()
  curses.use_default_colors()
  curses.noecho()
  stdscr.clear()
  c=stdscr.getkey()
  stdscr.refresh
  f=""
  idx=""
  p=[]
  with open("pthread.h","r") as o:
    f=o.read()
  while len(idx)<len(f):
    f=f[len(idx):]
    if debug: print f[:32]
    idx=""
    try:
      p=[f[i:i+n] for i in range(0,len(f),n)]
      for o in cycle(p):
        if debug: print o
        idx+=o
        stdscr.getkey()
        stdscr.addstr(o)
        stdscr.refresh()
    except KeyboardInterrupt:
      curses.nocbreak()
      stdscr.keypad(False)
      curses.echo()
      curses.endwin()
    except:
      print "Crash? idx={0} p={1} f={2}".format(idx,p[:16],f[:16])
      
if __name__=='__main__':
  typer(True)
