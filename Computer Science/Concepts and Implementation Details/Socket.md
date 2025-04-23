A socket is an endpoint of a two-way communication link between two programs running on a network, acting as a software construct for sending and receiving data.

In Unix-like operating systems, **sockets are treated as files**. Each open socket gets a **file descriptor**, just like a file opened with `open()`.

When a client creates a socket using `socket()`, it gets **one file descriptor**.

A typical TCP server involves:
1. Listening socket ---> socket + blind + listen
2. Accepted socket ---> accept

**Breakdown:**

- `listen_fd`: The **listening socket** (1 FD).
- `client_fd`: Each **new connection** gets **a new file descriptor**.

✅ **Total file descriptors:**

- **Before accept():** 1 (only the listening socket).
- **After accept():** 2 (listening socket + new connection FD).
- **For N clients:** `1 (listen_fd) + N (client_fds)`


### **How It Works (Step-by-Step)**

1. **Server accepts a client connection**
    - `accept()` returns a new **file descriptor (`client_fd`)** for the client.
2. **Server writes data to `client_fd`**
    - The server calls `write(client_fd, buffer, size)` or `send(client_fd, buffer, size, 0)`.
3. **TCP takes over**
    - The kernel buffers the data and TCP ensures reliable delivery to the client.
    - TCP handles packetization, retransmissions (if needed), and ordering.
4. **Client reads the message**
    - The client calls `recv(client_fd, buffer, size, 0)` to retrieve the message.


### **Analogy: Writing to a File vs. Writing to a Socket**

|Operation|Writing to a File (`fd`)|Writing to a Socket (`client_fd`)|
|---|---|---|
|`write(fd, buf, size)`|Writes data to a file|Writes data to a socket|
|`read(fd, buf, size)`|Reads from a file|Reads from the network socket|
|**Kernel role**|Handles disk I/O|Handles TCP transmission|
