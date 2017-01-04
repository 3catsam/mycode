# coding:utf-8
#!flask/bin/python
from flask import Flask, jsonify, abort
from flask import make_response
from flask import url_for
from mysqlconn import conn


app = Flask(__name__)

'''tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]
'''

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)

'''@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})'''
@app.route('/api/sapaca', methods=['GET'])
def readme():
    return make_response('<h1>这是SAP账号数量的API</h1><p>http://url:port/api/sapaca 本说明页</p>\
<p>http://url:port/api/sapaca/date 获取所有时间，最长52条，降序</p>\
<p>http://url:port/api/sapaca/corp/<日期> 选定日期的数据，<日期>为YYYY-MM-DD格式</p>')
    
@app.route('/api/sapaca/corp/<date>', methods=['GET'])
def get_corp(date):
    # try:
    if len(date) != 10:
        abort(404)
    with conn.cursor() as cursor:
        # 执行sql语句，进行查询
        #date = '2016-12-23'
        sql = "SELECT inputdate as 'Date',corp_name as 'CORP',count(*) as 'UserNum' FROM SAPAccountAudit where inputdate = '%s' group by corp_name"
        cursor.execute(sql % date)
        # 获取查询结果
        result = cursor.fetchall()
        return jsonify(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    conn.commit()
    # finally:
    conn.close()
@app.route('/api/sapaca/date', methods=['GET'])
def get_date():
    with conn.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "SELECT distinct(inputdate) as 'Date' FROM SAPAccountAudit order by inputdate desc limit 52"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
        return jsonify(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    conn.commit()
    # finally:
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
