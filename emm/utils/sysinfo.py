import os
import platform
import psutil


def get_parent_process_name():
    parent_process = psutil.Process(os.getppid())
    return parent_process.name()


class SysInfo():
    def __init__(self):
        self.os_name = os.name
        self.platform = platform.system()
        self.architecture = platform.architecture()
        self.release = platform.release()
        self.shell = os.environ.get('SHELL')
        self.using_powershell = "powershell" in self.shell.lower()

    @property
    def info(self):
        return {
            "os_name": self.os_name,
            "platform": self.platform,
            "architecture": self.architecture,
            "release": self.release,
            "shell": self.shell,
            "using_powershell": self.using_powershell,
        }
