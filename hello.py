from flask import Flask, url_for, render_template, Markup, request, make_response
from werkzeug import secure_filename
app = Flask( __name__ )

@app.route( '/' )
def index():
    username = request.cookies.get( 'username' )
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    resp = make_response( render_template(...) )
    resp.set_cookie( 'username', 'the username' )
    return resp

@app.route( '/login', methods = [ 'GET', 'POST' ] )
def login():
    error = None
    if request.method == 'POST':
        if valid_login( request.form[ 'username' ],
                        request.form[ 'password' ] ):
            return log_the_user_in( request.form[ 'username' ] )
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template( 'login.html', error = error )

searchword = request.args.get( 'key', '' )
    
@app.route( '/user/<username>' )
def profile( username ): pass

@app.route( '/upload', methods = [ 'GET', 'POST' ] )
def upload_file():
    if request.method == 'POST':
        f = reques.files[ 'the_file' ]
        f.save( '/var/www/uploads/' + secure_filename( f.filename ) )
    return
    
        
with app.test_request_context():
    print( url_for( 'index' ) )
    print( url_for( 'login' ) )
    print( url_for( 'login', next = '/' ) )
    print( url_for( 'profile', username = 'John Doe' ) )
    '''
    results are as follows:
    /
    /login
    /login?next=/
    /user/John%20Doe
    '''

@app.route( '/hello/' )
@app.route( '/hello/<name>' )
def hello( name = None ):
    return render_template( 'hello.html', name = name )
    # searches /templates/ for 'hello.html'
    # alternatively, /application/templates/hello.html

#test Markup class    
Markup( '<strong>Hello %s!</strong>' ) % '<blink>hacker</blink>'
Markup.escape('<blink>hacker</blink>')
Markup('<em>Marked up</em> &raquo; HTML').striptags()

with app.test_request_context( '/hello', method = 'POST' ):
    # now you can do something with the request until the
    # end of the with block, such as basic assertion
    assert request.path == '/hello'
    assert request.method == 'POST'
    
with app.request_context( environ ):
    assert request.method = 'POST'

if __name__ == '__main__':
    app.run( debug = True )