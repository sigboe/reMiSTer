import curses, curses.ascii, os
from subprocess import run

os.environ['TERM'] = 'xterm'
screen = curses.initscr()
screen.keypad(True)
screen.notimeout(True)
os.environ.setdefault('ESCDELAY', '0')
os.environ.setdefault('MBC_SEQUENCE_WAIT', '0')
exitmsg = "Ctrl+D to exit \n"
screen.addstr(exitmsg)
screen.refresh()

keydict = {
        "curses.KEY_UP": ":67",
        "curses.KEY_DOWN": ":6C",
        "curses.KEY_LEFT": ":69",
        "curses.KEY_RIGHT": ":6A",
        "curses.KEY_HOME": ":66",
        "curses.KEY_F1": ":3B",
        "curses.KEY_F2": ":3C",
        "curses.KEY_F3": ":3D",
        "curses.KEY_F4": ":3E",
        "curses.KEY_F5": ":3F",
        "curses.KEY_F6": ":40",
        "curses.KEY_F7": ":41",
        "curses.KEY_F8": ":42",
        "curses.KEY_F9": ":43",
        "curses.KEY_F10": ":44",
        "curses.KEY_F11": ":57",
        "curses.KEY_F12": ":58",
        #KEY_SPACE
        "curses.ascii.SP": ":39",
        #KEY_ENTER
        "curses.ascii.NL": ":1C",
        #"curses.ascii.SOH": "ctrlA",
        #"curses.ascii.EOT": "ctrlD",
        #"curses.ascii.ENQ": "ctrlE",
        #"curses.ascii.CAN": "ctrlX",
        #KEY_ESC
        "curses.ascii.ESC": ":01",
        #KEY_DELETE
        "curses.KEY_DC": ":6F",
        #KEY_INSERT
        "curses.KEY_IC": ":6E",
        #KEY_PAGEDOWN
        "curses.KEY_NPAGE": ":6D",
        #KEY_PAGEUP
        "curses.KEY_PPAGE": ":68",
        "curses.KEY_END": ":6B",
        "curses.KEY_HOME": ":66",
        "curses.ascii.BS": ":0E"
}

while True:
    c = screen.getch()
    screen.clear()
    if c == curses.KEY_UP:
        screen.addstr(exitmsg + "Up")
        run(['mbc', 'raw_seq', ':67'])
    elif c == curses.KEY_DOWN:
        screen.addstr(exitmsg + "Down")
        run(['mbc', 'raw_seq', ':6C'])
    elif c == curses.KEY_LEFT:
        screen.addstr(exitmsg + "Left")
        run(['mbc', 'raw_seq', ':69'])
    elif c == curses.KEY_RIGHT:
        screen.addstr(exitmsg + "Right")
        run(['mbc', 'raw_seq', ':6A'])
    elif c == curses.ascii.ESC:
        screen.addstr(exitmsg + "Esc")
        run(['mbc', 'raw_seq', ':01'])
    elif c == curses.ascii.NL:
        screen.addstr(exitmsg + "Enter")
        run(['mbc', 'raw_seq', ':1C'])
    elif c == curses.KEY_HOME:
        screen.addstr(exitmsg + "Home")
        run(['mbc', 'raw_seq', ':66'])
    elif c == curses.KEY_F1:
        screen.addstr(exitmsg + "F1")
        run(['mbc', 'raw_seq', ':3B'])
    elif c == curses.KEY_F2:
        screen.addstr(exitmsg + "F2")
        run(['mbc', 'raw_seq', ':3C'])
    elif c == curses.KEY_F3:
        screen.addstr(exitmsg + "F3")
        run(['mbc', 'raw_seq', ':3D'])
    elif c == curses.KEY_F4:
        screen.addstr(exitmsg + "F4")
        run(['mbc', 'raw_seq', ':3E'])
    elif c == curses.KEY_F5:
        screen.addstr(exitmsg + "F5")
        run(['mbc', 'raw_seq', ':3F'])
    elif c == curses.KEY_F6:
        screen.addstr(exitmsg + "F6")
        run(['mbc', 'raw_seq', ':40'])
    elif c == curses.KEY_F7:
        screen.addstr(exitmsg + "F7")
        run(['mbc', 'raw_seq', ':41'])
    elif c == curses.KEY_F8:
        screen.addstr(exitmsg + "F8")
        run(['mbc', 'raw_seq', ':42'])
    elif c == curses.KEY_F9:
        screen.addstr(exitmsg + "F9")
        run(['mbc', 'raw_seq', ':43'])
    elif c == curses.KEY_F10:
        screen.addstr(exitmsg + "F10")
        run(['mbc', 'raw_seq', ':44'])
    elif c == curses.KEY_F11:
        screen.addstr(exitmsg + "F11")
        run(['mbc', 'raw_seq', ':57'])
    elif c == curses.KEY_F12:
        screen.addstr(exitmsg + "F12")
        run(['mbc', 'raw_seq', ':58'])
    elif c == curses.ascii.BS or c == 8 or c == 127:
        screen.addstr(exitmsg + "Backspace")
        run(['mbc', 'raw_seq', ':0E'])
    elif c == curses.ascii.SP:
        screen.addstr(exitmsg + "Space")
        run(['mbc', 'raw_seq', ':39'])
    elif c == curses.KEY_DC:
        screen.addstr(exitmsg + "Delete")
        run(['mbc', 'raw_seq', ':6F'])
    elif c == curses.KEY_NPAGE:
        screen.addstr(exitmsg + "Page Down")
        run(['mbc', 'raw_seq', ':6D'])
    elif c == curses.KEY_PPAGE:
        screen.addstr(exitmsg + "Page Up")
        run(['mbc', 'raw_seq', ':68'])
    elif c == curses.KEY_END:
        screen.addstr(exitmsg + "End")
        run(['mbc', 'raw_seq', ':6B'])
    elif c == curses.KEY_HOME:
        screen.addstr(exitmsg + "Home")
        run(['mbc', 'raw_seq', ':66'])
    elif c == curses.ascii.EOT:
        break
    else:
        screen.addstr(exitmsg + chr(c))
        run(['mbc', 'raw_seq', chr(c)])
    screen.refresh()

curses.endwin()
