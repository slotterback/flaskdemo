from flask import Flask, url_for
app = Flask( __name__ )

@app.route( '/' )
def index(): pass

@app.route( '/login' )
def login(): pass
    
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