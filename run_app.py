import optparse

from apps.routes import app
from sys import exit as sys_exit


def run_with_twisted(debug_mode, port=8000):
    """
    Import twisted dependencies, set app as WSGIResource and start reactor.
    """
    try:
        from twisted.internet import reactor
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource
    except ImportError:
        print 'ERROR: twistd is not installed in this environment. Please install appropriate version of twistd and try again.'
        sys_exit(1)

    print 'Twisted on port {port} ...'.format(port=port)
    app.debug = debug_mode
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)

    reactor.listenTCP(port, site, interface="0.0.0.0")
    reactor.run()


def run_with_builtin(port, debug_mode):
    """
    Run with default builtin flask/klein/bottle app
    """
    print 'Built-in development server on port {port} ...'.format(port=port)
    app.run(host="0.0.0.0",port=port,debug=debug_mode)


def main():
    """
    Parse the options to get WSGi container of choice, the debug mode, and the port number"
    """
    parser = optparse.OptionParser(usage="%prog [options]  or type %prog -h (--help)")
    parser.add_option('-p', '--port', help='Port on which to run service, defaults to 8000', dest="app_port", type="int", default=8000);
    parser.add_option('--debug', help='When passed, sets app in debug mode', dest="debug_mode", action="store_true", default=False);
    parser.add_option('-w', '--with', type='choice', action='store', dest='app_container',
                      choices=['builtin', 'tornado', 'twistd'], default='builtin',
                      help='WSGI container to be used to wrap and run the app. Valid options - builtin/tornado/twistd. Defaults to builtin')
    (options, args) = parser.parse_args()

    port = options.app_port
    debug_mode = options.debug_mode

    if options.app_container == 'twistd':
        run_with_twisted(debug_mode, port)
    else:
        run_with_builtin(port, debug_mode)


if __name__ == '__main__':
    main()
