from bottle import route, run, static_file

import client


@bottleroute("/")
def demo1():
    return static_file('demo1.html', root="")


@bottleroute("/")
def newlink():
    return static_file('newlink.html', root="")


@bottle.route('/client')
def code():
    return client.main()


run(host="localhost", port=8080, debug=True)
