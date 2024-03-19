generate_kwargs = dict(
        max_new_tokens=256,
        repetition_penalty=1.35, # helps to prevent repeated lines over and over 
        do_sample=True, # enables multinomial sampling
        num_return_sequences=num_seqs, 
        num_beams=num_seqs, 
        early_stopping=True, # generation stops as soon as there are num_beams complete candidates
    )

SEQ:
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(debug=True) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(debug=True) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(debug=True) 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.run(host='0.0.0.0') 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') 


SEQ: 
@app.route('/url/ping', methods=['GET'])
def ping():
    #the URL to ping is stored as a variable "url"
    url = request.args.get('url')
    #run the ping command using the system command "ping"
    try:
        p = subprocess.Popen(['ping', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return redirect(url)
    except:
        return redirect(url)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', debug=True) 