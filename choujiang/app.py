# 让我们的电脑支持服务访问
# 需要一个web框架
# pip install Flask   ps:Flask 是一个使用 Python 编写的轻量级 Web 应用框架
from flask import Flask,render_template
from random import randint   # 运用其生成随机数的功能


app = Flask(__name__)

hero = [
    '吴邪','张起灵','胖子','吴三省','解连环','钟离','温迪','雷电将军','纳西妲','芙宁娜',
    '富岗义勇','宇髓天元'
]

# 创建一个URL,并于下面函数绑定，通过访问IP地址可以实现下函数功能
@app.route('/index')    
def index():
    return render_template('index.html', heros = hero)


@app.route('/choujiang')
def choujiang():
    num = randint(0,len(hero)-1)
    return render_template('index.html', heros = hero, h = hero[num])




app.run(debug=True)  # 使html内容更改时不需要再次运行程序就可以改变网页内容，实时更新