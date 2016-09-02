from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    from dns.resolver import query
    from urlparse import urlparse
    o = urlparse(request.host_url)
    txtrecords = query(o.hostname, 'TXT').response.answer[0]
    newpath="not found"
    for txtrecord in txtrecords:
        if (str(txtrecord)[1:8] == "dns301="):
            newpath = str(txtrecord)[8:-1]
    if (newpath[-1] == '$'):
        newpath = newpath[0:-1] + path
    return redirect(newpath, code=301)

if __name__ == '__main__':
    app.run()
