[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EASYUI AND COBOL... Just a question

_6 messages · 3 participants · 2020-01_

---

### EASYUI AND COBOL... Just a question

- **From:** "federico.priolo" <ua-author-14501736@usenetarchives.gap>
- **Date:** 2020-01-04T13:47:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com>`

```
HI all. just to try I am playing with the easyui jquery tool. I
wrote two simple html pages ( a login and a menu htm).

from the form post method of the login I call the cobol procedure (fujitsu cobol) that read the field and then simple (should !!) write the second html page.

this is already perfomed without easyui without any troubles..

but in this case unfortuanately the secondo menu doesn't appears. ..

is anyone using easyui and cobol together ?

Federico
```

#### ↳ Re: EASYUI AND COBOL... Just a question

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2020-01-04T18:01:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad54d61fc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com>`
- **References:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com>`

```
[posted and emailed]

In article ,
wrote:
› HI all. just to try I am playing with the easyui jquery tool.

Please do your own homework.

DD
```

##### ↳ ↳ Re: EASYUI AND COBOL... Just a question

- **From:** "federico.priolo" <ua-author-14501445@usenetarchives.gap>
- **Date:** 2020-01-05T04:15:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad54d61fc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ad54d61fc-p2@usenetarchives.gap>`
- **References:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com> <gap-0ad54d61fc-p2@usenetarchives.gap>`

```
Here the files I used and some brief explanations: the webserver is apache and i am running on windows the cgi-open virtual path is configurated into the httpd.conf like you can see:

ScriptAlias /cgi-open/ "c:/apache/htdocs/OpenPA/"
the contents you find in this email:

the cobol compiler is fujitsu cobol

other test I did.. running directly the cobol it put on the screen the single line (without execute any javascript code however). using the link on the login.htm to the menu.htm thee form it correctly showed.

1) login.htm
2) menu.hmt
3) e very simple wrapper cobol last test I did is using writing single line from the template men.htm instead using the complete send that fujitsy also allows with the CALL "COBW3_PUT_HTML" USING COBW3.

1) login.htm

























Inserire i dati di autenticazione






























Accedi




Pulisci
```

###### ↳ ↳ ↳ Re: EASYUI AND COBOL... Just a question

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2020-01-06T00:42:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad54d61fc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ad54d61fc-p3@usenetarchives.gap>`
- **References:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com> <gap-0ad54d61fc-p2@usenetarchives.gap> <gap-0ad54d61fc-p3@usenetarchives.gap>`

```
In article <9c4aa4ee-0967-4f73-8ee9-d85··5@goo··s.com>,
federico priolo wrote:

[snip]

› any helps will be really appreciated

This is beyond my own simple understanding, I'll help by stepping back and
leaving the responding to others of greater learning.

DD
```

#### ↳ Re: EASYUI AND COBOL... Just a question

- **From:** "federico.priolo" <ua-author-14501445@usenetarchives.gap>
- **Date:** 2020-01-06T11:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad54d61fc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com>`
- **References:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com>`

```
I solved replacing the easy-window with easy-panel widget ...


Federico
```

##### ↳ ↳ Re: EASYUI AND COBOL... Just a question

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2020-01-08T21:27:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ad54d61fc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ad54d61fc-p5@usenetarchives.gap>`
- **References:** `<b42e0f08-efe0-4195-9adb-87960e3e7cd0@googlegroups.com> <gap-0ad54d61fc-p5@usenetarchives.gap>`

```
In article ,
federico priolo wrote:
› I solved replacing the easy-window with easy-panel widget ...

Greatly appreciated, Mr Priolo.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
