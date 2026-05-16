[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 6.1 CGI facilities

_8 messages · 4 participants · 2002-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### Fujitsu 6.1 CGI facilities

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-16T00:42:44+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c441a17_3@Usenet.com>`

```
I am quite impressed by the "new" support for CGI in Fujitsu V6.1. and have
started using it for a "real" project.

However, I am really sweating the conversion of an HTML skeleton for output
directly from the CGI. Every time I issue a COBW3_PUT_HTML it returns code
6101 which means it can't read the skeleton file. I have tried using
relative and absolute paths for this file, placed it in the "scripts"
directory on the server, and even used a URL for it, all to no avail.

I would appreciate it if anyone else is using this product and can contact
me with any ideas, or indeed if anyone has any actual code that works and
does a conversion of output HTML.

It is being tested on MS Personal Web Server which supports CGI and SSI and
ISAPI (although I am not currently using ISAPI for this exercise.)

With Version 5, I used a third party product to output HTML but it could
only do one line at a time. V6 correctly outputs single lines of HTML using
the COBW3_PUT_TEXT function.

I have spent many hours trying to get the "bulk output" function to work and
am now looking at writing my own version of this function so I can get the
same effect using COBW3_PUT_TEXT. I really don't want to re-invent the wheel
(but when the wheel won't turn it is sometimes necessary...) Before I embark
on this 2 day exercise, I would really appreciate hearing from anybody who
is doing the same thing or has the delivered software working correctly.

Thanks,

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Fujitsu 6.1 CGI facilities

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-01-15T05:27:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0201150527.3d7e509b@posting.google.com>`
- **References:** `<3c441a17_3@Usenet.com>`

```
Without seeing your code, I don't know if you have the data area setup
property for the call or if you are setting all the necessary flags. 
This is from a Fujitsu example - there are several of them you can
find by putting COBW3_PUT_HTML in a Google search.


* Setup the prototype HTML file name
     MOVE "c:\ORANT\OWS\admin\OWS\WAS\HTTPD_SPICE\WWW\doc\messageResponse.htm"
       TO COBW3-HTML-FILENAME
* Set the CONTENT-TYPE to HTML
       SET COBW3-CONTENT-TYPE-HTML TO TRUE
* Send the completed HTML to the user
       CALL "COBW3_PUT_HTML" USING COBW3.

Where COBW3 is a Fujitsu copybook.

There's also a lot of other pre-initialization you need to do for
COBW3 -
see the example here:

http://www.adtools.com/news/prelease/oraclecart.htm



"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3c441a17_3@Usenet.com>...
> I am quite impressed by the "new" support for CGI in Fujitsu V6.1. and have
> started using it for a "real" project.
…[35 more quoted lines elided]…
>                 http://www.usenet.com
```

##### ↳ ↳ Re: Fujitsu 6.1 CGI facilities

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-16T11:40:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c44b5bd_14@Usenet.com>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com>`

```
Thanks Thane.

There is nothing new here and I am doing everything you describe (and more
besides...<G>)

I have also examined the sample code (but didn't run a GOOGLE search; that's
a good idea...<G>) but the sample code (cgismp01) as delivered cannot run.
(The library paths will only work on the machine of the guy who wrote the
sample, as they are incorrect). I corrected the sample code and ran it, but
get the same result. I also find that the Debugger will not invoke through
@CBR_ATTACH_TOOL so I can't really examine what is going on. The message
written to the message file says "Service not run" and the Manual says I
need to start the "COBOL ATTACH TOOLS" service. I haven't the faintest idea
what this means or how to do it and can't find anything in the documentation
which explains it or even refers to it.

I did manage to get messages from CGI appearing on the Browser by using
COBW3-DMODE-DBG (as described in the manual) and that is how I know it is
returning error 6101.

After 25 hours I am running out of options. If a tool takes longer to get
working than doing the job manually, then it is probably wiser to do the job
manually in the first place.

The Web support in V6.1 overall, is impressive and the generation capability
through the Editor is excellent. However, it is not much help if the
generated code won't run...

I'll explore the other options you have posted and I'll try the GOOGLE
Search.

It is very possible that it just won't work with Win 98SE using PWS, or
maybe it is necessary to use the multi-threading RTS, there are many
possibilities...

Thanks for your post and suggestions.

In the meantime, I would really like to hear from anyone who has actually
DONE it, so we can compare environments, etc.

Pete.

Thane Hubbell <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0201150527.3d7e509b@posting.google.com...
> Without seeing your code, I don't know if you have the data area setup
> property for the call or if you are setting all the necessary flags.
…[5 more quoted lines elided]…
>      MOVE
"c:\ORANT\OWS\admin\OWS\WAS\HTTPD_SPICE\WWW\doc\messageResponse.htm"
>        TO COBW3-HTML-FILENAME
> * Set the CONTENT-TYPE to HTML
…[14 more quoted lines elided]…
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3c441a17_3@Usenet.com>...
> > I am quite impressed by the "new" support for CGI in Fujitsu V6.1. and
have
> > started using it for a "real" project.
> >
> > However, I am really sweating the conversion of an HTML skeleton for
output
> > directly from the CGI. Every time I issue a COBW3_PUT_HTML it returns
code
> > 6101 which means it can't read the skeleton file. I have tried using
> > relative and absolute paths for this file, placed it in the "scripts"
> > directory on the server, and even used a URL for it, all to no avail.
> >
> > I would appreciate it if anyone else is using this product and can
contact
> > me with any ideas, or indeed if anyone has any actual code that works
and
> > does a conversion of output HTML.
> >
> > It is being tested on MS Personal Web Server which supports CGI and SSI
and
> > ISAPI (although I am not currently using ISAPI for this exercise.)
> >
> > With Version 5, I used a third party product to output HTML but it could
> > only do one line at a time. V6 correctly outputs single lines of HTML
using
> > the COBW3_PUT_TEXT function.
> >
> > I have spent many hours trying to get the "bulk output" function to work
and
> > am now looking at writing my own version of this function so I can get
the
> > same effect using COBW3_PUT_TEXT. I really don't want to re-invent the
wheel
> > (but when the wheel won't turn it is sometimes necessary...) Before I
embark
> > on this 2 day exercise, I would really appreciate hearing from anybody
who
> > is doing the same thing or has the delivered software working correctly.
> >
…[10 more quoted lines elided]…
> >                 http://www.usenet.com



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 CGI facilities

- **From:** COBOL Gold Mine at ILS International <cgm@ils-international.com>
- **Date:** 2002-01-17T00:15:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C461774.3837D83@ils-international.com>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com> <3c44b5bd_14@Usenet.com>`

```
It does work.  It does work beautifully and reliably

To see COBOL in Action on the Internet like you have never seen it before visit
COBOLonWeb.com .

To test and experience a full blown production eCommerce application powered by
Fujitsu COBOL, visit ILS's own online store - COBOL Gold  Mine eStore - that
customers from around the globe are using to order the COBOL products. (100%
COBOL and HTML. Nothing else! Javascript is there just to make COBOL "swing"!!).

__________________________________________
COBOL is dead, Long Live COBOL!!(SM)
COBOL Gold Mine(SM) staff
At your service 24 hours a day, 7 days a week...AROUND THE GLOBE
www.ils-international.com

"Peter E. C. Dashwood" wrote:

> Thanks Thane.
>
…[36 more quoted lines elided]…
> DONE it, so we can compare environments, etc.

> Pete.
>
…[84 more quoted lines elided]…
>               http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 CGI facilities

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-18T11:50:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c47598a_15@Usenet.com>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com> <3c44b5bd_14@Usenet.com> <3C461774.3837D83@ils-international.com>`

```

COBOL Gold Mine at ILS International <cgm@ils-international.com> wrote in
message news:3C461774.3837D83@ils-international.com...
> It does work.  It does work beautifully and reliably
>
Wow! I guess I must be stupid then...

Can I have half an ounce of whatever you're on?

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 CGI facilities

_(reply depth: 5)_

- **From:** COBOL Gold Mine at ILS International <cgm@ils-international.com>
- **Date:** 2002-01-18T14:16:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C482F4C.A04DBA09@ils-international.com>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com> <3c44b5bd_14@Usenet.com> <3C461774.3837D83@ils-international.com> <3c47598a_15@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:

> COBOL Gold Mine at ILS International <cgm@ils-international.com> wrote in
> message news:3C461774.3837D83@ils-international.com...
…[7 more quoted lines elided]…
>

Yes you can.
Please follow the instructions in "Info & Inquiries" at the bottom of
COBOLonWeb.com homepage
__________________________________________
COBOL is dead, Long Live COBOL!!(SM)
COBOL Gold Mine(SM) staff
At your service 24 hours a day, 7 days a week...AROUND THE GLOBE
www.ils-international.com
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 CGI facilities

- **From:** COBOL Gold Mine at ILS International <cgm@ils-international.com>
- **Date:** 2002-01-17T00:27:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C461A50.440E0135@ils-international.com>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com> <3c44b5bd_14@Usenet.com>`

```
It does work.  It does work beautifully and reliably

To see COBOL in Action on the Internet like you have never seen it before visit
COBOLonWeb.com.

To test and experience a full blown production eCommerce application powered by
Fujitsu COBOL, visit ILS's own online store - COBOL Gold  Mine eStore - that
customers from around the globe are using to order the COBOL products. (100%
COBOL and HTML. Nothing else! Javascript is there just to make COBOL "swing"!!).

__________________________________________
COBOL is dead, Long Live COBOL!!(SM)
COBOL Gold Mine(SM) staff
At your service 24 hours a day, 7 days a week...AROUND THE GLOBE
www.ils-international.com


"Peter E. C. Dashwood" wrote:

> Thanks Thane.
>
…[124 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Fujitsu 6.1 CGI facilities

_(reply depth: 4)_

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-01-17T16:34:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u2D18.41689$uA.401189@rwcrnsc51.ops.asp.att.net>`
- **References:** `<3c441a17_3@Usenet.com> <bfdfc3e8.0201150527.3d7e509b@posting.google.com> <3c44b5bd_14@Usenet.com> <3C461A50.440E0135@ils-international.com>`

```
Post it again...... someone may have missed it

  "COBOL Gold Mine at ILS International" <cgm@ils-international.com> wrote in message news:3C461A50.440E0135@ils-international.com...
  It does work.  It does work beautifully and reliably 
  To see COBOL in Action on the Internet like you have never seen it before visit 
  COBOLonWeb.com. 

  To test and experience a full blown production eCommerce application powered by 
  Fujitsu COBOL, visit ILS's own online store - COBOL Gold  Mine eStore - that 
  customers from around the globe are using to order the COBOL products. (100% 
  COBOL and HTML. Nothing else! Javascript is there just to make COBOL "swing"!!). 

  __________________________________________ 
  COBOL is dead, Long Live COBOL!!(SM) 
  COBOL Gold Mine(SM) staff 
  At your service 24 hours a day, 7 days a week...AROUND THE GLOBE 
  www.ils-international.com 
    

  "Peter E. C. Dashwood" wrote: 

    Thanks Thane. 
    There is nothing new here and I am doing everything you describe (and more 
    besides...<G>) 

    I have also examined the sample code (but didn't run a GOOGLE search; that's 
    a good idea...<G>) but the sample code (cgismp01) as delivered cannot run. 
    (The library paths will only work on the machine of the guy who wrote the 
    sample, as they are incorrect). I corrected the sample code and ran it, but 
    get the same result. I also find that the Debugger will not invoke through 
    @CBR_ATTACH_TOOL so I can't really examine what is going on. The message 
    written to the message file says "Service not run" and the Manual says I 
    need to start the "COBOL ATTACH TOOLS" service. I haven't the faintest idea 
    what this means or how to do it and can't find anything in the documentation 
    which explains it or even refers to it. 

    I did manage to get messages from CGI appearing on the Browser by using 
    COBW3-DMODE-DBG (as described in the manual) and that is how I know it is 
    returning error 6101. 

    After 25 hours I am running out of options. If a tool takes longer to get 
    working than doing the job manually, then it is probably wiser to do the job 
    manually in the first place. 

    The Web support in V6.1 overall, is impressive and the generation capability 
    through the Editor is excellent. However, it is not much help if the 
    generated code won't run... 

    I'll explore the other options you have posted and I'll try the GOOGLE 
    Search. 

    It is very possible that it just won't work with Win 98SE using PWS, or 
    maybe it is necessary to use the multi-threading RTS, there are many 
    possibilities... 

    Thanks for your post and suggestions. 

    In the meantime, I would really like to hear from anyone who has actually 
    DONE it, so we can compare environments, etc. 

    Pete. 

    Thane Hubbell <thaneh@softwaresimple.com> wrote in message 
    news:bfdfc3e8.0201150527.3d7e509b@posting.google.com... 
    > Without seeing your code, I don't know if you have the data area setup 
    > property for the call or if you are setting all the necessary flags. 
…[5 more quoted lines elided]…
    >      MOVE 
    "c:\ORANT\OWS\admin\OWS\WAS\HTTPD_SPICE\WWW\doc\messageResponse.htm" 
    >        TO COBW3-HTML-FILENAME 
    > * Set the CONTENT-TYPE to HTML 
…[14 more quoted lines elided]…
    > "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message 
    news:<3c441a17_3@Usenet.com>... 
    > > I am quite impressed by the "new" support for CGI in Fujitsu V6.1. and 
    have 
    > > started using it for a "real" project. 
    > > 
    > > However, I am really sweating the conversion of an HTML skeleton for 
    output 
    > > directly from the CGI. Every time I issue a COBW3_PUT_HTML it returns 
    code 
    > > 6101 which means it can't read the skeleton file. I have tried using 
    > > relative and absolute paths for this file, placed it in the "scripts" 
    > > directory on the server, and even used a URL for it, all to no avail. 
    > > 
    > > I would appreciate it if anyone else is using this product and can 
    contact 
    > > me with any ideas, or indeed if anyone has any actual code that works 
    and 
    > > does a conversion of output HTML. 
    > > 
    > > It is being tested on MS Personal Web Server which supports CGI and SSI 
    and 
    > > ISAPI (although I am not currently using ISAPI for this exercise.) 
    > > 
    > > With Version 5, I used a third party product to output HTML but it could 
    > > only do one line at a time. V6 correctly outputs single lines of HTML 
    using 
    > > the COBW3_PUT_TEXT function. 
    > > 
    > > I have spent many hours trying to get the "bulk output" function to work 
    and 
    > > am now looking at writing my own version of this function so I can get 
    the 
    > > same effect using COBW3_PUT_TEXT. I really don't want to re-invent the 
    wheel 
    > > (but when the wheel won't turn it is sometimes necessary...) Before I 
    embark 
    > > on this 2 day exercise, I would really appreciate hearing from anybody 
    who 
    > > is doing the same thing or has the delivered software working correctly. 
    > > 
…[10 more quoted lines elided]…
    > >                 http://www.usenet.com 

     Posted Via Usenet.com Premium Usenet Newsgroup Services 
    ---------------------------------------------------------- 
        ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY ** 
    ---------------------------------------------------------- 
                    http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
