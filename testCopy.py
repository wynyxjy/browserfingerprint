# coding=utf-8
import datetime
import json
import sys
import time
import os.path
import traceback
import hashlib
from json import dumps
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from dict_to_db import DictToDb
from fastapi.responses import FileResponse
from user_agents import parse

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
db = DictToDb(os.path.join(BASE_DIR, "DATA.db"), check_same_thread=False)
SAVE_FINGERPRINT_DIR = os.path.join(os.path.join(BASE_DIR, 'static'), 'save_fingerprint')
SAVE_FINGERPRINT_DIR_1 = os.path.join(os.path.join(BASE_DIR, 'static'), 'save_information')
if not os.path.exists(SAVE_FINGERPRINT_DIR):
    os.makedirs(SAVE_FINGERPRINT_DIR)
if not os.path.exists(SAVE_FINGERPRINT_DIR_1):
    os.makedirs(SAVE_FINGERPRINT_DIR_1)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# 配置 Jinja2 模板引擎
templates = Jinja2Templates(directory="templates")

class FingerprintData(BaseModel):
    User: str
    Content_Length: int
    Referer: str
    fingerprint: str

def get_total_count(search_time=None):
    if search_time:
        sql = "select count() as total_count from t2 where insert_time>?;"
        return db.execute(sql, (search_time,)).fetchone()['total_count']
    else:
        return db.execute('select count() as total_count from t2;').fetchone()['total_count']


def compute_browser_language(total_count, search_time):
    sql = "SELECT COUNT(BrowserLanguage) AS count, BrowserLanguage AS name " \
          "FROM t2 WHERE insert_time > ? GROUP BY BrowserLanguage"
    select_data = db.execute(sql, (search_time,)).fetchall()
    result_data = {"其它": 0}
    for data in select_data:
        scale = data['count'] / total_count
        if scale < 0.05:
            result_data['其它'] += scale
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



@app.post('/save_fingerprint')
async def save_fingerprint(request: Request):
    try:
        post_data = await request.json()
        post_data.update(dict(request.headers))
        post_data.pop('Referer', None)
        # del post_data['Referer']
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
        return JSONResponse(content={"code": 0, "msg": "服务器已收到您的指纹信息！"})
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"code": 1, "msg": "出错了！请检查Bug！"})



# 新的后端接口，存储JS生成的指纹
# 失败版本
# @app.post('/save_fingerprint')
# async def save_fingerprint(request: Request):
#     try:
#         post_data = await request.json()
#         visitor_id = post_data.get('fingerprint')  # 从前端获取 visitorId

#         # 防止空值
#         if not visitor_id:
#             return JSONResponse(content={"code": 1, "msg": "指纹数据已存储！"})

#         now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # 插入数据库 t2 表
#         sql = "INSERT INTO t2 (fingerprint, insert_time) VALUES (?, ?)"
#         db.execute(sql, (visitor_id, now))
#         db.commit()

#         # 可选：保存到文件作为备份
#         with open(os.path.join(SAVE_FINGERPRINT_DIR, f'{time.time()}.txt'), 'w', encoding='utf8') as f:
#             f.write("浏览器指纹:\n")
#             f.write(visitor_id + "\n")

#         return JSONResponse(content={"code": 0, "msg": "指纹数据已存储！"})
#     except Exception as e:
#         traceback.print_exc()
#         return JSONResponse(content={"code": 1, "msg": "服务器出错，请联系管理员！"})



# @app.get('/compute_data')
# async def compute_data(request: Request):
#     try:
#         start_time = request.query_params.get("start_time")
#         dt = datetime.datetime.now()
#         if start_time == "today":
#             search_time = dt - datetime.timedelta(days=0, seconds=dt.second, microseconds=dt.microsecond,
#                                                   milliseconds=0,
#                                                   minutes=dt.minute, hours=dt.hour, weeks=0)
#         elif start_time == "three_day":
#             search_time = dt - datetime.timedelta(days=3, seconds=dt.second, microseconds=dt.microsecond,
#                                                   milliseconds=0,
#                                                   minutes=dt.minute, hours=dt.hour, weeks=0)
#         elif start_time == "week":
#             search_time = dt - datetime.timedelta(days=7, seconds=dt.second, microseconds=dt.microsecond,
#                                                   milliseconds=0,
#                                                   minutes=dt.minute, hours=dt.hour, weeks=0)
#         else:
#             search_time = datetime.datetime(year=1970, month=1, day=1)
#         search_count = get_total_count(search_time)
#         total_count = get_total_count()
#         browser_language_info = compute_browser_language(search_count, search_time)
#         system_info = compute_system(search_count, search_time)
#         browser_info = compute_browser(search_count, search_time)
#         timezone_info = compute_timezone(search_count)
#         vendor_info = compute_vendor(search_count, search_time)
#         renderer_info = compute_renderer(search_count, search_time)
#         version_info = compute_version(search_count, search_time)
#         sHADING_LANGUAGE_VERSION_info = compute_SHADING_LANGUAGE_VERSION(search_count, search_time)
#         Vendor_info = compute_Vendor(search_count, search_time)
#         Renderer_info = compute_Renderer(search_count, search_time)
#         bool_2_string_info = compute_bool_2_string(search_count, search_time)
#         angle_info = compute_angle(search_count, search_time)
#         caveat_info = compute_caveat(search_count, search_time)
#         vectors_info = compute_vectors(search_count, search_time)
#         aNGLE_info = compute_ANGLE(search_count, search_time)
#         texture_info = compute_texture(search_count, search_time)
#         wEBGL_draw_buffers_info = compute_WEBGL_draw_buffers(search_count, search_time)
#         shader_info = compute_shader(search_count, search_time)

#         response_data = {"code": 0, "msg": "success", "total_count": total_count,
#                          "search_count": search_count,
#                          "data": {
#                              "browser_language_info": browser_language_info,
#                              "system_info": system_info,
#                              "browser_info": browser_info,
#                              "timezone_info": timezone_info,
#                              "vendor_info": vendor_info,
#                              "renderer_info": renderer_info,
#                              "version_info": version_info,
#                              "sHADING_LANGUAGE_VERSION_info": sHADING_LANGUAGE_VERSION_info,
#                              "Vendor_info": Vendor_info,
#                              "Renderer_info": Renderer_info,
#                              "bool_2_string_info": bool_2_string_info,
#                              "angle_info": angle_info,
#                              "caveat_info": caveat_info,
#                              "vectors_info": vectors_info,
#                              "aNGLE_info": aNGLE_info,
#                              "texture_info": texture_info,
#                              "wEBGL_draw_buffers_info": wEBGL_draw_buffers_info,
#                              "shader_info": shader_info,
#                          }}
#         return JSONResponse(content=response_data)
#     except Exception as e:
#         traceback.print_exc()
#         return JSONResponse(content={"code": 1, "msg": "出错了！请检查BUG！"})

@app.get('/compute_data')
async def compute_data(request: Request):
    try:
        # dt = datetime.datetime.now()
        # today_str = dt.strftime("%Y-%m-%d")

        # # 检查是否已有今天的数据
        # sql_check = "SELECT COUNT(*) as count FROM t2 WHERE insert_time >= ?"
        # count = db.execute(sql_check, (today_str,)).fetchone()["count"]

        # # 如果没有今天的数据，就插入
        # if count == 0:
        #     insert_dummy_data(request)  # 传入 request 以获取 User-Agent
            
        

        # # 继续执行原来的数据统计逻辑
        # start_time = request.query_params.get("start_time")
        # if start_time == "today":
        #     search_time = dt - datetime.timedelta(days=0, seconds=dt.second, microseconds=dt.microsecond,
        #                                           milliseconds=0, minutes=dt.minute, hours=dt.hour, weeks=0)
        # elif start_time == "three_day":
        #     search_time = dt - datetime.timedelta(days=3, seconds=dt.second, microseconds=dt.microsecond,
        #                                           milliseconds=0, minutes=dt.minute, hours=dt.hour, weeks=0)
        # elif start_time == "week":
        #     search_time = dt - datetime.timedelta(days=7, seconds=dt.second, microseconds=dt.microsecond,
        #                                           milliseconds=0, minutes=dt.minute, hours=dt.hour, weeks=0)
        # else:
        #     search_time = datetime.datetime(year=1970, month=1, day=1)
        dt = datetime.datetime.now()

        # 每次访问都记录一次指纹（包含浏览器信息）
        insert_dummy_data(request)  # 每次都执行，动态记录

        # 获取时间范围
        start_time = request.query_params.get("start_time")
        if start_time == "today":
            search_time = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        elif start_time == "three_day":
            search_time = dt - datetime.timedelta(days=3)
        elif start_time == "week":
            search_time = dt - datetime.timedelta(days=7)
        else:
            search_time = datetime.datetime(year=1970, month=1, day=1)

        # Continue with the data processing as usual
        search_count = get_total_count(search_time)
        total_count = get_total_count()
        browser_language_info = compute_browser_language(search_count, search_time)
        system_info = compute_system(search_count, search_time)
        browser_info = compute_browser(search_count, search_time)
        timezone_info = compute_timezone(search_count)
        vendor_info = compute_vendor(search_count, search_time)
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
                         }}
        return JSONResponse(content=response_data)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"code": 1, "msg": "出错了！请检查BUG！"})


@app.post('/save_information')
async def save_information(request: Request):
    try:
        post_data_1 = await request.json()
        with open(os.path.join(SAVE_FINGERPRINT_DIR_1, f'{time.time()}.txt'), 'w', encoding='utf8') as po:
            po.write(json.dumps(post_data_1, ensure_ascii=False, indent=4, separators=(',', ':')) + '\n')
        return JSONResponse(content={"code": 0, "msg": "服务器已收到您的反馈信息！"})
    except Exception as e:
        return JSONResponse(content={"code": 1, "msg": "出错了！请检查BUG！"})

@app.get("/chart.html")
async def render_chart():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/chart.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")

@app.get("/js1.html")
async def js1_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/js1.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")



@app.get("/js.html", response_class=HTMLResponse)
async def js_html(request: Request):
    seed = 131
    hash1 = 0
    m = request.headers
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    mdhms = time.strftime('%m%d%H%M%S', time.localtime(time.time()))
    
    # 文件路径
    fileDir = f'{BASE_DIR}/static/f{mdhms}.txt'
    fileDir1 = f'{BASE_DIR}/static/fingerprint/p{mdhms}.txt'
    fileDir2 = f'{BASE_DIR}/static/head/ua{mdhms}.txt'
    fileDir3 = f'{BASE_DIR}/static/head/ho{mdhms}.txt'
    fileDir4 = f'{BASE_DIR}/static/head/co{mdhms}.txt'
    fileDir5 = f'{BASE_DIR}/static/head/up{mdhms}.txt'
    fileDir6 = f'{BASE_DIR}/static/head/ac{mdhms}.txt'
    fileDir7 = f'{BASE_DIR}/static/head/ace{mdhms}.txt'
    fileDir8 = f'{BASE_DIR}/static/head/acl{mdhms}.txt'

    # 写入请求头信息到文件
    with open(fileDir, 'w', encoding='utf8') as f:
        f.write(json.dumps(dict(m), indent=4))
    with open(fileDir2, 'w', encoding='utf8') as m:
        m.write(request.headers.get("User-Agent"))
    with open(fileDir3, 'w', encoding='utf8') as q:
        q.write(request.headers.get("Host"))
    with open(fileDir4, 'w', encoding='utf8') as w:
        w.write(request.headers.get("Connection"))
    with open(fileDir5, 'w', encoding='utf8') as e:
        e.write(request.headers.get("Upgrade-Insecure-Requests"))
    with open(fileDir6, 'w', encoding='utf8') as r:
        r.write(request.headers.get("Accept"))
    with open(fileDir7, 'w', encoding='utf8') as t:
        t.write(request.headers.get("Accept-Encoding"))
    with open(fileDir8, 'w', encoding='utf8') as y:
        y.write(request.headers.get("Accept-Language"))

    # 文件名
    name = f'f{mdhms}.txt'
    ss = f'ua{mdhms}.txt'
    qq = f'ho{mdhms}.txt'
    ww = f'co{mdhms}.txt'
    ee = f'up{mdhms}.txt'
    rr = f'ac{mdhms}.txt'
    tt = f'ace{mdhms}.txt'
    yy = f'acl{mdhms}.txt'

    # 计算哈希值
    host = request.headers.get("Host").encode('gbk')
    connection = request.headers.get("Connection").encode('gbk')
    re = request.headers.get("Upgrade-Insecure-Requests").encode('gbk')
    user = request.headers.get("User-Agent").encode('gbk')
    ac = request.headers.get("Accept").encode('gbk')
    ace = request.headers.get("Accept-Encoding").encode('gbk')
    acl = request.headers.get("Accept-Language").encode('gbk')
    miumiu = host + connection + re + user + ac + ace + acl
    for ch in miumiu:
        hash1 = hash1 * seed + ch
    mes = hash1 & 0x7FFFFFFF
    res = str(mes)

    # 匹配逻辑
    flag = 0
    count = 0
    count1 = 0
    path = f"{BASE_DIR}/static/fingerprint"
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(os.path.join(path, file)):
            position = os.path.join(path, file)
            with open(position, "r", encoding='utf8') as k:
                count += 1
                data = k.read()
                if res == data:
                    count1 += 1
                    flag = 1

    # 写入哈希值到文件
    with open(fileDir1, 'w', encoding='utf8') as f1:
        f1.write(str(res))

    # 渲染模板并返回
    return templates.TemplateResponse(
        "js.html",
        {
            "request": request,
            "u": name,
            "hash": res,
            "m": flag,
            "x": count,
            "s": ss,
            "q": qq,
            "w": ww,
            "e": ee,
            "r": rr,
            "t": tt,
            "y": yy,
            "count": count1
        }
    )


@app.get("/canvas.html")
async def canvas_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/canvas.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")

@app.get("/webglConstants.html")
async def webglConstants_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/webglConstants.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")

@app.get("/js3.html")
async def js3_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/js3.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")


@app.get("/js4.html")
async def js4_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/js4.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")


@app.get("/js5.html")
async def js5_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/js5.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")

@app.get("/favicon.ico")
async def favicon():
    try:
        favicon_path = os.path.join(BASE_DIR, 'templates', 'favicon.ico')
        return FileResponse(favicon_path, media_type='image/vnd.microsoft.icon')
    except Exception as e:
        return JSONResponse(content={"code": 1, "msg": f"Error: {str(e)}"})

@app.get("/login.html")
async def login_html():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/login.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")


@app.post("/login")
async def login(request: Request):
    try:
        post_data = await request.json()
        post_data.update(dict(request.headers))

        if 'Referer' in post_data:
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
            return JSONResponse(content={"msg": "用户不存在！"})
        elif select_data[0]['fp'] == fp:
            return JSONResponse(content={"msg": "登录成功！"})
        else:
            return JSONResponse(content={"msg": "登录失败，请检查用户名是否正确"})
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(content={"code": 1, "msg": f"出错了！请检查BUG！"})


@app.get('/')
async def send():
    try:
        # 使用 UTF-8 编码读取文件
        with open('templates/js1.html', 'r', encoding='utf-8') as f:
            content = f.read()
        return HTMLResponse(content=content)
    except Exception as e:
        return HTMLResponse(content=f"Error: {str(e)}")


#使数据库动态更新
# def insert_dummy_data():
#     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     sql = "INSERT INTO t2 (BrowserLanguage, system, browser, simpleTimeZone, insert_time) VALUES (?, ?, ?, ?, ?)"
#     db.execute(sql, ('zh-CN', 'Windows', 'Chrome', 'UTC+8', now))
#     db.commit()

def insert_dummy_data(request: Request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 从 HTTP 头部获取 User-Agent
    user_agent = request.headers.get("User-Agent", "Unknown")
    parsed_ua = parse(user_agent)  # 解析 User-Agent

    browser_name = parsed_ua.browser.family or "Unknown"
    os_name = parsed_ua.os.family or "Unknown"

    sql = "INSERT INTO t2 (BrowserLanguage, system, browser, simpleTimeZone, insert_time) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, ('zh-CN', os_name, browser_name, 'UTC+8', now))
    db.commit()
# # 插入测试数据
# insert_dummy_data()
# def insert_dummy_data(request: Request):
#     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # 从 HTTP 头部获取 User-Agent
#     user_agent = request.headers.get("User-Agent", "Unknown")
#     parsed_ua = parse(user_agent)  # 解析 User-Agent

#     browser_name = parsed_ua.browser.family or "Unknown"
#     os_name = parsed_ua.os.family or "Unknown"

#     sql = "INSERT INTO t2 (BrowserLanguage, system, browser, simpleTimeZone, insert_time) VALUES (?, ?, ?, ?, ?)"
#     db.execute(sql, ('zh-CN', os_name, browser_name, 'UTC+8', now))
#     db.commit()



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=81)
