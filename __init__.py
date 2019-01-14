#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avalon generic user I/O framework

Description: this framework tries to make printing messages and
getting user input easier it includes most UNIX terminal background
and foreground colors.

Name: Avalon Framework
Author: K4T
Date Created: March 20, 2017
Last Modified: October 19, 2018

Licensed under the GNU Lesser General Public License Version 3 (GNU LGPL v3),
    available at: https://www.gnu.org/licenses/lgpl-3.0.txt

(C) 2017 - 2019 K4YT3X
"""
from datetime import datetime
import sys

if sys.platform == 'win32':
    from colorama import init
    init()
else:
    import syslog

VERSION = '1.7.0'
PLATFORM = sys.platform

class Avalon:

    def __init__(self,logLevel='warning'):
        logLevel = logLevel.upper()
        if logLevel == 'DEBUG':
            self.loglevel = 0
        elif logLevel == 'INFO':
            self.loglevel = 1
        elif logLevel == 'WARNING':
            self.loglevel = 2
        elif logLevel == 'ERROR':
            self.loglevel = 3
        elif logLevel == 'CRITCAL':
            self.loglevel = 4
        elif logLevel == 'NONE':
            self.loglevel = 5
        else:
            raise TypeError("invalid type for positional argument: 'default'")

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

    def info(self, msg,highlight=False):
        if highlight == True:
            style = Avalon.FG.LG + Avalon.FM.BD
        elif highlight == False:
            style = Avalon.FG.G + Avalon.FM.BD
        else:
            raise TypeError('invalid type for positional argument: \' default\'')
        print('{}[INFO]{}{}'.format(style, str(msg), Avalon.FM.RST))
        if self.loglevel <= 1 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_INFO, msg)

    def time_info(self,msg,highlight=False):
        if highlight == True:
            style = Avalon.FG.LG + Avalon.FM.BD
        elif highlight == False:
            style = Avalon.FG.G + Avalon.FM.BD
        else:
            raise TypeError('invalid type for positional argument: \' default\'')
        print('{}[{}]{}[INFO]{}{}'.format(Avalon.FM.RST, str(datetime.now().time()), style, str(msg), Avalon.FM.RST))
        if self.loglevel <= 1 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_INFO, msg)

    def debug_info(self,msg):
        print('{}[{}][INFO]{}{}'.format(Avalon.FG.DGR, str(datetime.now().time()), str(msg), Avalon.FM.RST), file=sys.stderr)
        if self.loglevel <= 0 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_DEBUG, msg)

    def warning(self,msg):
        print('{}{}[WARNING]{}{}'.format(Avalon.FG.Y, Avalon.FM.BD, str(msg), Avalon.FM.RST), file=sys.stderr)
        if self.loglevel <= 2 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_WARNING, msg)

    def error(self,msg):
        print('{}{}[ERROR]{}{}'.format(Avalon.FG.R, Avalon.FM.BD, str(msg), Avalon.FM.RST), file=sys.stderr)
        if self.loglevel <= 3 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_WARNING, msg)

    def critical(self,msg):
        print('{}{}{}[CRITICAL]{}{}'.format(Avalon.BG.LR, Avalon.FM.BD, Avalon.FG.W,str(msg), Avalon.FM.RST),file=sys.stderr)
        if self.loglevel <= 4 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_WARNING, msg)

    def banner(self,msg):
        from os import get_terminal_size
        width = get_terminal_size().columns
        print('{}{}{}{}'.format(Avalon.FG.LR,Avalon.FM.BD,'#'*width,Avalon.FM.RST))
        print(('\n{}{}{:^%d}{}\n'%width).format(Avalon.FG.R,Avalon.FM.BD,str(msg),Avalon.FM.RST))
        print('{}{}{}{}'.format(Avalon.FG.LR,Avalon.FM.BD,'#'*width,Avalon.FM.RST))
        

    def debug(self,msg):
        print('{}{}[DEBUG]{}{}'.format(Avalon.FG.R, Avalon.FM.RDM, str(msg), Avalon.FM.RST), file=sys.stderr)
        if self.loglevel <= 0 and PLATFORM != 'win32':
            syslog.syslog(syslog.LOG_DEBUG, msg)

    def gets(self,msg):
        print('{}{}[USER]:{}{}'.format(Avalon.FG.Y, Avalon.FM.BD, msg, Avalon.FM.RST), end='')
        return input()

    def ask(self,msg, default=False):
        """ Gets a True / False answer from user

        This method will ask user a question that will
        require a true / false answer. Pressing enter without
        entering anything will return the default value.
        """
        if default is False:
            while True:
                ans = Avalon.gets(self,msg + ' [y/N]: ')
                if ans == '' or ans[0].upper() == 'N':
                    return False
                elif ans[0].upper() == 'Y':
                    return True
                else:
                    Avalon.warning(self,'Invalid Input!')
        elif default is True:
            while True:
                ans = Avalon.gets(self,msg + ' [Y/n]: ')
                if ans == '' or ans[0].upper() == 'Y':
                    return True
                elif ans[0].upper() == 'N':
                    return False
                else:
                    Avalon.warning(self,'Invalid Input!')
        else:
            raise TypeError('invalid type for positional argument: \' default\'')
