"""
avalon generic user I/O framework

this framework tries to make printing messages and getting user input easier
it includes most UNIX terminal background and foreground colors


Name: Avalon Framework
Author: K4T
Date Created: 3/20/17
Last Modified: 8/31/2017

Licensed under the GNU Lesser General Public License Version 3 (GNU LGPL v3),
    available at: https://www.gnu.org/licenses/lgpl-3.0.txt

(C) 2017 K4YT3X
"""
from __future__ import print_function


VERSION = '1.5.3'


class FG():
    """
        Foreground Color
    """
    BL = '\033[30m'  # Black
    R = '\033[31m'  # Red
    G = '\033[32m'  # Green
    Y = '\033[33m'  # Yellow
    B = '\033[34m'  # Blue
    M = '\033[35m'  # Magenta
    C = '\033[36m'  # Cyan
    LGR = '\033[37m'  # Light Grey
    DGR = '\033[90m'  # Dark Grey
    LR = '\033[91m'  # Light Red
    LG = '\033[92m'  # Light Green
    LY = '\033[93m'  # Light Yellow
    LB = '\033[94m'  # Light Blue
    LM = '\033[95m'  # Light Magenta
    LC = '\033[96m'  # Light Cyan
    W = '\033[97m'  # White


class BG():
    """
        Background Color
    """
    BL = '\033[40m'  # Black
    R = '\033[41m'  # Red
    G = '\033[42m'  # Green
    Y = '\033[43m'  # Yellow
    B = '\033[44m'  # Blue
    M = '\033[45m'  # Magenta
    C = '\033[46m'  # Cyan
    LGR = '\033[47m'  # Light Grey
    DGR = '\033[100m'  # Dark Grey
    LR = '\033[101m'  # Light Red
    LG = '\033[102m'  # Light Green
    LY = '\033[103m'  # Light Yellow
    LB = '\033[104m'  # Light Blue
    LM = '\033[105m'  # Light Magenta
    LC = '\033[106m'  # Light Cyan
    WT = '\033[107m'  # White


class FM():
    """
        Formatting
    """
    # SET
    BD = '\033[1m'  # Bold
    DM = '\033[2m'  # Dim
    UN = '\033[4m'  # Underlined
    BL = '\033[5m'  # Blink
    RV = '\033[7m'  # Reverse
    HD = '\033[8m'  # Hidden

    # RESET
    RST = '\033[0m'  # Reset ALL
    RBD = '\033[21m'  # Bold
    RDM = '\033[22m'  # Dim
    RUN = '\033[24m'  # Underlined
    RBL = '\033[25m'  # Blink
    RRV = '\033[27m'  # Reverse
    RHD = '\033[28m'  # Hidden


def info(msg):
    print(FG.G + '[+] INFO: ' + str(msg) + FM.RST)


def timeInfo(msg):
    import datetime
    print(FM.RST + str(datetime.datetime.now()) + FG.G + ' [+] INFO: ' + str(msg) + FM.RST)


def subLevelTimeInfo(msg):
    import datetime
    print(FG.DGR + str(datetime.datetime.now()) + ' [+] INFO: ' + str(msg) + FM.RST)


def warning(msg):
    print(FG.Y + FM.BD + '[!] WARNING: ' + str(msg) + FM.RST)


def error(msg, style='LINE'):
    if style.upper() == 'BANNER':
        import shutil
        width, height = shutil.get_terminal_size((80, 20))
        topBottomBar = FG.R + (((width - len(' ERROR ')) // 2) * '#') + ' ERROR ' + (((width - len(' ERROR ')) // 2) * '#')
        print('\n' + topBottomBar + FM.RST + '\n')
        spaces = ((width - len(str(msg))) // 2) * ' '
        print(FG.R + FM.BD + spaces + str(msg) + spaces + FM.RST)
        print('\n' + topBottomBar + FM.RST + '\n')
    else:
        print(FG.R + FM.BD + '[!] ERROR: ' + str(msg) + FM.RST)


def debug(msg):
    print(FG.R + FM.RDM + '[*] DBG: ' + str(msg) + FM.RST)


def gets(msg):
    res = input(FG.Y + FM.BD + '[?] USER: ' + msg + FM.RST)
    return res


def ask(msg, default=False):
    if default is False:
        while True:
            ans = gets(msg + ' [y/N]: ')
            if ans == '' or ans[0].upper() == 'N':
                return False
            elif ans[0].upper() == 'Y':
                return True
            else:
                error('Invalid Input!')
    elif default is True:
        while True:
            ans = gets(msg + ' [Y/n]: ')
            if ans == '' or ans[0].upper() == 'Y':
                return True
            elif ans[0].upper() == 'N':
                return False
            else:
                error('Invalid Input!')
    else:
        raise TypeError('invalid type for positional argument: \' default\'')


def sequencePrint(msg):
    import time
    for word in str(msg):
        print(word, end="")
        time.sleep(0.05)
    print()
