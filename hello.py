from flask import Flask, url_for, render_template, Markup, request
app = Flask( __name__ )

@app.route( '/' )
def index(): pass

@app.route( '/login', methods = [ 'GET', 'POST' ] )
def login():
    url_for( 'static', filename = 'style.css' )
    # 'style.css' is stored in /static/style.css
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
    
@app.route( '/user/<username>' )
def profile( username ): pass
        
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