# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
import urllib
import urllib2
import cookielib
import hashlib
import re
import json
import sys
import time
from sinastorage.bucket import SCSBucket
import sinastorage
import random
import name

app = Flask(__name__)

cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

@app.route('/html',methods=['GET'])
def html_form():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url=s.make_url_authed('picture/bj1.gif')
    whuurl=s.make_url_authed('picture/whu.jpg')
    return render_template('html_form.html',url=url,url1=whuurl)

@app.route('/html',methods=['POST'])
def html():
    url=request.form['url']
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={"User-Agent":user_Agent}
    req=urllib2.Request(url,headers=headers)
    try:
        response=urllib2.urlopen(req)
    except urllib2.URLError as e:
        result=u'该网站访问受限(⊙o⊙)哦，还是去PC端查看源代码吧！'
        return render_template('html.html',result=result)
    content=response.read()
    try:
        result=content.decode('utf-8')
    except UnicodeDecodeError as e:
        try:
            result=content.decode('gb2312')
        except UnicodeDecodeError as e:
            try:
                result=content.decode('gbk')
            except UnicodeDecodeError as e:
                result=u'不好意思哇，水平有限，解码失败咯'
    return render_template('html.html',result=result)

@app.route('/', methods=['GET', 'POST'])
def home():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    bkdurl=s.make_url_authed('picture/P50714-095115.jpg')
    whuurl=s.make_url_authed('picture/whu.jpg')
    phoneurl=s.make_url_authed('picture/phone.png')
    blogurl=s.make_url_authed('picture/blog.png')
    return render_template('hello.html',url1=bkdurl,url2=whuurl,url3=phoneurl,url4=blogurl)

@app.route('/phone', methods=['GET'])
def phone():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    bkdurl=s.make_url_authed('picture/P50714-095115.jpg')
    whuurl=s.make_url_authed('picture/whu.jpg')
    pcurl=s.make_url_authed('picture/computer.png')
    blogurl=s.make_url_authed('picture/blog.png')
    return render_template('phone.html',url1=bkdurl,url2=whuurl,url3=pcurl,url4=blogurl)

@app.route('/home', methods=['GET'])
def hello():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    pcurl=s.make_url_authed('picture/computer.png')
    phoneurl=s.make_url_authed('picture/phone.png')
    blogurl=s.make_url_authed('picture/blog.png')
    whuurl=s.make_url_authed('picture/whu.jpg')
    cycleurl=s.make_url_authed('picture/cycle.JPG')
    return render_template('home.html',url1=pcurl,url2=phoneurl,url3=blogurl,url4=whuurl,url5=cycleurl)

@app.route('/blog',methods=['GET'])
def blog():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    url1=s.make_url_authed('picture/beijing.jpg')
    url2=s.make_url_authed('picture/ziti.png')
    return render_template('blog.html',url0=url1,url1=url2)

@app.route('/qingzangxian',methods=['GET'])
def chuan():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url=s.make_url_authed('picture/bj1.gif')
    url0=s.make_url_authed('picture/q3.JPG')
    url1=s.make_url_authed('picture/q4.JPG')
    url2=s.make_url_authed('picture/q7.jpg')
    url3=s.make_url_authed('picture/q2.jpg')
    url4=s.make_url_authed('picture/q1.jpg')
    url5=s.make_url_authed('picture/q8.jpg')
    url6=s.make_url_authed('picture/q5.JPG')
    url7=s.make_url_authed('picture/q0.jpg')
    url8=s.make_url_authed('picture/q6.jpg')
    url9=s.make_url_authed('picture/whu.jpg')
    return render_template('cycle.html',url=url,url0=url0, url1=url1, url2=url2, url3=url3, url4=url4, url5=url5, url6=url6, url7=url7, url8=url8, whuurl=url9,)

@app.route('/chuanzangxian',methods=['GET'])
def qing():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url=s.make_url_authed('picture/bj1.gif')
    url0=s.make_url_authed('picture/c4.jpg')
    url1=s.make_url_authed('picture/c5.jpg')
    url2=s.make_url_authed('picture/c6.jpg')
    url3=s.make_url_authed('picture/c8.jpg')
    url4=s.make_url_authed('picture/c0.jpg')
    url5=s.make_url_authed('picture/c1.jpg')
    url6=s.make_url_authed('picture/c7.jpg')
    url7=s.make_url_authed('picture/c2.jpg')
    url8=s.make_url_authed('picture/c3.jpg')
    url9=s.make_url_authed('picture/whu.jpg')
    return render_template('cycle.html',url=url,url0=url0, url1=url1, url2=url2, url3=url3, url4=url4, url5=url5, url6=url6, url7=url7, url8=url8, whuurl=url9,)

@app.route('/diary',methods=['GET'])
def diary():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    url0=s.make_url_authed('picture/beijing.jpg')
    return render_template('diary.html',url0=url0)
@app.route('/diary/chuanzangxian',methods=['GET'])
def czx():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url0=s.make_url_authed('picture/bj1.gif')
    url1=s.make_url_authed('picture/cz1.jpg')
    url11=s.make_url_authed('picture/czx.JPG')
    url12=s.make_url_authed('picture/cz0.jpg')
    url2=s.make_url_authed('picture/cz22.jpg')
    url21=s.make_url_authed('picture/cz21.jpg')
    url22=s.make_url_authed('picture/cz23.jpg')
    url31=s.make_url_authed('picture/c0.jpg')
    url32=s.make_url_authed('picture/cz31.jpg')
    url33=s.make_url_authed('picture/cz32.jpg')
    url34=s.make_url_authed('picture/cz33.jpg')
    url35=s.make_url_authed('picture/cz34.jpg')
    url36=s.make_url_authed('picture/cz35.jpg')
    url41=s.make_url_authed('picture/cz41.jpg')
    url42=s.make_url_authed('picture/cz42.jpg')
    url43=s.make_url_authed('picture/cz43.jpg')
    url44=s.make_url_authed('picture/cz44.jpg')
    url45=s.make_url_authed('picture/cz45.jpg')
    url46=s.make_url_authed('picture/cz46.jpg')
    url51=s.make_url_authed('picture/cz51.jpg')
    url52=s.make_url_authed('picture/cz52.jpg')
    url53=s.make_url_authed('picture/cz53.jpg')
    url54=s.make_url_authed('picture/cz54.jpg')
    url55=s.make_url_authed('picture/cz55.jpg')
    url56=s.make_url_authed('picture/cz56.jpg')
    url61=s.make_url_authed('picture/cz61.jpg')
    url62=s.make_url_authed('picture/cz62.jpg')
    url63=s.make_url_authed('picture/cz63.jpg')
    return render_template('diary_czx.html',url0=url0,url1=url1,url11=url11,url12=url12,url2=url2,url21=url21,url22=url22,
                           url31=url31,url32=url32,url33=url33,url34=url34,url35=url35,url36=url36,url41=url41,url42=url42,
                           url43=url43,url44=url44,url45=url45,url46=url46,url51=url51,url52=url52,url53=url53,url54=url54,
                           url55=url55,url56=url56,url61=url61,url62=url62,url63=url63)


@app.route('/diary/qingzangxian',methods=['GET'])
def qzx():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url0=s.make_url_authed('picture/bj1.gif')
    return render_template('diary_qzx.html',url0=url0)

@app.route('/python',methods=['GET'])
def qzx():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    url0=s.make_url_authed('picture/bj1.gif')
    return render_template('diary_qzx.html',url0=url0)

@app.route('/blog/register',methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/blog/register',methods=['POST'])
def register():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    username=request.form['username']
    try:
        response=s[r'password/'+username+'.txt']
    except BaseException, e:
        password=request.form['password']
        password1=request.form['password1']
        if password==password1:
            password=password+username+'Sundae'
            md5=hashlib.md5()
            md5.update(password.encode('utf-8'))
            pwd=md5.hexdigest()
            s.put(r'password/'+username+'.txt',pwd)
            return '<h3>注册成功，感谢您的支持！</h3>'
        else:
            return '''
            <h3>请输入相同密码！</h3>
            <p><button onclick="javascript:window.location.href='http://sundae.applinzi.com/blog/register';">点击返回</button></p>
            '''
    return '''
    <h3>用户名已存在！</h3>
    <p><button onclick="javascript:window.location.href='http://sundae.applinzi.com/blog/register';">点击返回</button></p>
    '''
@app.route('/blog/signin',methods=['GET'])
def blog_signin_form():
    return render_template('blog_signin.html')

@app.route('/blog/signin',methods=['POST'])
def blog_signin():
    username=request.form['username']
    password=request.form['password']+username+'Sundae'
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    pwd=md5.hexdigest()
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    try:
        response=s[r'password/'+username+'.txt']
    except BaseException, e:
        return   '''
        <h3>用户名不存在！</h3>
        <p><button onclick="javascript:window.location.href='http://sundae.applinzi.com/blog/signin';">点击返回</button></p>
        '''
    content=response.read()
    if pwd==content:
        return '<h3>登录成功！</h3>'
    else:
        return '''
        <h3>密码错误！</h3>
        <p><button onclick="javascript:window.location.href='http://sundae.applinzi.com/blog/signin';">点击返回</button></p>
        '''
    
    

@app.route('/signin', methods=['GET'])
def signin_form():
    global opener,cookie,handler
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('eggtart')
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={"User-Agent":user_Agent}
    url0='http://210.42.121.132/servlet/GenImg'
    cookie = cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    req0=urllib2.Request(url0,headers=headers)
    response = opener.open(req0)
    s.put('picture/123.jpg',response.read())
    url=s.make_url_authed('picture/123.jpg')
    return render_template('signin_test.html',pic=url)

@app.route('/signin', methods=['POST'])
def signin():
    global cookie,opener
    student=request.form['username']
    password=request.form['password']
    picture=request.form['picture']
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    key=md5.hexdigest()
    reload(sys)
    sys.setdefaultencoding("utf8")
    url='http://210.42.121.132/servlet/Login'
    user_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
    headers={"User-Agent":user_Agent}
    req=urllib2.Request(url,headers=headers)
    data=urllib.urlencode({'id':student,'pwd':key,'xdvfb':picture})
    response=opener.open(req,data)
    content=response.read().decode('gb2312')
    images=re.findall(r'<font color="red" style="font-size: 12px;">(.*?)<label id="alertp">',content,re.S)
    if images==[u'验证码错误']:
        return render_template('result.html',result=u'验证码错误噢 (⊙o⊙)\n')
    elif images==[u'用户名/密码错误']:
        return render_template('result.html',result=u'\n用户名或密码错误噢 (⊙o⊙)\n')
    else:	
        items=re.findall(r'<div id="login_info2"><span id="term">(.*?)<span id="showOrHide">',content,re.S)
        if items==[u' 2016-2017学年上学期 ']:
            csrftokens=re.findall(r'valu.*?action=queryStuLsn&(.*?)></input>',content,re.S)
            csrf=csrftokens[0]
            now=time.strftime('%H:%M:%S')
            week=time.strftime('%a')
            month=time.strftime('%b')
            date=time.strftime('%d')
            year=time.strftime('%Y')
            score=opener.open('http://210.42.121.132/servlet/Svlt_QueryStuScore?'+csrf+'&year=0&term=&learnType=&scoreFlag=0&t='+week+'%20'+month+'%20'+date+'%20'+year+'%20'+now+'%20GMT+0800').read().decode('gb2312')
            reports=re.findall(r'<tr null>.*?<td>.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',score,re.S)
            words=''
            for report in reports:
                if report[8]!='':
                    words=words+u'课程：'+'  '+report[0]+'\n'+u'种类：'+report[1]+'    '+u'学分：'+report[2]+'    '+u'成绩：'+report[8]+'\n\n'
            return render_template('result.html',result=words)

@app.route('/who',methods=['POST','GET'])
def who():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    url1=s.make_url_authed('picture/who.png')
    url0=s.make_url_authed('picture/bj1.gif')
    url2=s.make_url_authed('picture/i.png')
    return render_template('who.html',url0=url0,url1=url1,url2=url2)

@app.route('/happy',methods=['GET'])
def happy():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    e=SCSBucket('eggtart')
    url1=s.make_url_authed('picture/bj2.gif')
    url2=s.make_url_authed('picture/bianpao.gif')
    url3=s.make_url_authed('picture/dui0.gif')
    url4=s.make_url_authed('picture/door.gif')
    url5=s.make_url_authed('picture/deng.gif')
    url6=s.make_url_authed('picture/ji.gif')
    url7=s.make_url_authed('picture/ren.gif')
    url8=s.make_url_authed('picture/tu.gif')
    url9=s.make_url_authed('picture/yuan.gif')
    url10=s.make_url_authed('picture/cai.gif')
    url11=s.make_url_authed('picture/fa.gif')
    url12=s.make_url_authed('picture/zong.gif')
    url13=s.make_url_authed('picture/lazha.png')
    whuurl=e.make_url_authed('picture/whu.jpg')
    return render_template('happy.html',url1=url1,url2=url2,url3=url3,url4=url4,url5=url5,url6=url6,
                           url7=url7,url8=url8,url9=url9,url10=url10,url11=url11,url12=url12,url13=url13,whuurl=whuurl)

@app.route('/newyear',methods=['POST'])
def year():
    sinastorage.setDefaultAppInfo('***********************', '*************************************')
    s=SCSBucket('sundae')
    password=request.form['password']
    url0=s.make_url_authed('picture/bj1.gif')
    url1=s.make_url_authed('picture/boom.jpg')
    url2=s.make_url_authed('picture/tree.jpg')
    url3=s.make_url_authed('picture/snow.jpg')
    url4=s.make_url_authed('picture/we.jpg')
    url5=s.make_url_authed('picture/me.png')
    url7=s.make_url_authed('picture/001.png')
    if password==u'王璐琰':
        c=SCSBucket('brokenmist')
        url10=c.make_url_authed('picture/bj1.gif')
        url11=c.make_url_authed('picture/w1.jpg')
        url12=c.make_url_authed('picture/w2.jpg')
        url13=c.make_url_authed('picture/w4.jpg')
        return render_template('wly.html',url10=url10,url11=url11,url12=url12,url13=url13,url14=url7)
    else:
        names=(****************************************************************************************)
        num=len(names)
        for i in range(0,num):
            if password==names[i][0]:
                na=names[i][1]
                words=name.example(na)
                nameurl=s.make_url_authed('picture/'+na+'.png')
                return render_template('newyear.html',url1=url1,url2=url2,url3=url3,url4=url4,url5=url5,nameurl=nameurl,words=words)
        return render_template('seeyou.html',url0=url0)
        
if __name__ == '__main__':
    app.run()
