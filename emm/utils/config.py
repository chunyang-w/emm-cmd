import os
import appdirs


class Config():
    def __init__(self):
        self.app_name = "spt"
        self.auth_file = "openai_key.conf"

    @property
    def config_path(self):
        return appdirs.user_config_dir(
            self.app_name)

    @property
    def config_file_path(self):
        return os.path.join(
            self.config_path, self.auth_file)

    def write_config(self, content={
        "key": "value",
    }):
        if not os.path.exists(self.config_path):
            os.makedirs(self.config_path)

        config = {}
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=', 1)
                    config[key] = value

        config.update(content)

        # Write updated config
        with open(self.config_file_path, 'w') as file:
            for key, value in config.items():
                file.write(f"{key}={value}\n")

    def read_config(self):
        config = {}
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
        return config

    def show_config(self):
        config = self.read_config()
        print("Config:", config)
        return

    def get_config_value(self, key):
        config = self.read_config()
        return config[key]
