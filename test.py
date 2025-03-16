# coding=utf-8
import datetime
import json
import sys
import time
import os.path
import traceback
import hashlib
from json import dumps

from flask import Flask
from flask import request
from flask import render_template, send_from_directory
from dict_to_db import DictToDb

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
db = DictToDb(os.path.join(BASE_DIR, "DATA.db"), check_same_thread=False)
SAVE_FINGERPRINT_DIR = os.path.join(os.path.join(BASE_DIR, 'static'), 'save_fingerprint')
SAVE_FINGERPRINT_DIR_1 = os.path.join(os.path.join(BASE_DIR, 'static'), 'save_information')
if not os.path.exists(SAVE_FINGERPRINT_DIR):
    os.makedirs(SAVE_FINGERPRINT_DIR)
if not os.path.exists(SAVE_FINGERPRINT_DIR_1):
    os.makedirs(SAVE_FINGERPRINT_DIR_1)


def get_total_count(search_time=None):
    if search_time:
        sql = "select count() as total_count from t2 where insert_time>?;"
        return db.execute(sql, (search_time,)).fetchone()['total_count']
    else:
        return db.execute('select count() as total_count from t2;').fetchone()['total_count']


def compute_browser_language(total_count, search_time):
    sql = "select count(BrowserLanguage)as count,BrowserLanguage as name " \
          "from t2 where insert_time >? group by BrowserLanguage"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


def compute_system(total_count, search_time):
    sql = "select count(system)as count,system as name from t2 where insert_time >? group by system"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


def compute_browser(total_count, search_time):
    sql = "select count(browser)as count,browser as name from t2 where insert_time>? group by browser"
    select_data = db.execute(sql, (search_time,)).fetchall()
    print(select_data)
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


def compute_timezone(total_count):
    sql = "select count(simpleTimeZone)as count,simpleTimeZone as name from t2 group by simpleTimeZone"
    select_data = db.execute(sql).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# vendor
def compute_vendor(total_count, search_time):
    sql = "select count(webglC)as count,webglC as name from t2 where insert_time >? group by webglC"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# renderer
def compute_renderer(total_count, search_time):
    sql = "select count(webglC1)as count,webglC1 as name from t2 where insert_time >? group by webglC1"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# version
def compute_version(total_count, search_time):
    sql = "select count(webglC2)as count,webglC2 as name from t2 where insert_time >? group by webglC2"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# SHADING_LANGUAGE_VERSION
def compute_SHADING_LANGUAGE_VERSION(total_count, search_time):
    sql = "select count(webglC3)as count,webglC3 as name from t2 where insert_time >? group by webglC3"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# Vendor
def compute_Vendor(total_count, search_time):
    sql = "select count(webglC4)as count,webglC4 as name from t2 where insert_time >? group by webglC4"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# Renderer
def compute_Renderer(total_count, search_time):
    sql = "select count(webglC5)as count,webglC5 as name from t2 where insert_time >? group by webglC5"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# bool_2_string
def compute_bool_2_string(total_count, search_time):
    sql = "select count(webglC6)as count,webglC6 as name from t2 where insert_time >? group by webglC6"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# angle
def compute_angle(total_count, search_time):
    sql = "select count(webglC7)as count,webglC7 as name from t2 where insert_time >? group by webglC7"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# caveat
def compute_caveat(total_count, search_time):
    sql = "select count(webglC8)as count,webglC8 as name from t2 where insert_time >? group by webglC8"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# vectors
def compute_vectors(total_count, search_time):
    sql = "select count(webglC9)as count,webglC9 as name from t2 where insert_time >? group by webglC9"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# ANGLE
def compute_ANGLE(total_count, search_time):
    sql = "select count(webglC10)as count,webglC10 as name from t2 where insert_time >? group by webglC10"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# texture
def compute_texture(total_count, search_time):
    sql = "select count(webglC11)as count,webglC11 as name from t2 where insert_time >? group by webglC11"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# WEBGL_draw_buffers
def compute_WEBGL_draw_buffers(total_count, search_time):
    sql = "select count(webglC12)as count,webglC12 as name from t2 where insert_time >? group by webglC12"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


# shader
def compute_shader(total_count, search_time):
    sql = "select count(webglC13)as count,webglC13 as name from t2 where insert_time >? group by webglC13"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.005:
            result_data['其它'] = result_data['其它'] + scale
        else:
            result_data[data['name']] = scale
    return [{"name": k, "value": v} for k, v in result_data.items()]


@app.route('/save_fingerprint', methods=['POST'])
def save_fingerprint():
    try:
        post_data = request.json
        post_data.update(dict(request.headers))
        del post_data['Referer']
        s = json.dumps(post_data)
        sha256 = hashlib.sha256()
        sha256.update(s.encode('utf-8'))
        fp = sha256.hexdigest()
        post_data['User'] = "User"
        post_data['fingerprint'] = fp
        db.insert(post_data)
        with open(os.path.join(SAVE_FINGERPRINT_DIR, f'{time.time()}.txt'), 'w', encoding='utf8') as f:
            f.write("js属性:\n")
            f.write(json.dumps(post_data, ensure_ascii=False, indent=4, separators=(',', ':')) + '\n')
            f.write('headers:\n')
            f.write(json.dumps(dict(request.headers), ensure_ascii=False, indent=4, separators=(',', ':')))
        return {"code": 0, "msg": "服务器已收到您的指纹信息！"}
    except:
        traceback.print_exc()
        return {"code": 1, "msg": "出错了！请检查BUG！"}


@app.route('/compute_data', methods=['GET'])
def compute_data():
    try:
        start_time = request.args.get("start_time")
        dt = datetime.datetime.now()
        if start_time == "today":
            search_time = dt - datetime.timedelta(days=0, seconds=dt.second, microseconds=dt.microsecond,
                                                  milliseconds=0,
                                                  minutes=dt.minute, hours=dt.hour, weeks=0)
        elif start_time == "three_day":
            search_time = dt - datetime.timedelta(days=3, seconds=dt.second, microseconds=dt.microsecond,
                                                  milliseconds=0,
                                                  minutes=dt.minute, hours=dt.hour, weeks=0)
        elif start_time == "week":
            search_time = dt - datetime.timedelta(days=7, seconds=dt.second, microseconds=dt.microsecond,
                                                  milliseconds=0,
                                                  minutes=dt.minute, hours=dt.hour, weeks=0)
        else:
            search_time = datetime.datetime(year=1970, month=1, day=1)
        search_count = get_total_count(search_time)
        total_count = get_total_count()
        browser_language_info = compute_browser_language(search_count, search_time)
        system_info = compute_system(search_count, search_time)
        browser_info = compute_browser(search_count, search_time)
        timezone_info = compute_timezone(search_count)
        # vendor
        vendor_info = compute_vendor(search_count, search_time)
        #renderer
        renderer_info = compute_renderer(search_count, search_time)
        version_info = compute_version(search_count, search_time)
        sHADING_LANGUAGE_VERSION_info = compute_SHADING_LANGUAGE_VERSION(search_count, search_time)
        Vendor_info = compute_Vendor(search_count, search_time)
        Renderer_info = compute_Renderer(search_count, search_time)
        bool_2_string_info = compute_bool_2_string(search_count, search_time)
        angle_info = compute_angle(search_count, search_time)
        caveat_info = compute_caveat(search_count, search_time)
        vectors_info = compute_vectors(search_count, search_time)
        aNGLE_info = compute_ANGLE(search_count, search_time)
        texture_info = compute_texture(search_count, search_time)
        wEBGL_draw_buffers_info = compute_WEBGL_draw_buffers(search_count, search_time)
        shader_info = compute_shader(search_count, search_time)

        # canvas
        # canvas_info = compute_canvas(search_count, search_time)
        # canvas1_info = compute_canvas1(search_count, search_time)
        # canvas2_info = compute_canvas2(search_count, search_time)
        # canvas3_info = compute_canvas3(search_count, search_time)
        # canvas4_info = compute_canvas4(search_count, search_time)
        # canvas5_info = compute_canvas5(search_count, search_time)
        # webgl_info = compute_webgl(search_count, search_time)
        response_data = {"code": 0, "msg": "success", "total_count": total_count,
                         "search_count": search_count,
                         "data": {
                             "browser_language_info": browser_language_info,
                             "system_info": system_info,
                             "browser_info": browser_info,
                             "timezone_info": timezone_info,
                             "vendor_info": vendor_info,
                             "renderer_info": renderer_info,
                             "version_info": version_info,
                             "sHADING_LANGUAGE_VERSION_info": sHADING_LANGUAGE_VERSION_info,
                             "Vendor_info": Vendor_info,
                             "Renderer_info": Renderer_info,
                             "bool_2_string_info": bool_2_string_info,
                             "angle_info": angle_info,
                             "caveat_info": caveat_info,
                             "vectors_info": vectors_info,
                             "aNGLE_info": aNGLE_info,
                             "texture_info": texture_info,
                             "wEBGL_draw_buffers_info": wEBGL_draw_buffers_info,
                             "shader_info": shader_info,
                            #  "canvas_info": canvas_info,
                            #  "canvas1_info": canvas1_info,
                            #  "canvas2_info": canvas2_info,
                            #  "canvas3_info": canvas3_info,
                            #  "canvas4_info": canvas4_info,
                            #  "canvas5_info": canvas5_info,
                            #  "webgl_info": webgl_info,
                         }}
        return response_data
    except:
        traceback.print_exc()
        return {"code": 1, "msg": "出错了！请检查BUG！"}



@app.route('/save_information', methods=['POST'])
def save_information():
    try:
        post_data_1 = request.json
        with open(os.path.join(SAVE_FINGERPRINT_DIR_1, f'{time.time()}.txt'), 'w', encoding='utf8') as po:
            po.write(json.dumps(post_data_1, ensure_ascii=False, indent=4, separators=(',', ':')) + '\n')
        return {"code": 0, "msg": "服务器已收到您的反馈信息！"}
    except:
        return {"code": 1, "msg": "出错了！请检查BUG！"}

@app.route("/chart.html")
def render_chart():
    return render_template("chart.html")



@app.route("/js1.html")
def js1_html():
    return render_template("js1.html")


@app.route("/js.html")
def js_html():
    seed = 131
    hash1 = 0
    m = request.headers
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    mdhms = time.strftime('%m%d%H%M%S', time.localtime(time.time()))
    fileDir = f'{BASE_DIR}/static/f{mdhms}.txt'
    fileDir1 = f'{BASE_DIR}/static/fingerprint/p{mdhms}.txt'
    fileDir2 = f'{BASE_DIR}/static/head/ua{mdhms}.txt'
    fileDir3 = f'{BASE_DIR}/static/head/ho{mdhms}.txt'
    fileDir4 = f'{BASE_DIR}/static/head/co{mdhms}.txt'
    fileDir5 = f'{BASE_DIR}/static/head/up{mdhms}.txt'
    fileDir6 = f'{BASE_DIR}/static/head/ac{mdhms}.txt'
    fileDir7 = f'{BASE_DIR}/static/head/ace{mdhms}.txt'
    fileDir8 = f'{BASE_DIR}/static/head/acl{mdhms}.txt'
    with open(fileDir, 'w') as f:
        f.write(dumps(dict(m), indent=4))
    with open(fileDir2, 'w') as m:
        m.write(request.headers.get("User-Agent"))
    with open(fileDir3, 'w') as q:
        q.write(request.headers.get("Host"))
    with open(fileDir4, 'w') as w:
        w.write(request.headers.get("Connection"))
    with open(fileDir5, 'w') as e:
        e.write(request.headers.get("Upgrade-Insecure-Requests"))
    with open(fileDir6, 'w') as r:
        r.write(request.headers.get("Accept"))
    with open(fileDir7, 'w') as t:
        t.write(request.headers.get("Accept-Encoding"))
    with open(fileDir8, 'w') as y:
        y.write(request.headers.get("Accept-Language"))
    name = f'f{mdhms}.txt'
    ss = f'ua{mdhms}.txt'
    qq = f'ho{mdhms}.txt'
    ww = f'co{mdhms}.txt'
    ee = f'up{mdhms}.txt'
    rr = f'ac{mdhms}.txt'
    tt = f'ace{mdhms}.txt'
    yy = f'acl{mdhms}.txt'
    host = request.headers.get("Host")
    host = host.encode('gbk')
    connection = request.headers.get("Connection")
    connection = connection.encode('gbk')
    re = request.headers.get("Upgrade-Insecure-Requests")
    re = re.encode('gbk')
    user = request.headers.get("User-Agent")
    user = user.encode('gbk')
    ac = request.headers.get("Accept")
    ac = ac.encode('gbk')
    ace = request.headers.get("Accept-Encoding")
    ace = ace.encode('gbk')
    acl = request.headers.get("Accept-Language")
    acl = acl.encode('gbk')
    miumiu = host + connection + re + user + ac + ace + acl
    for ch in miumiu:
        hash1 = hash1 * seed + ch
    mes = hash1 & 0x7FFFFFFF
    res = str(mes)
    flag = 0
    count = 0
    count1 = 0
    path = f"{BASE_DIR}/static/fingerprint"
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            position = path + '/' + file
            with open(position, "r") as k:
                count = count + 1
                data = k.read()
                if res == data:
                    count1 = count1 + 1
                    flag = 1
    with open(fileDir1, 'w') as f1:
        f1.write(str(res))
    return render_template("js.html", u=name, hash=res, m=flag, x=count, s=ss, q=qq, w=ww, e=ee, r=rr, t=tt, y=yy,
                           count=count1)


# canvas
@app.route("/canvas.html")
def canvas_html():
    return render_template("canvas.html")


# webgl
@app.route("/webglConstants.html")
def webglConstants_html():
    return render_template("webglConstants.html")


@app.route("/js3.html")
def js3_html():
    return render_template("js3.html")


@app.route("/js4.html")
def js4_html():
    return render_template("js4.html")


@app.route("/js5.html")
def js5_html():
    return render_template("js5.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/login.html")
def login_html():
    return render_template("login.html")


@app.route("/login", methods=['POST'])
def login():
    try:
        post_data = request.json
        post_data.update(dict(request.headers))
        del post_data['Referer']
        user = post_data.pop('User')
        post_data['Content-Length'] = str(int(post_data['Content-Length']) - 10 - len(user))
        s = json.dumps(post_data)
        sha256 = hashlib.sha256()
        sha256.update(s.encode('utf-8'))
        fp = sha256.hexdigest()
        sql = "select fingerprint as fp from t3 where User=?"
        select_data = db.execute(sql, (user,)).fetchall()
        if not select_data:
            return {"msg": "用户不存在！"}
        elif select_data[0]['fp'] == fp:
            return {"msg": "登录成功！"}
        else:
            return {"msg": "登录失败，请检查用户名是否正确"}
    except:
        traceback.print_exc()
        return {"code": 1, "msg": "出错了！请检查BUG！"}


@app.route('/')
def send():
    return render_template("js1.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=82)
