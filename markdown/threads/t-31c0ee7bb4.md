[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The MicroSoft view of multi-tier development.

_3 messages · 3 participants · 2002-12_

---

### The MicroSoft view of multi-tier development.

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-12-09T09:57:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0212090957.5efc5419@posting.google.com>`

```
Many of you will know that I have been advocating the use of
components for encapsulating Business Logic almost since they became
available.

I was persuaded to this point of view by developing and using
ActiveX/COM components in COBOL, using the Object Oriented features of
Fujitsu COBOL and PowerCOBOL. (In fact, I still use COBOL for this and
really enjoy doing it...)

COM components are "wrapped" in a common interface based on
MicroSoft's "Component Object Model". If you use Fujitsu all the
"donkey work" of this wrapping is transparent to you and you can
concentrate simply on the Methods, Attributes (Properties) and Events
of your specific component.

In Java, the same functionality can be achieved by building Java
Beans. As MicroSoft's COM/OLE and the OMG's CORBA functionality have
been growing together, it is now possible to use COM objects under
CORBA and there is also software available to "re-wrap" Java Beans for
use as COM objects.

When it comes to using the Web as the User Interface (or 1st tier of
your n-tier application design), the availability of components
written in Java and COBOL (or anything else that is useful) becomes
apparent because you can embed COM components into your Web Page using
HTML tags and/or JavaScript as "glue". The full implications of all
this are way beyond the scope of this post, but suffice to say, I have
been doing this for some time now. I taught myself JavaScript about a
year ago when I realised that I needed more on the Web pages than HTML
could easily provide. I developed a few Web Applications in order to
consolidate this but, up until recently, the nuances of ASP (Active
Server Pages) had escaped me.

Recently I decided to get into ASP and found, to my delight that it is
really JavaScript re-invented <G> (OK, it is really VBSCript because
that is MS's preference, but they DO allow JavaScript...)

Imagine my surprise, when scanning the MSDN posts on ASP, to come
across the following:

============================= quote from MSDN 
=============================
Proper Use of ASP

With ASP, you can easily and quickly create Web applications, in a
fraction of the time it would take with a more conventional
server-side language, such as C or C++. [...or other procedural
language, like COBOL. Pete.]

However, the ease with which you can create ASP-based applications
belies the complexity of the server processing and client-server
interaction required by that application. It is possible that Web
applications that have been created with extensive ASP scripting will
not scale well.

To avoid scalability problems, there are two points to keep in mind
when developing with ASP:

ASP is the "Glue" 
ASP should not be used for business logic 
The first point emphasizes that ASP dovetails with HTML, client-side
scripting using DHTML, and XML to create a powerful platform for
interacting with the user. ASP scripting was designed to be used to
bind the user interface to the business logic of the Web application,
and ASP was optimized for these sorts of tasks.

The second point should serve as an important reminder: If you find
that most of your business logic is embedded into the ASP, your
application will probably not scale properly. It is true that ActiveXï¿½
scripting languages, hosted by ASP, are capable of accomplishing a
great deal of business logic processing.

[....this bit blew me away...Pete]
However, if the business logic required for your Web application is
more than trivial, then that business logic should be folded into a
new COM component, rather than embedded in ASP scripts.

Optimizing ASP on IIS

Once you have established that your use of ASP is appropriate for the
design of your application, and you have encapsulated the bulk of your
business logic into COM components, there are two avenues by which you
can further improve the performance and scalability of your Web
application:  <snip>
============================ end quote from MSDN 
============================

So, it would seem that the MS view confirms what I arrived at
independently some years ago... Use components for Business Logic!

Of course, if you do, you will have little need or use for maintaining
Source code...<G>

Repeat after me...<G>
"The future of programming is in Object Orientation. Java will teach
me this quickly and painlessly if I just open my mind and set aside
what I already "know". Once I have this, I can use OO COBOL and I can
learn JavaScript, VBScript, and ASP VERY easily. This will help me
assure my future."

Expand your skill set. 

Pete.
```

#### ↳ Re: The MicroSoft view of multi-tier development.

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-10T05:02:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qzeJ9.124925$Gc.4184315@twister.austin.rr.com>`
- **References:** `<b3638c46.0212090957.5efc5419@posting.google.com>`

```
So, at the risk of wrath unleashed, learn server side Java, and instead of ASP, use JSP's and Enterprise Java Beans where
appropriate. This is a very good technology indeed, especially when combined with an appropriate use of Javascript.

Scalability is virtually unlimited with this methodology, and since you can build/utilize a standard repository, as wells as take
full advantage of OOD, well, it is much better than trying to do it with VSB. I will say that VSB has some very nice features, but
any old Java class can be used in a JSP, and EJBs make things like database work both easy and even fun.

Java works in this environment far *far* better than when trying to use it to create a GUI. :/


"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message news:b3638c46.0212090957.5efc5419@posting.google.com...
> Many of you will know that I have been advocating the use of
> components for encapsulating Business Logic almost since they became
…[100 more quoted lines elided]…
> Pete.
```

##### ↳ ↳ Re: The MicroSoft view of multi-tier development.

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-10T09:45:32
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at4d48$5rp$1@hyperion.microfocus.com>`
- **References:** `<b3638c46.0212090957.5efc5419@posting.google.com> <qzeJ9.124925$Gc.4184315@twister.austin.rr.com>`

```
And at Micro Focus we allow COBOL to be used in BOTH of these alternative
scenarios. ;-)

www.microfocus.com

"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:qzeJ9.124925$Gc.4184315@twister.austin.rr.com...
> So, at the risk of wrath unleashed, learn server side Java, and instead of
ASP, use JSP's and Enterprise Java Beans where
> appropriate. This is a very good technology indeed, especially when
combined with an appropriate use of Javascript.
>
> Scalability is virtually unlimited with this methodology, and since you
can build/utilize a standard repository, as wells as take
> full advantage of OOD, well, it is much better than trying to do it with
VSB. I will say that VSB has some very nice features, but
> any old Java class can be used in a JSP, and EJBs make things like
database work both easy and even fun.
>
> Java works in this environment far *far* better than when trying to use it
to create a GUI. :/
>
>
> "Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:b3638c46.0212090957.5efc5419@posting.google.com...
> > Many of you will know that I have been advocating the use of
> > components for encapsulating Business Logic almost since they became
…[102 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
