from flask import Flask , render_template

app_1= Flask(__name__)

@app_1.route('/') 
def hello():
    return'<h1 style = "color:blue">Hello world ! </h>' 
@app_1.route('/athour') 
def  wolcame():
    return'<h1 style = "color:blue">Hello world ather ! </h>' 
  
if __name__ == '__main__':
    app_1.run( debug=True ,port = 330)
  