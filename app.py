from flask import Flask, request, render_template,flash, redirect
from forex_python.converter import CurrencyRates,CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension
import convert

app = Flask(__name__)

app.config['SECRET_KEY'] = 'myman'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug = DebugToolbarExtension(app)



@app.route('/')
def converter():
    '''shows converter'''

    return render_template('base.html')

@app.route('/result')
def form():
    '''handles the form and errors'''
    error = False

    from_currency = request.args['convert-from']
    to_currency = request.args['convert-to']
    amount = convert.check_amount(request.args['amount'])
   
    if not convert.check_currency_code(from_currency):
        error = True
        flash(f'Not a valid Currency Code {from_currency}')
    
    if not convert.check_currency_code(to_currency):
        error = True
        flash(f'Not a valid Currency Code {to_currency}')

    if amount is None:
        error = True
        flash('Not a valid Amount')
        
    if error == True:
        return render_template('base.html')
    
    
    result = convert.currency_converter(from_currency,to_currency,amount)
 
    return render_template("base.html",result = result)
    
