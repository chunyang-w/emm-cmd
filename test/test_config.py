from emm.utils.config import Config

set_open_ai_key = False

print("Test Config")

# 0. print config folder
print("Config path:", Config().config_path)

# 1. write_config
Config().write_config(content={
    "test_key": "test_value"
    })

# 2. read_config
config = Config().get_config_value("test_key")
assert config == "test_value"

# 3. show_config
Config().show_config()

# 4. set openai_key
if set_open_ai_key:
    open_ai_key = input("Please enter your OpenAI key: ")
    Config().write_config(content={
        "openai_key": open_ai_key
    })
