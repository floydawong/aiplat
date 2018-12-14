#-*- coding: UTF-8 -*-
import sys
sys.path.append('..')
import apiutil
import json

app_key = 'xxx'
app_id = 'xxx'

if __name__ == '__main__':
    with open('../data/face.png', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getFaceDetectmultiface(image_data)

    if rsp['ret'] == 0:
        for i in rsp['data']['face_list']:
            print 'x1:', i['x1']
            print 'y1:', i['y1']
            print 'x2:', i['x2']
            print 'y2:', i['y2']
            print
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(
            rsp,
            encoding="UTF-8",
            ensure_ascii=False,
            sort_keys=False,
            indent=4)
        print '----------------------API FAIL----------------------'
