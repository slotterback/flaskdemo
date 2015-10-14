from flask import Flask, url_for
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

    
if __name__ == '__main__':
    app.run( debug = True )