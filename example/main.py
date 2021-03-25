import pyspaceapp
import pyspacemouse
import pyautogui
import time

config = pyspaceapp.Config(
    {
        "Opera": pyspacemouse.Config(
            button_callback_arr=[
                pyspacemouse.ButtonCallback(4, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', '1')),
                # Messenger
                pyspacemouse.ButtonCallback(9, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', 'shift',
                                                                                                      'tab')),
                # Reopen tab
                pyspacemouse.ButtonCallback(10, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', 'tab')),
                # Next tab
                pyspacemouse.ButtonCallback(11, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', 't')),
                # New tab
                pyspacemouse.ButtonCallback(12, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', 'shift',
                                                                                                       't')),
                # Previous tab
                pyspacemouse.ButtonCallback(13, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', 'w')),
                # Close tab
                pyspacemouse.ButtonCallback(3, lambda state, buttons, buttons_state: pyautogui.hotkey('alt', 'left')),
                # Close tab
                pyspacemouse.ButtonCallback(2, lambda state, buttons, buttons_state: pyautogui.hotkey('alt', 'right')),
                # Close tab
                pyspacemouse.ButtonCallback(5, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', '[')),

                # Workspace 1
                pyspacemouse.ButtonCallback(6, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', ']')),
                # Workspace 2
                pyspacemouse.ButtonCallback(7, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', ';')),
                # Workspace 3
                pyspacemouse.ButtonCallback(8, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', "'")),
                # Workspace 4
            ],
            dof_callback_arr=[
                pyspacemouse.DofCallback("pitch", lambda state, axis: pyautogui.scroll((axis*2)**3), 0.08, None, 0.1),
            ]
        ),

        "Chrome": pyspacemouse.Config(

        ),

        ".py": pyspacemouse.Config(
            button_callback_arr=[
                # Previous tab
                pyspacemouse.ButtonCallback(9, lambda state, buttons, buttons_state: pyautogui.hotkey('alt', 'left')),
                # Next tab
                pyspacemouse.ButtonCallback(10, lambda state, buttons, buttons_state: pyautogui.hotkey('alt', 'right')),
                # Close tab
                pyspacemouse.ButtonCallback(11, lambda state, buttons, buttons_state: pyautogui.hotkey('ctrl', '4')),
            ],
            dof_callback_arr=[
                pyspacemouse.DofCallback("yaw", lambda state, axis: pyautogui.scroll((axis * 2) ** 3), 0.08, None, 0.1),
                pyspacemouse.DofCallback("x", lambda state, axis: pyautogui.press("right"), 0.1,
                                         lambda state, axis: pyautogui.press("left"), 0.3),
                pyspacemouse.DofCallback("roll", lambda state, axis: pyautogui.press("right"), 0.01,
                                         lambda state, axis: pyautogui.press("left"), 0.5),
                pyspacemouse.DofCallback("pitch", lambda state, axis: pyautogui.press("up"), 0.03,
                                         lambda state, axis: pyautogui.press("down"), 0.5),
                pyspacemouse.DofCallback("y", lambda state, axis: pyautogui.press("up"), 0.2,
                                         lambda state, axis: pyautogui.press("down"), 0.3),
            ]
        ),

        "Inkscape": pyspacemouse.Config(
            dof_callback_arr=[
                pyspacemouse.DofCallback("x", lambda state, axis: pyautogui.hotkey("ctrl", "left"), 0.1,
                                         lambda state, axis: pyautogui.hotkey("ctrl", "right"), 0.2),
                pyspacemouse.DofCallback("y", lambda state, axis: pyautogui.hotkey("ctrl", "down"), 0.1,
                                         lambda state, axis: pyautogui.hotkey("ctrl", "up"), 0.2),
                pyspacemouse.DofCallback("z", lambda state, axis: pyautogui.press("+"), 0.3,
                                         lambda state, axis: pyautogui.press("-"), 0.2)
            ]
        ),

        "GIMP": pyspacemouse.Config(
            dof_callback_arr=[
                pyspacemouse.DofCallback("x", lambda state, axis: pyautogui.hotkey("shift", "left"), 0.1,
                                         lambda state, axis: pyautogui.hotkey("shift", "right"), 0.2),
                pyspacemouse.DofCallback("y", lambda state, axis: pyautogui.hotkey("shift", "down"), 0.1,
                                         lambda state, axis: pyautogui.hotkey("shift", "up"), 0.2),
                pyspacemouse.DofCallback("z", lambda state, axis: pyautogui.press("+"), 0.2,
                                         lambda state, axis: pyautogui.press("-"), 0.2),
            ]
        )
    }
)


def pyaoto_cfg():
    pyautogui.PAUSE = 0
    pyautogui.MINIMUM_DURATION = 0
    pyautogui.MINIMUM_SLEEP = 0


if __name__ == '__main__':
    pyaoto_cfg()
    app = pyspaceapp.App(config)
    app.setup()
    while True:
        app.run()
        time.sleep(0.001)

