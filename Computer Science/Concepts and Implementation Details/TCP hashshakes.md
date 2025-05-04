In TCP (Transmission Control Protocol), **3-way handshake** and **2-way teardown** are processes used to establish and terminate a reliable connection between a client and a server.

---

### 🔁 **3-Way Handshake (Connection Establishment)**

This is the process by which a TCP connection is established. It ensures both sides are ready and agree on initial sequence numbers.

**Steps:**

1. **SYN (synchronize)** – The client sends a TCP segment with the SYN flag set, initiating the connection and proposing a sequence number (say, `Seq = x`).
2. **SYN-ACK** – The server responds with a TCP segment that has both the SYN and ACK flags set. It acknowledges the client’s SYN by setting `Ack = x + 1` and proposes its own sequence number (`Seq = y`).
3. **ACK** – The client sends an ACK back to the server, acknowledging `Seq = y` with `Ack = y + 1`.

✅ After this exchange, the connection is **established**, and data transfer can begin.

---

### 🔚 **2-Way Teardown (Connection Termination)**

When a TCP connection is closed, it typically involves **4 steps**, but in concept, it's called a **2-way teardown**, as each side independently closes its half of the connection.

**Steps:**

1. **FIN (from one side)** – One side (say, the client) sends a TCP segment with the FIN flag to indicate it has finished sending data.
2. **ACK (from the other side)** – The server acknowledges the FIN.
3. **FIN (from server)** – The server later sends its own FIN when it's done sending data.
4. **ACK (from client)** – The client acknowledges the server's FIN.

✅ After this exchange, the connection is **fully closed**.

---

### Summary Table:

|Phase|Direction|Flag(s)|Purpose|
|---|---|---|---|
|Handshake Step 1|Client → Server|SYN|Initiate connection|
|Handshake Step 2|Server → Client|SYN-ACK|Acknowledge & sync back|
|Handshake Step 3|Client → Server|ACK|Confirm server's sync|
|Teardown Step 1|Client → Server|FIN|Client wants to close connection|
|Teardown Step 2|Server → Client|ACK|Acknowledge client’s FIN|
|Teardown Step 3|Server → Client|FIN|Server wants to close connection|
|Teardown Step 4|Client → Server|ACK|Acknowledge server’s FIN|

![[ChatGPT Image May 4, 2025, 05_05_12 PM.png]]