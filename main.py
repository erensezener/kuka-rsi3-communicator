"""
Author: Eren Sezener (erensezener@gmail.com)
Date: May 11, 2014

Description: 

Status: Works correctly.

Dependencies:

Known bugs: -

"""

from multiprocessing import Process, Pipe
import server
import client

# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()

if __name__ == '__main__':
    parent_connection, child_connection = Pipe()
    # p = Process(target=f, args=(child_connection,))
    # p.start()
    # print parent_connection.recv()   # prints "[42, None, 'hello']"
    # p.join()
    server_process = Process(target=server.run_server, args=(parent_connection,))
    client_process = Process(target=client.run_client, args=(child_connection,))