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


def main():
    parent_connection, child_connection = Pipe()
    server_process = Process(target=server.run_server, args=(parent_connection,))
    server_process.start()
    client.run_client(child_connection)
    server_process.terminate()

if __name__ == '__main__':
    main()