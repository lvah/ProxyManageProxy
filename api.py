from flask import Flask

# __name__， 当前文件的名称
# print(__name__)
from db import RedisClient

app = Flask(__name__)


# url: http://127.0.0.1:5000/
@app.route('/')
def index():
    html = """
        <h1 style="color:green">欢迎来到代理池监控维护器</h1>
        <hr/>
        <ul>
            <li><a href="/get_proxy/">代理IP的API地址</a></li>
            <li><a href="/count/">IP池代理个数</a></li>
        </ul>

    """
    return html


@app.route('/get_proxy/')
def get_proxy():
    r = RedisClient()
    proxy = r.random()
    return proxy


@app.route('/count/')
def count():
    r = RedisClient()
    return str(r.count())

if __name__ == '__main__':
    # 开启服务
    # 共享本机的所有IP， 0.0.0.0
    app.run(host='0.0.0.0', port =8888)
