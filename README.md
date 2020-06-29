[README на русском](README_RU.md)

# ip-teller

This app is telegram bot which can send a message with current ip-address of
 host it runs on to the user. There is also function of authorization, so admin
 can choose who can use this bot.

## Installation

The app is written in python3. In case of you want to use this app for your
 server, all you need for now to set up this app is to follow steps:

**Step 1**: Clone repository:

```
# git clone https://github.com/gogagum/ip-teller
```
**Step 2**: Create your bot at botfather.

**Step 3**: Create file `token.txt` at the root of the repo. And put token
 to this file.

**Step 4**: install requirements by typing

```
# pip3 install requirements.txt
```

## How to use

For now I recommend to use tool which is called
 [screen](https://linux.die.net/man/1/screen) (`man 1 screen`). I start this app 
 typing a command:


```
# screen -dmS telebot python3 main.py
```

After starting app using `screen`, you can easily logout and bot will
 continue working.

When a message `/register` is sent to the bot it asks for a password,
 which you can get by typing:
```
# cat passwd.txt
```

## But you should not use it

I guess it crashes when internet connection fails and it is not
 the only problem for now. It is not usable yet, as it is first version.
 The reason of publication of this version is to show idea and first results.
