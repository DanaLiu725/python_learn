import re
 
url = 'https://www.github.com/Dana/python'
 
reobj = re.compile(r"""(?xi)\A
[a-z][a-z0-9+\-.]*://                                # Scheme
([a-z0-9\-._~%!$&'()*+,;=]+@)?                       # User
([a-z0-9\-._~%]+                                     # Named or IPv4 host
|\[[a-z0-9\-._~%!$&'()*+,;=:]+\])                    # IPv6+ host
""")

match = reobj.search(url)

if match:
    print match.group(2)
