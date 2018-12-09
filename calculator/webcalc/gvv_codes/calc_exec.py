from flask import Flask,render_template,request

# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
        # show html form
		return render_template('calc.html')
#	        return '''
#	            <form method="post">
#	                <input type="text" name="expression" />
#	                <input type="submit" value="Calculate" />
#	            </form>
#	        '''
	elif request.method == 'POST':
        # calculate result
        	expression = request.form.get('expression')
        	result = eval(expression)
        	return 'result: %s' % result

# run app
if __name__ == '__main__':
	app.run(debug=True)




#app=Flask(__name__)
#@app.route('/')
#
#def student():
#	return render_template('calc.html')
#
#if __name__=='__main__':
#	app.run(debug = True)
