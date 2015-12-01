Trying to timeout remi socket.

On one shell run:

    python pub_rate.py

This will publish at 10Hz rate. (or whatever you put after `pub_rate.py` if you want to change it).

On another shell run the remi app (after launching `pub_rate.py`!!):

    python test_update_rate.py

The rate of updating is also controlled by the number after `test_update_rate.py` (if you want to change it).

It will show in the shell sequence number of the message received. In the browser you'll see
a label updating with the same value.

Be warned that if you do control+c on test_update_rate.py it will not stop. There is some
issue with the signals catching. To completely stop it send it to the background with
`Control+Z` and do `kill -9 %%` (which is killing the process in the background).
(Any idea on how to overcome this?).


After a while (60s for me, every time) I get:

````
Exception happened during processing of request from ('127.0.0.1', 50888)
Traceback (most recent call last):
  File "/usr/lib/python2.7/SocketServer.py", line 593, in process_request_thread
    self.finish_request(request, client_address)
  File "/usr/lib/python2.7/SocketServer.py", line 334, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/usr/lib/python2.7/SocketServer.py", line 649, in __init__
    self.handle()
  File "/usr/local/lib/python2.7/dist-packages/remi/server.py", line 155, in handle
    if not self.read_next_message():
  File "/usr/local/lib/python2.7/dist-packages/remi/server.py", line 169, in read_next_message
    length = self.rfile.read(2)
  File "/usr/lib/python2.7/socket.py", line 380, in read
    data = self._sock.recv(left)
timeout: timed out
````

To see the error, just check the browser and you'll see the page stuck with the last number before the
timeout.

This happens with both the current master and with the reliable_websocket branch.

