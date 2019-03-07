from bottle import route, run, static_file

import client


@route("/")
def demo1():
    return static_file('demo1.html', root="")


@route("/")
def newlink():
    return static_file('newlink.html', root="")


@route('/client')
def code():
    return client.main()
    print(connected)


run(host="localhost", port=8080, debug=True)
