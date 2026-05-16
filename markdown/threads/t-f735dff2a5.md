[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Needed On Web Application using Fujitsu COBOL97 CGI-Subroutine

_4 messages · 3 participants · 2002-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web) · [`Help requests and how-to`](../topics.md#help)

---

### Help Needed On Web Application using Fujitsu COBOL97 CGI-Subroutine

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2002-07-17T01:14:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0207170014.7c9b8ebf@posting.google.com>`

```
Hi there,

I'm quite new with this group. Wishing all members fine.

I have a set of Fujitsu COBOL development tool with me. I am in the
middle of choosing to use PowerCOBOL, COBOL97 or Web-developmebt using
COBOL97 CGI-subroutines.

Thus, I hope if anyone out there can give me a hand if you have
experience or using the Fujitsu COBOL CGI Subroutines on developing
the web based e-commerce systems.

FYI, I have tried the sample program came with Fujitsu COBOL, but not
able to make it works!

Any other comment is welcome.


Thank you.

Calvin Chin
Ipmuda Berhad
Malaysia
```

#### ↳ Re: Help Needed On Web Application using Fujitsu COBOL97 CGI-Subroutine

- **From:** maross@texoma.net (Mike)
- **Date:** 2002-07-17T09:31:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2763b81a.0207170831.75d95bda@posting.google.com>`
- **References:** `<62843e96.0207170014.7c9b8ebf@posting.google.com>`

```
calvinchin@fm333.com (Calvin) wrote in message news:
> FYI, I have tried the sample program came with Fujitsu COBOL, but not
> able to make it works!

Hi Calvin;
  You are not clear to your development goal. Is it a Web-site(CGI) or
a PC-app(PowerCobol-97). If your goal is WWW then you need CGI and you
MUST have a working WebServer (IIS or Apache), which is on your
Windows CD or Http://apache.org for free.
   If above Web-server is working then you probably have a Http-path
error and/or your sample01.htm is being cached to view in I.E. using
file-drive-path verses IIS-webserver-Http. Look in your Web-browser
address bar and make sure it starts with http:// .You need to add a
pre html file to verify your server paths are correct PRIOR to
invoking a more complicated process such as CGI calls.
   Create a "KISS" Simple.html page with only this line 
<p><a href="http://(your_server)/(alias_path)/sample01.htm">         
http://(your_server)/(alias_path_to c:*\cgismp01)/sample01.htm</a></p>

example <a  href="http://mikepc/z/sample01.htm"> 
http://mike/z/sample01.htm</a>
   Add @CBR_ATTACH_TOOL=test to your cobol85.cbr file IF YOU NEED to
start the COBOL-97 debugger.
   Start your IIS Personal Web Manager and in advanced give the
cgismp01.exe *alias_path  execute,read,write,Script Source Access
permissions.
   Start your Simple.html page, click the link in windows explorer OR
set Simple.html in <a href-link from your Personal-Web-Manager e.g.
http://mikepc (no .com etc)  If your IIS is set up properly you will
get Simple.html else your problem is your server setup and/or path.
 IF Simple.html is working from your IIS-link (e.g. http://mikepc)
then you can simplify sample01.htm to <form method="post"
action="cgismp01.exe">   (verses Http: path needed).
However I would suggest if you are not migrating Cobol code and your
goal is WWW-b2b  you set up a PHP-MySql-Apache PC workstation as there
are tons of resources on the WWW or maybe Fujitsu-Linux will include
better MySql-integration? Good Luck Mike
```

##### ↳ ↳ Re: Help Needed On Web Application using Fujitsu COBOL97 CGI-Subroutine

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2002-07-18T03:13:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0207180213.3dd411b7@posting.google.com>`
- **References:** `<62843e96.0207170014.7c9b8ebf@posting.google.com> <2763b81a.0207170831.75d95bda@posting.google.com>`

```
maross@texoma.net (Mike) wrote in message news:<2763b81a.0207170831.75d95bda@posting.google.com>...
> calvinchin@fm333.com (Calvin) wrote in message news:
> > FYI, I have tried the sample program came with Fujitsu COBOL, but not
…[34 more quoted lines elided]…
> better MySql-integration? Good Luck Mike

Hi Mike,

Your views are really helpful. Thanks.

Yes, my goal is to develop web application using CGI routines and html
files. I ran Personal Web server for testing of the Sample01.html in
my PC. Not working!
Or is it really need IIS or Apache?
 
Any other better guide book or manuals on this topic besides Fujitsu
COBOL's short manual?

Thank you.

Regards,
Calvin
```

###### ↳ ↳ ↳ Re: Help Needed On Web Application using Fujitsu COBOL97 CGI-Subroutine

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-19T07:54:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D37B79D.AF7F4CED@Azonic.co.nz>`
- **References:** `<62843e96.0207170014.7c9b8ebf@posting.google.com> <2763b81a.0207170831.75d95bda@posting.google.com> <62843e96.0207180213.3dd411b7@posting.google.com>`

```
Calvin wrote:
> 
> Yes, my goal is to develop web application using CGI routines and html
> files. I ran Personal Web server for testing of the Sample01.html in
> my PC. Not working!
> Or is it really need IIS or Apache?

Try Xitami (www.Xitami.com) as it is easy to set up and works.  It will
run on Windows 95/98/etc and there are Unix/Linux versions.  It does
proper CGI.  
 
> Any other better guide book or manuals on this topic besides Fujitsu
> COBOL's short manual?

Plenty on CGI, Web Serving and HTML, hundreds even.  None on what
Fujitsu do with their routines which hide what is really going on.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
