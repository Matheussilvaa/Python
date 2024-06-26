from flask import Flask

projetoA3 = Flask()

@projetoA3.route('/')
def index ():
    return ''