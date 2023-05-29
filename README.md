# streamgpt

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
git clone https://github.com/TesfaAsmara/streamgpt.git
```

## How to use

To stream messages from Twitch IRC you need to get a to token for
authentication. To do that you need to:

1.  Create a Twitch account
2.  Go to https://twitchapps.com/tmi/ to request an auth token for your
    Twitch account. You’ll need to click “Connect with Twitch” and
    “Authorize” to produce a token

Your token should look something like
“oauth:yj23Ds7BB97Hju85QYTenVox12x03”. Including your token, there’s two
constants we’ll define for the connection to a Twitch channel’s chat
feed:

1.  Your Twitch account nickname
2.  The channel you want to join

The channel you want to join should be preceeded by a hashtag. So if I
wanted to join `https://www.twitch.tv/kaicenat`, then I would pass in
`#kaicenat`.

## Code

``` python
from core import join_channel, read_chat

# Enter your twitch nickname, token
socket = join_channel(nickname="streamgpt", 
                        token="oauth:yj23Ds7BB97Hju85QYTenVox12x03",  
                        channel="#kaicenat")

# This will store the chat messages to a file named chat.log
read_chat(socket)

# close the socket when you're done reading messages
socket.close()
```
