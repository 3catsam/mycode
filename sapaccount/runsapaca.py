# coding:utf-8
#!flask/bin/python
from flask import Flask, jsonify, abort
from flask import make_response,render_template
from flask import url_for
from mysqlconn import conn

from datetime import timedelta
from flask import request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    '''if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()
'''
    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
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
@app.route('/sapaca')
@crossdomain(origin='*')
def root():
    return render_template('index.html')
@app.errorhandler(404)
@crossdomain(origin='*')
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'}), 404)

'''@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})'''


@app.route('/sapaca/api', methods=['GET'])
@crossdomain(origin='*')
def readme():
    return make_response('<h1>这是获取SAP账号数量的API</h1>\
    <h3>http://url:port/sapaca/api 本说明页</h3>\
    <h3>http://url:port/sapaca/api/date 获取所有日期，最长52条，降序</h3>\
    <h3>http://url:port/sapaca/api/users/<日期> 选定日期的所有账号数据，<日期>为YYYY-MM-DD格式</h3>\
    <p>corp_name:公司名</p><p>countAll:所有账号数量</p><p>countIdle:闲置账号数量</p><p>inputdate:数据日期</p>')


@app.route('/sapaca/api/users/<date>', methods=['GET'])
@crossdomain(origin='*')
def get_users(date):
    # try:
    if len(date) != 10:
        abort(404)
    with conn.cursor() as cursor:
        # 执行sql语句，进行查询
        #date = '2016-12-23'
        sql = "select idle.inputdate,idle.corp_name,countAll,countIdle \
from ((select inputdate,corp_name,count(*) as countIdle from SAPAccountAudit a \
where a.`diffdays` > 30 and a.inputdate='%s' group by a.`CORP_NAME`) as idle,\
(select inputdate,corp_name,count(*) as countAll from SAPAccountAudit a \
where a.inputdate='%s' group by a.`CORP_NAME`) as allcount) \
WHERE idle.corp_name = allcount.corp_name"
        cursor.execute(sql % (date, date))
        # 获取查询结果
        result = cursor.fetchall()
        return jsonify(result)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    conn.commit()
    # finally:
    conn.close()


@app.route('/sapaca/api/date', methods=['GET'])
@crossdomain(origin='*')
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
    app.run(host='10.254.110.144', port=8000, debug=True)
