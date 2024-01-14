from flask import Flask,render_template,request, redirect,session
# Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'clicked' 
@app.route('/')          # The "@" decorator associates this route with the function immediately following

@app.route('/') 
def index():
    #set default session key as 1 
    session['key'] = 1
    session["num_of_visit"] = 1
    session["num_counter_used"] = 0
    print('Session:',session)
    return render_template('index.html')

@app.route('/count', methods = ['POST']) 
def increase_count():
    #increment the session['key'] value by one
    session['key'] += 1
    session["num_of_visit"]+=1
    session["num_counter_used"]+=1
    print('Session:',session)
    return render_template('count.html')

@app.route('/count_2', methods = ['POST']) 
def increase_count_by_2():
    session['key'] += 2
    session["num_of_visit"]+=1
    session["num_counter_used"]+=1
    print('Session:',session)
    return render_template('count.html')

@app.route('/count_define', methods = ['POST']) 
def increase_count_by_user():
    if(request.form['count_define']== ''):
        num_fr_req = 1
    else:
        num_fr_req= request.form['count_define']
    num = int(num_fr_req)
    session['key'] += (num)
    session["num_of_visit"]+=1
    session["num_counter_used"]+=1
    print('Session:',session)
    return render_template('count.html')


# @app.route('/reset', methods = ['POST']) 
# def make_reset():
#     print("Reset")
#     session['key'] = 0
#     session.clear()		# clears all keys
#     session.pop('key')		# clears a specific key
#     return render_template('index.html')
@app.route('/destroy_session', methods= ['POST']) 
def destroy():
    # print("Reset")
    # print("session",session)
    # session.clear()		# clears all keys
    session['key'] = 1

    print("session",session)
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.