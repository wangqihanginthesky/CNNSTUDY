from urllib.parse import urlparse,parse_qs
from http.server import BaseHTTPRequestHandler,HTTPServer
from cgi import FieldStorage
with open("index.html",mode="r") as f:
    index=f.read()
with open("next.html",mode="r")as f:
    next=f.read()

routes=[]
def route(path,method):
    routes.append((path,method))
#add route setting
route("/","index")
route("/index","index")
route("/next","next")
route("/xml","xml")
class HelloServerhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global routes
        _url=urlparse(self.path)
        for r in routes:
            if (r[0]==_url.path):
                eval("self."+r[1]+"()")
                break
        else:
            self.error()
    #index action
    def index(self):
        #_url=urlparse(self.path)
        self.send_response(200)#responseを送信して開始する
        self.end_headers()#HEADER情報終了
        #self.wfile.write(b'sample web-server')#テキストを書く
        html=index.format(
            title="帮助你指定最优的学习计划，指导你报考最适合你的大学。",
            #link="/next?"+_url.query,
            message="同学，你是文科生还是理科生呢？"
        )
        self.wfile.write(html.encode("gbk"))
        return

    def next(self):
        #_url=urlparse(self.path)
        #query=parse_qs(_url.query)
        #id=query["id"][0]
        #password=query["pass"][0]
        #msg="id="+ id+',password='+password
        #print(query)
        self.send_response(200)  # responseを送信して開始する
        self.end_headers()  # HEADER情報終了
        html = next.format(
            message="header data.",
            data=self.headers
        )
        self.wfile.write(html.encode("gbk"))
        return
    #xml
    def xml(self):
        xml='''<?xml version="1.0" encoding="UTF-8"?>
        <data>
            <person>
                <name>Wang</name>
                <mail>wangqihanginthesky@gmail.com</mail>
                <age>27</age>
            </person>
            <message>Hello python!!</message>
        </data>'''
        self.send_response(200)
        self.send_header('Content-Type',\
                         'application/xml;charset=utf-8')
        self.end_headers()
        self.wfile.write(xml.encode("gbk"))
        return
    #error acction.
    def error(self):
        self.send_error(404,"CANNOT ACCESS!!")
        return
    #post
    def do_POST(self):
        form=FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD":"POST"})
        res=form["subject"].value
        #res=form["textfield"].value
        self.send_response(200)
        self.end_headers()
        html=next.format(
            message=res,
            data=form
        )
        self.wfile.write(html.encode("gbk"))
        return


server=HTTPServer(("",8000),HelloServerhandler)
server.serve_forever()