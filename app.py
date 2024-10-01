import os
from flask import Flask, request, render_template
from predict import predict_image_class  
from werkzeug.utils import secure_filename
from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3
from tips2 import scrape_quick_facts

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}
val = None
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
app.secret_key="123"
con=sqlite3.connect("database.db")
con.execute("create table if not exists customer(pid integer primary key,name text,address text,contact integer,mail text)")
con.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/go',methods=["GET","POST"])
def go():
    return render_template('upload.html')

#image proccess

@app.route('/customer',methods=["GET","POST"])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            n="No selected file"
            return render_template('upload.html',data=n)
        if file and allowed_file(file.filename):
            global filename
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            global val
            val= predict_image_class(filepath)
            #return f"name {val}"
            return render_template('upload.html',data=val)           
    return render_template('upload.html')

#get tips and medicine

@app.route('/tips', methods=['GET', 'POST'])
def tips():
    global val  
    hi=val

    if hi =='Apple Black rot':
        target_url = "https://extension.umn.edu/plant-diseases/cedar-apple-rust"
        m1="https://www.indiamart.com/proddetail/fungi-organic-fungicide-23064943791.html?pos=1&kwd=apple%20black%20rot%20fungicide&tags=A||||0|Price|product|pfSt|selam|TS|type=attr=1|attrS|br"
        mo1="https://extension.umn.edu/plant-diseases/cedar-apple-rust"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=mo1)
    
    elif hi== 'Apple_scab':
        target_url = "https://extension.umn.edu/plant-diseases/apple-scab"
        mo1="https://extension.umn.edu/plant-diseases/apple-scab"
        m1="https://dir.indiamart.com/search.mp?ss=apple+scab+fungicide&mcatid=4883&catid=12&src=as-popular%257Ckwd%253Dapple%2520scab%257Cpos%253D2%257Ccat%253D12%257Cmcat%253D4883%257Ckwd_len%253D10%257Ckwd_cnt%253D2%7C&prdsrc=1&stype=attr=1|attrS&res=RC3&com-cf=nl&qu=to&qry_typ=P"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=mo1)
    
    elif hi== 'Apple Cedar apple rust':
        target_url = "https://extension.umn.edu/plant-diseases/cedar-apple-rust"
        mo1 = "https://extension.umn.edu/plant-diseases/cedar-apple-rust"
        m1="https://www.indiamart.com/proddetail/sulphur-80-wdg-fungicide-2852058008130.html?pos=1&kwd=apple%20scab%20fungicide&tags=||||1292.7979|Price|product|pfSt|selam|TS|type=attr=1|attrS"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=mo1)
    
    elif hi== 'Apple healthy':
        target_url = "https://extension.umn.edu/fruit/growing-apples"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Blueberry healthy':
        target_url = "https://extension.umn.edu/fruit/growing-blueberries-home-garden"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Cherry healthy':
        target_url = "https://extension.umn.edu/plant-diseases/brown-rot-stone-fruit"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Cherry Powdery mildew':
        target_url = "https://extension.umn.edu/plant-diseases/powdery-mildew-trees-and-shrubs"
        m1="https://www.indiamart.com/proddetail/basf-acrisio-fungicide-2852928185230.html?pos=2&kwd=cherry%20powdery%20mildew%20fungicide&tags=A||||141.88246|Price|product|pfSt|selam|TS"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Corn Cercospora leaf spot Gray leaf spot':
        target_url = "https://extension.umn.edu/corn-pest-management/corn-ear-rots-and-mycotoxins"
        m1="https://www.indiamart.com/proddetail/bayer-nativo-fungicide-2852888121962.html?pos=1&kwd=corn%20circospora%20leaf%20spot%20gray%20leaf%20spotfungicide&tags=||||141.88246|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Corn Common rust ':
        target_url = "https://extension.umn.edu/corn-pest-management/corn-ear-rots-and-mycotoxins"
        m1="https://www.indiamart.com/proddetail/krilaxyl-fungicide-2850376276733.html?pos=2&kwd=corn%20common%20rust%20fungicide&tags=A||||1517.1705|Price|product|pfSt|selam|MDC"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Corn healthy':
        target_url = "https://extension.umn.edu/vegetables/growing-sweet-corn"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Corn Northern Leaf Blight':
        target_url = "https://extension.umn.edu/corn-pest-management/corn-ear-rots-and-mycotoxins"
        m1="https://www.indiamart.com/proddetail/roko-fungicide-powder-2853220848062.html?pos=2&kwd=corn%20northern%20leaf%20blight%20fungicide&tags=BA||||44.23123|Price|product|pfSt|selam|MDC|type=attr=1|attrS|br"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Grape Black rot':
        target_url = "https://extension.umn.edu/fruit/growing-grapes-home-garden"
        m1="https://www.indiamart.com/proddetail/multiplex-black-out-bactericide-2853467666648.html?pos=1&kwd=grape%20black%20rot%20fungicide&tags=A||||141.88246|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Grape Esca':
        target_url = "https://extension.umn.edu/fruit/growing-grapes-home-garden"
        m1="https://www.indiamart.com/proddetail/roko-fungicide-powder-2853220848062.html?pos=1&kwd=grape%20esca%20fungicide&tags=||||44.23123|Price|product|pfSt|selam|MDC|type=attr=1|attrS"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Grape healthy':
        target_url = "https://extension.umn.edu/fruit/growing-grapes-home-garden"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Grape Leaf blight':
        target_url = "https://extension.umn.edu/plant-diseases/leaf-spot-diseases-trees-and-shrubs"
        m1="https://www.indiamart.com/proddetail/power-plant-virosol-2851223659812.html?pos=4&kwd=grape%20leaf%20blight%20fungicide&tags=BA||||228.01602||product||selam|MDC|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Orange Haunglongbing':
        target_url = "https://extension.umn.edu/identify-invasive-species/orange-hawkweed"
        m1="https://www.indiamart.com/proddetail/antinematocide-sp-fungicides-24197640897.html?pos=5&kwd=orange%20haunglong%20fungicide&tags=BA||||917.8211|Price|product||selam|MDC|type=attr=1|attrS|attrMtch=1"
      
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Peach Bacterial spot':
        target_url = "https://extension.umn.edu/plant-diseases/leaf-spot-diseases-trees-and-shrubs"
        m1="https://www.indiamart.com/proddetail/organic-anti-bacterial-fertilizer-16671888962.html?pos=7&kwd=peach%20bacterial%20spot%20fungicide&tags=A||||1542.9468||product|pfSt|selam|TS"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Peach healthy':
        target_url = "https://extension.umn.edu/fruit/growing-stone-fruits-home-garden"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Pepper bell Bacterial spot':
        target_url = "https://extension.umn.edu/disease-management/bacterial-spot-tomato-and-pepper"
        m1="https://www.indiamart.com/proddetail/bacto-nill-crop-protectant-bactericide-16687809830.html?pos=7&kwd=pepper%20bell%20bacterial%20spot%20fungicide&tags=A||||808.72754|Price|product|pfSt|selam|TS"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Pepper bell healthy':
        target_url = "https://extension.umn.edu/vegetables/growing-peppers"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Potato Early blight':
        target_url = "https://extension.umn.edu/disease-management/early-blight-tomato-and-potato"
        m1="https://www.indiamart.com/proddetail/monceren-pencycuron-22-9-sc-1-ltr-2850887159555.html?pos=5&kwd=potato%20early%20blight%20fungicide&tags=A||||1883.668|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Potato healthy':
        target_url = "https://extension.umn.edu/vegetables/growing-potatoes"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Potato Late blight':
        target_url = "https://extension.umn.edu/disease-management/late-blight"
        m1="https://www.indiamart.com/proddetail/click-late-blight-downey-mildew-control-biofungicide-26733930933.html?pos=4&kwd=potato%20late%20blight%20fungicide&tags=||||640.0239|Price|product||selam|NA|type=attr=1|attrS"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Raspberry healthy':
        target_url = "https://extension.umn.edu/fruit/growing-raspberries-home-garden"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Soybean healthy':
        target_url = "https://extension.umn.edu/soybean-pest-management/soybean-cyst-nematode-management-guide"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Squash Powdery mildew':
        target_url = "https://extension.umn.edu/disease-management/downy-mildew-cucurbits"
        m1="https://www.indiamart.com/proddetail/fungicide-powder-2853267128373.html?pos=5&kwd=squash%20powder%20mildew%20fungicide&tags=A||||1292.7979|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Strawberry healthy':
        target_url = "https://extension.umn.edu/fruit/growing-strawberries-home-garden"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Strawberry Leaf scorch':
        target_url = "https://extension.umn.edu/strawberry-farming/strawberry-diseases-minnesota"
        m1="https://www.indiamart.com/proddetail/bio-fungicides-23085627288.html?pos=6&kwd=strawberry%20leaf%20scotch%20fungicide&tags=||||1006.8655|Price|product|pfSt|selam|TS|type=attr=1|attrS"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato Bacterial spot':
        target_url = "https://extension.umn.edu/disease-management/bacterial-canker-tomato"
        m1="https://www.indiamart.com/proddetail/anti-bacterial-anti-fungal-3255502330.html?pos=5&kwd=tomato%20bacterial%20spot%20fungicides&tags=A||||952.8169|Price|product||selam|MDC|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato Early blight':
        target_url = "https://extension.umn.edu/disease-management/early-blight-tomato-and-potato"
        m1="https://www.indiamart.com/proddetail/blightbuster-matelaxy-8-mancozeb-64-wp-2851614720633.html?pos=3&kwd=tomato%20early%20blight%20fungicides&tags=||||1688.8075|Price|product||selam|MDC"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato healthy':
        target_url = "https://extension.umn.edu/vegetables/growing-tomatoes"
        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,more=target_url)
    
    elif hi== 'Tomato Late blight':
        target_url = "https://extension.umn.edu/disease-management/late-blight"
        m1="https://www.indiamart.com/proddetail/sulphur-80-wdg-24658877791.html?pos=3&kwd=tomato%20late%20blight%20fungicides&tags=BB||||0|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato Leaf Mold':
        target_url = "https://extension.umn.edu/disease-management/tomato-leaf-mold"
        m1="https://www.indiamart.com/proddetail/bannari-leaf-guard-licheniformis-21450379130.html?pos=1&kwd=tomato%20leaf%20mold%20fungicides&tags=||||135.49039|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato Septoria leaf spot':
        target_url = "https://extension.umn.edu/plant-diseases/tomato-leaf-spot-diseases"
        m1="https://www.indiamart.com/proddetail/dise-nill-plant-growth-promoter-and-biofungicide-14971067048.html?pos=1&kwd=tomato%20septoria%20leaf%20spot%20fungicides&tags=||||44.541527||product|pfSt|selam|TS|type=attr=1|attrS"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=mo1,more=target_url)
    
    elif hi== 'Tomato Spider mites':
        target_url = "https://extension.umn.edu/yard-and-garden-insects/spider-mites"
        m1="https://www.indiamart.com/proddetail/daksh-systemic-organic-fungicides-24821699655.html?pos=1&kwd=tomato%20spider%20mites%20fungicides&tags=||||141.88246|Price|product||selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
        
    elif hi== 'Tomato Target Spot':
        target_url = "https://extension.umn.edu/disease-management/early-blight-tomato-and-potato"
        m1="https://www.indiamart.com/proddetail/bayer-antracol-fungicide-23376359862.html?pos=4&kwd=tomato%20target%20spot%20fungicides&tags=BA||||141.88246||product||selam|MDC|type=attr=1|attrS"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato mosaic virus':
        target_url = "https://extension.umn.edu/disease-management/tomato-viruses"
        m1="https://www.indiamart.com/proddetail/plant-virus-controller-21809276648.html?pos=2&kwd=tomato%20mosaic%20virus%20fungicides&tags=A||||1265.247|Price|product|pfSt|selam|TS|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== 'Tomato Yellow Leaf Curl Virus':
        target_url = "https://extension.umn.edu/plant-diseases/viruses-backyard-fruit"
        m1="https://www.indiamart.com/proddetail/metarhizium-anisopliae-pesticides-23885192448.html?pos=3&kwd=tomato%20yellow%20leaf%20curl%20virus%20fungicides&tags=A||||1089.0875|Price|product|pfSt|selam|SSnp|type=attr=1|attrS|attrMtch=1"

        hi=scrape_quick_facts(target_url)
        return render_template('tip.html',hello=hi,name=val,image=filename,medi=m1,more=target_url)
    
    elif hi== '':
        return render_template('no.html') 
    else:
        return render_template('no.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')
    
#admin login

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=='POST':
        name=request.form['user']
        password=request.form['pass']
        con=sqlite3.connect("database.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from customer where name=? and mail=?",(name,password))
        data=cur.fetchone()

        if data:
            
            
            return render_template('adup.html')
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render_template('admin.html', error_message=error_message)
    return redirect(url_for("admin"))

#admin upload

UPLOAD_FOLDER1 = 'admin'
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1
def get_uploaded_file():
    files = os.listdir(app.config['UPLOAD_FOLDER1'])
    if files:
        return files[0]
    else:
        return None
@app.route('/success', methods=['POST'])
def about1():
    return render_template('adup.html')

@app.route('/back2', methods=['POST'])
def about2():
    return render_template('upload2.html')

@app.route('/up', methods=['POST'])
def upload_form1():
    existing_file = get_uploaded_file()
    return render_template('upload2.html', existing_file=existing_file)

@app.route('/upload2', methods=['POST'])
def upload_file():
    existing_file = get_uploaded_file()
    if existing_file:
        return "You already have a file uploaded."
    else:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Save the file to the upload folder
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER1'], uploaded_file.filename))
    return render_template('success.html')

@app.route('/remove', methods=['POST'])
def remove_file():
    existing_file = get_uploaded_file()
    if existing_file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER1'], existing_file)
        if os.path.exists(file_path):
            os.remove(file_path)
    return render_template('removed.html')

#main
if __name__ == '__main__':
    app.run(debug=True)
