[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL engine that works with Domino

_4 messages · 4 participants · 1998-03_

---

### COBOL engine that works with Domino

- **From:** "joel berger" <ua-author-2718587@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`

```

Anyone have any ideas on how I would take a COBOL calculation engine from
the Mainframe and use it as a back-end calculator for a Web site. Would
creating a DLL help with either Reali or Micro Focus? I assume I would have
to call the engine and pass information and get returned values. Not sure
how this would work? Would I need to write a Java program on the Server to
interface with this thing? Can I use CGI?

Anyone have any ideas?
```

#### ↳ Re: COBOL engine that works with Domino

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4b90f8e4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`
- **References:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`

```

Joel Berger wrote:
› 
› Anyone have any ideas on how I would take a COBOL calculation engine from
…[6 more quoted lines elided]…
› Anyone have any ideas?

There's a bunch of ways to do it. It depends on what you plan to do
with the returned values and who has to maintain it as to whether Java
or CGI is the most appropriate.

Assuming you want to get input from an end-user and display a result
then the easiest approach may be to port the calculator to the PC and
front-end it with a CGI application. (I'm guessing your web server is
on an NT machine since you mention DLLs and Realia.) Other than a bit
of HTML, and maybe some Javascript to enhance the basic HTML form, you
can do it all with COBOL.

One option is to port the calculator subroutine to the PC. The CGI
Agent is a COBOL program that parses the URL-encoded stream from the web
server, calls your calculator, then returns the result as an HTML
document.

Browser <--> Web Server <--> CGI Agent <--> calculator
(COBOL) (ported COBOL)

If the plan is to leave the application on the mainframe then you need
some sort of PC-to-Mainframe communications using either TCP/IP or some
LU6.2-based protocol. In this case the agent is a client/server
application which converses with a corresponding server application on
the mainframe which invokes your existing subroutine or transaction on
the mainframe.

Browser <--> Web Server <--> CGI Agent <---/---> Mainframe <--->
Existing
Server

Using Java may be appropriate if you already have TCP/IP on the
mainframe. The java application can converse directly with the
mainframe.


Karl Wagner
```

#### ↳ Re: COBOL engine that works with Domino

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4b90f8e4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`
- **References:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`

```

"Joel Berger" wrote:

› Anyone have any ideas on how I would take a COBOL calculation engine from
› the Mainframe and use it as a back-end calculator for a Web site. Would
…[7 more quoted lines elided]…
› 

Joel:

Flexus just released the freeware version of the COBOL Java Client.
You can download it from our web site at: http://www.flexus.com.
Before you download it, you should note that in order to use it, you
must have a COBOL compiler which supports the 32 bit Windows
environment.

In addition, you can also receive e-mail technical support on the
COBOL Java Client from flexus.

The COBOL Java Client is a set of libraries which allow you to write a
COBOL program for the server and display the screens within a
Java-enabled world wide web browser such as Netscape Navigator or
Internet Explorer. You write your entire program in COBOL with CALL
USING statements to invoke a server DLL which builds the screen to be
displayed in a Java enabled web browser. We provide you with a Java
applet which gets automatically downloaded and performs the functions
needed to build the screen on the client machine.

I'm not sure how the COBOL Java Client would work with Domino or
whether or not you would even need Domino. With the Java Client, your
COBOL program would reside on a Windows NT server. When the end user
wants to perform a calculation, the numbers would be entered into the
web browser fields which are created by your NT based COBOL program.
The end user would click on a pushbutton or press a control key and
the Java Client returns the numbers to your COBOL program residing on
the NT box.

Your COBOL program on the NT box simply acts as the middleware program
communicating the numbers and calculation method to the mainframe
COBOL program while receiving the reults from the mainframe
calculation engine. Once the result is returned, your NT based COBOL
program simply refreshes the fields in the web browser through a CALL
USING statement.

Yes, you can use it to write a calculator, but I would suggest writing
a calculator with enterable data fields for the numbers involved in
the calculation. You **really** don't want to try to have a
calculator similar to the Windows calculator. That would require
communication between the client machine and the web server **each**
time a numeric button is pressed in the web browser. Based on typical
internet connection speeds, it would take a home user with a 28,800
baud modem a long time to perform a simple calculation.

Instead of clogging up the newsgroup with a bunch of commercial junk,
I would simply ask anyone who is interested in the COBOL Java Client
to send an e-mail to me and I'll provide them with much more detailed
information via e-mail, mail, fax or carrier pigeon if you prefer!!

Thanks!! And be sure to remove the "-at-spammers-are-meat-heads-"
from my e-mail reply address. Also change the "-dot-" to a real "."
That's a "point," a "period" or a "full stop" or whatever you want to
call it today!!



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: COBOL engine that works with Domino

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb4b90f8e4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`
- **References:** `<6es6qh$b5o$1@newsbell.bellglobal.com>`

```

Joal,

There are a number of ways of doing this. Micro Focus' NetExpress product
has
web facilities specifically designed for tackling these sort of
requirements. Can
I suggest you contact one of our offices and they will be happy to take you
through
all the options.

Micro Focus (California)
(800) 872-6265

Micro Focus (Philadelphia)
(610) 263-3400

Micro Focus (New York)
(212) 312-2200

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus UK.

Joel Berger wrote in message <6es6qh$b5o$1.··.@new··l.com>...
› Anyone have any ideas on how I would take a COBOL calculation engine from
› the Mainframe and use it as a back-end calculator for a Web site. Would
…[7 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
