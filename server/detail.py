"""
import time
import requests
import json
import shutil

start_time = time.time()


def find_between(s, start, end):
    return (s.split(start))[1].split(end)[0]


class user:
    def __init__(self):
        self.s = requests.session()
        # self.s.proxies={"http","127.0.0.1:8888"}
        self.html_data = self.s.get('https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Host': 'vahan.nic.in'}, verify=False)
        self.token = find_between(self.html_data.text, '="j_id1:javax.faces.ViewState:0" value="',
                                  '" autocomplete="off" ', )
        self.arg1 = find_between(self.html_data.text, '<div class="col-md-12 center-position"><button id="',
                                 '" name="', )
        self.arg2 = find_between(self.html_data.text, '<div class="col-md-12"><input type="hidden" name="',
                                 '" value="" /><div id="userMessages" class="ui-messages ui-widget erro', )

    def print_data(self):
        return self.html_data.text

    def captcha(self):
        # self.html_data= self.s.get('http://jmiregular.ucanapply.com/universitysystem/student/'+self.token+'/view/')
        response = self.s.get("https://vahan.nic.in/nrservices/cap_img.jsp",
                              headers={'Referer': 'https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml',
                                       'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                                       'Host': 'vahan.nic.in', 'Connection': 'keep-alive'}, stream=True, verify=False)
        with open('img.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

    #        return self
    def fetch(self):
        self.captcha()
        cap = input("enter captcha: ")
        self.html_data = self.s.post('https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml',
                                     data={'javax.faces.partial.ajax': 'true', 'javax.faces.source': self.arg1,
                                           'javax.faces.partial.execute': '@all',
                                           'javax.faces.partial.render': 'rcDetailsPanel resultPanel userMessages capatcha txt_ALPHA_NUMERIC',
                                           self.arg1: self.arg1, 'masterLayout': 'masterLayout', self.arg2: '',
                                           'regn_no1_exact': 'DL3SAM4323', 'txt_ALPHA_NUMERIC': cap,
                                           'javax.faces.ViewState': self.token}, headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                'Host': 'vahan.nic.in', 'Referer': 'https://vahan.nic.in/nrservices/faces/user/searchstatus.xhtml',
                'Faces-Request': 'partial/ajax', 'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Origin': 'https://vahan.nic.in',
                'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin',
                'Accept': 'application/xml, text/xml, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9'}, verify=False)
        return self.html_data.text


r1 = user()
print(r1.fetch())
print("--- %s seconds1 ---" % (time.time() - start_time))
"""