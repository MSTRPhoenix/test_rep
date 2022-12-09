import requests
import socket
import sys


def session_for_src_addr(addr: str) -> requests.Session:
    """
    Create `Session` which will bind to the specified local address
    rather than auto-selecting it.
    """
    session = requests.Session()
    for prefix in ('http://', 'https://'):
        session.get_adapter(prefix).init_poolmanager(
            # those are default values from HTTPAdapter's constructor
            connections=requests.adapters.DEFAULT_POOLSIZE,
            maxsize=requests.adapters.DEFAULT_POOLSIZE,
            # This should be a tuple of (address, port). Port 0 means auto-selection.
            source_address=(addr, 0),
        )

    return session


try:
    s = session_for_src_addr(sys.argv[1])
    r = s.get('https://google.com')
    #print(r.text[0][100])
    text = r.text
    print(text + '\r\n')
    div = text[text.find('lang')+6:100]
    div = div.split('\"')[0]
    print(div)
except:
    print('error')
# print([i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)])
