from flask import Flask,render_template,request

# create app
app = Flask(__name__)

#result = " "
temp = ""
@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        # show html form
        return render_template('calc_bkup.html')
#	        return '''
#	            <form method="post">
#	                <input type="text" name="expression" />
#	                <input type="submit" value="Calculate" />
#	            </form>
#	        '''
    elif request.method == 'POST': 
        # calculate result
#		expression = request.form.get('expression')
#		result = eval(expression)
#		result = request.form.get('abc', type=int)
#		if request.form['submit_button'] == "1":
        
        
        global temp
        if "one" in request.form:
            temp = request.form['name']
            result = temp + "1" 
        elif "two" in request.form:
            temp = request.form['name'] 
            result = temp + "2" 
        elif "three" in request.form:
            temp = request.form['name']
            result = temp + "3"
        elif "four" in request.form:
            temp = request.form['name']
            result = temp + "4"
        elif "five" in request.form:
            temp = request.form['name']
            result = temp + "5"
        elif "six" in request.form:
            temp = request.form['name']
            result = temp + "6"
        elif "seven" in request.form:
            temp = request.form['name']
            result = temp + "7"
        elif "eight" in request.form:
            temp = request.form['name']
            result = temp + "8"
        elif "nine" in request.form:
            temp = request.form['name']
            result = temp + "9"
        elif "zero" in request.form:
            temp = request.form['name']
            result = temp + "0"
        elif "dot" in request.form:
            temp = request.form['name']
            result = temp + "."
        elif "cancel" in request.form:
            temp = request.form['name']
            result = ""
        elif "plus" in request.form:
            temp = request.form['name']
            result = temp + "+"
        elif "minus" in request.form:
            temp = request.form['name']
            result = temp + "-"
        elif "mul" in request.form:
            temp = request.form['name']
            result = temp + "*"
        elif "slash" in request.form:
            temp = request.form['name']
            result = temp + "/"
        elif "open" in request.form:
            temp = request.form['name']
            result = temp + "("
        elif "close" in request.form:
            temp = request.form['name']
            result = temp + ")" 
        elif "back" in request.form:
            temp = request.form['name']
            result = temp[:-1]
        elif "percentile" in request.form:
            temp = request.form['name']
            result = temp + "%"
        elif "equals" in request.form:
            temp = request.form['name']
            if temp[-1] == "+" or temp[-1] == "-" or temp[-1] == "*" or temp[-1] == "/" or temp[0] == "+" or temp[0] == "-" or temp[0] == "*" or temp[0] == "/" or temp[0] == "%" or temp[-1] == "%":
                return render_template('calc_bkup2.html', result=temp)
            else :
                result2 = eval(temp)
                #print (result2)
                temp = str(result2)

                #result = ""
                return render_template('calc_bkup.html',  result=result2)

#		result = request.form.get('abc')
#		result = eval(abc)
        
        temp = result
        return render_template('calc_bkup.html',  result=result)
#        	return 'result: %s' % result
        
        

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