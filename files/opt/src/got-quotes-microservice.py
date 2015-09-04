from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    'Winter is coming.',
    'You know nothing, Jon Snow.',
    'A Lannister always pays his debts.',
    'We do not sow.',
    'The First Sword of Braavos does not run.',
    'Valar Morghulis.',
    'Hodor!',
    'The King in the North!',
    'When you play a game of thrones you win or you die.',
    'The things I do for love.',
    'A very small man can cast a very large shadow.'
]

counters = [0 for _ in xrange(len(quotes))]

data = {
    'quote': ''
}

@app.route('/api/quote/<quoteid>')
def api_quote(quoteid):

    if quoteid.isdigit():
        quoteid = int(quoteid)
    else:
        return not_found('Invalid quote value.')

    if 0 <= quoteid <= len(quotes) - 1:
        data['quote'] = quotes[quoteid]
        counters[quoteid] += 1
        data['counter'] = counters[quoteid]
        resp = jsonify(data)
        resp.status_code = 200
        return resp
    else:
        return not_found('Quote not found.')

@app.route('/api/quote/random')
def api_quote_random():
    from random import randint
    quote_idx = randint(0,len(quotes) -1)
    counters[quote_idx] += 1
    data['quote'] = quotes[quote_idx]
    data['counter'] = counters[quote_idx]
    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/api/quote/top')
def api_quote_top():
    max_idx = 0
    max_value = 0
    for idx, value in enumerate(counters):
        print "idx: ", idx, " value: ", value
        if value > max_value:
            max_idx = idx
            max_value = value

    data['quote'] = quotes[max_idx]
    data['counter'] = max_value
    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/healthcheck')
def healthcheck():
    data = {
        'status': 'ok'
    }
    resp = jsonify(data)
    resp.status_code = 200
    return resp
    
@app.route('/Status')
def status():
    return 'Eureka!'
    
@app.errorhandler(404)
def not_found(error='Error'):
    message = {
            'status': 404,
            'message': error
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp    

if __name__ == '__main__':
    app.run(host='0.0.0.0')

