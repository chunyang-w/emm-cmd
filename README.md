# 🐠 EMM - what is the correct spell of the command?

All of us have been there, we are trying to write a command, but we are not sure what is the correct spelling of the command - "emm, what is that command again?"

Cool things is that, we can now use AI to help us to find the correct command.

Just try: `emm "what is the command to find all files start with 'data'?"`

Here is what it will return:

![](https://raw.githubusercontent.com/chunyang-w/chunyang-w.github.io/pic/202311232356431.webp)

## ⚙️ Installation

```python
pip install emm-cmd
```

... and you are good to go!

## 🔧 Usage

### 🔐 Authentication

If you are using for the first time, you will need to run the following command after installation:

```shell
spt set_auth <your_open_ai_key>
```

If you have not registered for an open ai key, you will need to register [here](https://beta.openai.com/account/api-keys).

Please ensure that you have key registered, and your account have sufficient credits to use the API.


### 💬 Command

```shell
emm <your_missing_command>
```

after this, hopefully you will see a table of commands that you are looking for, with explanation.

Please use your arrow key to select and run.