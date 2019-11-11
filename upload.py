# coding:utf-8
 
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
 
app = Flask(__name__)
 
@app.route('/', methods=['POST', 'GET'])
def upload():
  if request.method == 'POST':
    f = request.files['file']
    basepath = os.path.dirname(__file__) # 當前檔案所在路徑
    upload_path = os.path.join(basepath,'uploads',secure_filename(f.filename)) #注意：沒有的資料夾一定要先建立，不然會提示沒有該路徑 預設路徑是根目錄下加個叫做的uploads資料夾。這邊請自行更改想要的名稱
    f.save(upload_path)
    return redirect(url_for('upload'))
  return render_template('upload.html')
 
if __name__ == '__main__':
  app.run()