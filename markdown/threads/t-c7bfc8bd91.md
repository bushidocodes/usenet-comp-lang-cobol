[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCOBOL CGI Forms

_9 messages · 7 participants · 1998-11 → 1998-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### AcuCOBOL CGI Forms

- **From:** "Robert Annandale" <rob_a@unipharm.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73f141$fae$1@fountain.mindlink.net>`

```
AcuCOBOL AcuGT Version 4.0.0

I have a website using COBOL CGI forms.
My knowledge on HTML is limited to the basics.

I am able to receive data from <input type HTML fields, read an indexed file
and send output back to the HTML
document.  However, I am unable to display a COBOL table in the HTML
document.
My code is below,

working-storage section.
       01  support-form is external-form.
            05  support-type  pic x(8) is identified by "support-type".

       01  type-form is external-form identified by "description".
            05  call-type     pic x(30) occurs 30.

procedure division.

    accept support-form.

    i read the indexed file with the input.
    load up call-type with a varying index.

    display type-form. -> this displays an html document.

the html value that should receive this field is enclosed in %% as
stipulated by AcuCOBOLs manual.

      <center>
        <p>Problem<br>
        <select name="module" width="100">
        <option selected>- Problem  with...-
        <option value="%%call-type%%">
        </select>
        </p>
      </center>

I want the above HTML code to display a pull down menu loaded with my occurs
30 values.
Does anyone have any idea how to do this?
Thanks in advance.

___________________________
Rob Annandale;   ICQ#  5760258
rob_a@unipharm.com

* It is better to live one day as a tiger, than a thousand years as a sheep.
*
- Nepalese proverb.
```

#### ↳ Re: AcuCOBOL CGI Forms

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6aE62.195$Q91.523552@news.rdc1.on.wave.home.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net>`

```
What I know about ACUCOBOL can be written on the head of a pin with a magic
marker.

However, HTML for a <SELECT> control, it should look something like...

        <SELECT NAME="SORT">
          <OPTION VALUE="-a">Ascending</OPTION>
          <OPTION VALUE="-d">Descending</OPTION>
        </SELECT>

The value part is not required.
So, you might want to try...
    <OPTION>%%call-type%%</OPTION>

or
    <OPTION VALUE="%%call-type%%>%%call-type%%</OPTION>


Robert Annandale wrote in message <73f141$fae$1@fountain.mindlink.net>...
>AcuCOBOL AcuGT Version 4.0.0
>
…[3 more quoted lines elided]…
>I am able to receive data from <input type HTML fields, read an indexed
file
>and send output back to the HTML
>document.  However, I am unable to display a COBOL table in the HTML
…[31 more quoted lines elided]…
>I want the above HTML code to display a pull down menu loaded with my
occurs
>30 values.
>Does anyone have any idea how to do this?
…[6 more quoted lines elided]…
>* It is better to live one day as a tiger, than a thousand years as a
sheep.
>*
>- Nepalese proverb.
>
>
```

##### ↳ ↳ Re: AcuCOBOL CGI Forms

- **From:** "David Sanders" <dsanders@synkronix.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b25b4$0$12780@nntp1.ba.best.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net> <6aE62.195$Q91.523552@news.rdc1.on.wave.home.com>`

```
You may look into using PERCobol (www.synkronix.com), which is much more Web
friendly.

Some features include:

EXEC-HTML for embedded html,
GUI and Java Object support (including JavaBeans),
EXEC-SQL, and
standard COBOL code can run as an Applet in a browser or as an application!

You can download a 10 day trial of the Educational version at:

http://www.synkronix.com/educational/educational.html

Thanks,
David Sanders
Synkronix, Inc.

>Robert Annandale wrote in message <73f141$fae$1@fountain.mindlink.net>...
>>AcuCOBOL AcuGT Version 4.0.0
…[56 more quoted lines elided]…
>
```

#### ↳ Re: AcuCOBOL CGI Forms

- **From:** mattr@mentis.com.au
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73fgna$fsq$1@nnrp1.dejanews.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net>`

```
In article <73f141$fae$1@fountain.mindlink.net>,
  "Robert Annandale" <rob_a@unipharm.com> wrote:
> AcuCOBOL AcuGT Version 4.0.0
>
…[14 more quoted lines elided]…
>             05  call-type     pic x(30) occurs 30.

If you are going to send a table to a pull-down menu (ie <SELECT>), then you
really need to define a seperate cgi-variable for each bit of data.  ie :

        01  type-form is external-form identified by "description".
             05  call-type1     pic x(30) identified by "call-type1".
             05  call-type2     pic x(30) identified by "call-type2".
             05  call-type3     pic x(30) identified by "call-type3".
                       ... etc ...


> procedure division.
>
…[18 more quoted lines elided]…
>

 ... and then the HTML template would go something like this :

       <center>
         <p>Problem<br>
         <select name="module" width="100">
         <option>%%call-type1%%</option>
         <option>%%call-type2%%</option>
         <option>%%call-type3%%</option>
                ... etc ...
         </select>
         </p>
       </center>

thank god for cut & paste ! :-)

> I want the above HTML code to display a pull down menu loaded with my occurs
> 30 values.
> Does anyone have any idea how to do this?
> Thanks in advance.
>


Hope that was helpful.

Matt Robinson
Support Consultant - Mentis Technologies
----------------------------------------
<insert something witty here>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: AcuCOBOL CGI Forms

- **From:** MJHOPKI@ertltoys.com
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73fggo$fom$1@nnrp1.dejanews.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net>`

```
I don't think tables are supported very well yet.  To accomplish this you are
going to have to do a bit of cumbersome programming.  Remember that the
%%variable%% is replaced by the runtime via a scan that occurs just before
sending the final HTML results to the web server.  Make your input form look
something like :

        01  type-form is external-form identified by "description".
          03 call-info.
             05  call-type-01     pic x(30) identified by "type-01".
             05  call-type-02     pic x(30) identified by "type-02".
             05  call-type-03     pic x(30) identified by "type-03".
             .
             .
             .
             05  call-type-30     pic x(30) identified by "type-30".

        01  type-table.
             05  call-type        pic x(30) occurs 30 times.


Now in your program move call-info to the type-table.  Manipulate the
type-table in your code as usual and move it to the form table before sending
the form back out.  It seems like you should at least be able to use a
redefines on the form but if you do that it doesn't work properly.  I don't
know if that is by design or a bug.  Your HTML should then work - just use
the individual form variable listed in each of the "option value" statements
of your HTML select.

I encourage everyone to try using Acucobol for CGI.  It is quite simple and
you can produce some powerful results.

Hope this helps.

Jay_Hopkins@ertltoys.com

Be careful in your HTML when using Input statements - IE will show an input
box with the <FORM> tag but Netscape requires at least the beginning <FORM>
tag.

In article <73f141$fae$1@fountain.mindlink.net>,
  "Robert Annandale" <rob_a@unipharm.com> wrote:
> AcuCOBOL AcuGT Version 4.0.0
>
…[50 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: AcuCOBOL CGI Forms

- **From:** "Rob Aardvark" <zimboon@hotmail.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73g2rc$1ri$1@fountain.mindlink.net>`
- **References:** `<73f141$fae$1@fountain.mindlink.net> <73fggo$fom$1@nnrp1.dejanews.com>`

```
Thanks guys, but it was this cumbersome code that I was hoping to avoid.
If I ever needed to change the size of the table, I would have to go and
adjust all those other values.
I submitted this request on several other forums, still no luck.
The site is up and running, looks pretty good on the outside, but the
code...sheeesh.

Rob Annandale (Original poster)


>        01  type-form is external-form identified by "description".
>          03 call-info.
…[22 more quoted lines elided]…
>>       </center>
```

###### ↳ ↳ ↳ Re: AcuCOBOL CGI Forms

- **From:** MJHOPKI@ertltoys.com
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73hnkc$d59$1@nnrp1.dejanews.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net> <73fggo$fom$1@nnrp1.dejanews.com> <73g2rc$1ri$1@fountain.mindlink.net>`

```
You wouldn't necessarily have to change all the definitions if you changed the
size of the table.  You could use variable names in the "identified by" clause
on each field.  Then utilizing the fact that the runtime replaces any
%%variable%% with it's contents you could build your HTML dynamically within
your program.  I do this to attain various effects with HTML documents that
normally wouldn't be possible with static pages.  This is one of the true
advantages of this type of solution.

jh

In article <73g2rc$1ri$1@fountain.mindlink.net>,
  "Rob Aardvark" <zimboon@hotmail.com> wrote:
> Thanks guys, but it was this cumbersome code that I was hoping to avoid.
> If I ever needed to change the size of the table, I would have to go and
…[33 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: AcuCOBOL CGI Forms

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365e5af0.8459768@netnews>`
- **References:** `<73f141$fae$1@fountain.mindlink.net> <73fggo$fom$1@nnrp1.dejanews.com>`

```
'Twas Tue, 24 Nov 1998 23:46:39 GMT, when MJHOPKI@ertltoys.com illuminated
comp.lang.cobol thusly:

>Be careful in your HTML when using Input statements - IE will show an input
>box with the <FORM> tag but Netscape requires at least the beginning <FORM>
>tag.

Do you mean "withOUT" the <FORM> tag"?
```

###### ↳ ↳ ↳ Re: AcuCOBOL CGI Forms

- **From:** MJHOPKI@ertltoys.com
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<741obb$5v9$1@nnrp1.dejanews.com>`
- **References:** `<73f141$fae$1@fountain.mindlink.net> <73fggo$fom$1@nnrp1.dejanews.com> <365e5af0.8459768@netnews>`

```
Yes I meant "withOUT".  Thanks for the correction.

jh

In article <365e5af0.8459768@netnews>,
  Barticus@att.spam.net (Randall Bart) wrote:
> 'Twas Tue, 24 Nov 1998 23:46:39 GMT, when MJHOPKI@ertltoys.com illuminated
> comp.lang.cobol thusly:
…[15 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
