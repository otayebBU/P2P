# P2P

The P2P project has three primary parts:

1) secure_utils.py: Encrypts and decrypts messages to ensure communication security.

2)peer.py: Creates a peer-to-peer (P2P) system that allows users to send and receive encrypted communications.

3) api.py: An API for managing user registrations, subscriptions, blocking, muting, and message delivery logic.


Secure_utils.py is responsible for securing peer interactions with the pycryptodome package.Ensure that communications sent by peers are encrypted.


P2P allows peers to communicate directly with one another using sockets. A peer-to-peer network does not rely on a central server; instead, users can connect directly to one another. The steps involve creating a server, sending messages, and threading.

The socket library offers low-level networking operations, which are ideal for basic P2P communication because they allow direct TCP connections between peers.


Finally, the API creates RESTful API endpoints using FastAPI, which includes peer registration, subscription, blocking and muting, and message transmission. 


