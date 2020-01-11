import re
import traceback
from time import sleep

import win32con
import win32gui


class cWindow:
    def __init__(self):
        self._hwnd = None

    def SetAsForegroundWindow(self):
        # First, make sure all (other) always-on-top windows are hidden.
        self.hide_always_on_top_windows()
        win32gui.SetForegroundWindow(self._hwnd)

    def Maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)

    def _window_enum_callback(self, hwnd, regex):
        """Pass to win32gui.EnumWindows() to check all open windows"""
        if self._hwnd is None and re.match(regex, str(win32gui.GetWindowText(hwnd))) is not None:
            self._hwnd = hwnd

    def find_window_regex(self, regex):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, regex)

    def hide_always_on_top_windows(self):
        win32gui.EnumWindows(self._window_enum_callback_hide, None)

    def _window_enum_callback_hide(self, hwnd, unused):
        if hwnd != self._hwnd:
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowLong(hwnd,
                                                                         win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST:
                className = win32gui.GetClassName(hwnd)
                if not (className == 'Button' or className == 'Shell_TrayWnd'):
                    win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)


def run():
    sleep(1)
    try:
        regex = ".*YC GUI.*"
        cW = cWindow()
        cW.find_window_regex(regex)
        cW.Maximize()
        cW.SetAsForegroundWindow()
        return True
    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())
        return False

# main()
