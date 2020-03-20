from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET"])
def index():
    data=["one","two","three"]
    person={"name":"taro","mail":"tarp@yamada"}
    return render_template('index.html',\
                        title="Form sample",\
                        message='sample.',\
                           data=data,\
                           person=person\
                           )
@app.route("/",methods=["POST"])

def form():
    ck=request.form.get("check")
    rd=request.form.get("ratio")
    sel=request.form.getlist("sel")
    #field=request.form["field"]
    return render_template("index.html",\
                           title="Form sample",\
                           message=[ck,rd,sel])


if __name__=='__main__':
    app.run(debug=True,port=500)#加上host的话，其他的地方的机器才能发request过来

