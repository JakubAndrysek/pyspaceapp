import pyspacemouse
from typing import Callable, Union, List, Dict
import subprocess
import os
import metronome_loop


class Config:
    def __init__(self, config: Dict[str, pyspacemouse.Config]):
        self.check_config(config)
        self.config = config

    def add(self, config: Dict[str, pyspacemouse.Config]):
        self.check_config(config)
        for name, cfg in config.items():
            self.config[name] = cfg

    @staticmethod
    def check_config(config):
        if type(config) is dict:
            for name, cfg in config.items():
                if type(name) is str:
                    pass
                else:
                    raise Exception(f"Some pyspacemouse.Config key is not string")

                if isinstance(cfg, pyspacemouse.Config):
                    pass
                else:
                    raise Exception(f"'pyspacemouse.Config[{name}]' is not instance of 'pyspacemouse.Config'")
        else:
            raise Exception("Input is not dict of 'str': 'pyspacemouse.Config'")


class App:
    def __init__(self, appConfig: Config):
        self.appConfig = appConfig.config
        self.active_app_met = metronome_loop.metronome(100, self.active_app_loop)
        self.active_app = None
        self.active_app_last = None
        self.device_name = None
        self.device_config = None

    def get_active_app(self):
        x = subprocess.run(['xdotool getwindowfocus getwindowname'], shell=True, capture_output=True)
        return x.stdout.decode("utf-8")[:-1]

    def active_app_loop(self):
        self.active_app = self.get_active_app()
        if self.active_app != self.active_app_last and self.active_app is not None:
            device_name = None
            device_config = None
            for name, cfg in self.appConfig.items():
                if self.active_app.find(name) > 0:
                    device_name = name
                    device_config = cfg
                    self.active_app_last = self.active_app
                    break

            if device_name is not None and device_config is not None:
                self.device_config = device_config
                self.device_name = device_name
                pyspacemouse.config_set(device_config)
                print(device_name)
            else:
                pyspacemouse.config_remove()
                print(f"Not configured -> {self.active_app}")

            self.active_app_last = self.active_app

    def setup(self):
        mouse = pyspacemouse.open()
        # disable SpaceMouse as mouse input in Linux
        os.system(f"xinput --disable '{mouse.vendor_name} {mouse.product_name}'")

    def run(self):
        pyspacemouse.read()
        self.active_app_met.loop()
