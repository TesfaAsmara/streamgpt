# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['join_channel', 'read_chat']

# %% ../nbs/00_core.ipynb 1
def join_channel(nickname, token, channel):
    import socket
    server = "irc.chat.twitch.tv"
    port = 6667

    sock = socket.socket()

    sock.connect((server,port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    return sock

def read_chat(socket):
    import logging

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s — %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

    while True:
        resp = socket.recv(2048).decode('utf-8')
        print(resp)
        if resp.startswith('PING'):
            socket.send("PONG\n".encode('utf-8'))
        
        elif len(resp) > 0:
            logging.info(resp)
