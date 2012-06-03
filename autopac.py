#!/usr/bin/env python
#coding:utf-8

import web
from config import settings

render = settings.render

class autopac:
    def GET(self):
        return render.autopac()
    def POST(self):
        import base64
        web.header('Content-Type', 'application/x-ns-proxy-autoconfig', 
            unique=True)
        i = web.input()
        type1 = 'HTTP_PROXY'
        proxy1 = 'PROXY'
        port1 = '8080'
        if i.ptype and i.ptype == 'SOCKS5':
            type1 = 'SOCKS5_PROXY'
            proxy1 = 'SOCKS5'
        if i.port:
            port1 = i.port
        proxy_https = i.get('sptssl','')
        proxy_https = '//' if '1' == proxy_https else ''
        header1 = '''function FindProxyForURL(url, host) {
    HTTPS_PROXY = "DIRECT";
    %s = "%s 127.0.0.1:%s";//gae
    DIRECT = "DIRECT";
''' % (type1,proxy1,port1)
        foot1 = '''
if(/^http:\/\/v2ex\.com/i.test(url)) return DIRECT;
%sif(/^https:\/\//i.test(url)) return HTTPS_PROXY;

return %s;
}
''' % (proxy_https,type1)
        body1 = ''
        str1 = i.myarea.strip()
        l1 = str1.split(r',')
        s2 = r'if(/'
        s3 = r'/i.test(url)) return DIRECT;'
        for each_str1 in l1:
            body1 += s2 + each_str1.replace(r'.',r'\.') + s3 + '\
            '

        _64pac =  base64.b64encode(header1 + body1 + foot1)

        s5 = '''function decode64(_1){var _2="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";var _3="";var _4,_5,_6;var _7,_8,_9,_a;var i=0;_1=_1.replace(/[^A-Za-z0-9\+\/\=]/g,"");do{_7=_2.indexOf(_1.charAt(i++));_8=_2.indexOf(_1.charAt(i++));_9=_2.indexOf(_1.charAt(i++));_a=_2.indexOf(_1.charAt(i++));_4=(_7<<2)|(_8>>4);_5=((_8&15)<<4)|(_9>>2);_6=((_9&3)<<6)|_a;_3=_3+String.fromCharCode(_4);if(_9!=64){_3=_3+String.fromCharCode(_5);}if(_a!=64){_3=_3+String.fromCharCode(_6);}}while(i<_1.length);return _3;}eval(decode64("'''
        s6 = '"))'
        return s5 + _64pac + s6

