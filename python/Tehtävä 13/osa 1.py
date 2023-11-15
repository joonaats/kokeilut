from flask import Flask, request

app = Flask(__name__)


@app.route('/alkuluku/<luku1>')
def alkuluku(luku1):
    luku = int(luku1)
    isPrime = ""
    check = 0
    for i in range(1, luku):
        if luku % i == 0 and i != 1 and i != luku:
            check = 1
    if check == 1:
        isPrime = False
    else:
        isPrime = True

    vastaus = {
        "Number": luku,
        "isPrime": isPrime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)