[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL with Java

_4 messages · 4 participants · 1999-02_

---

### COBOL with Java

- **From:** rkumar@msi.com.au (Ram Kumar )
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c8b0f3.2340188763@news.ozemail.com.au>`

```
Hi,

We are writing a java application for S390.
We would like to make the java application
call an existing batch cobol application on S390.
We would also like the cobol application call the java
application. We know that the java application
can be run under the unix services of S390.

But what we do not know is how to make COBOL
and Java applications communicate with each other
on S390. Any suggestions will be highly appreciated.

Many thanks

Regards

Ram
```

#### ↳ Re: COBOL with Java

- **From:** "David Sanders" <dsanders@synkronix.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c9b5d5$0$205@nntp1.ba.best.com>`
- **References:** `<36c8b0f3.2340188763@news.ozemail.com.au>`

```
Check out www.synkronix.com

David Sanders
Synkronix, Inc.
```

#### ↳ Re: COBOL with Java

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c8b873.87915758@news1.ibm.net>`
- **References:** `<36c8b0f3.2340188763@news.ozemail.com.au>`

```
On Mon, 15 Feb 1999 23:45:46 GMT, rkumar@msi.com.au (Ram Kumar )
wrote:

>Hi,
>
…[10 more quoted lines elided]…
>


I think Bob Wolfe at Flexus might be able to answer this one.  They
have a JAVA client that they wrote that communicates with a COBOL
program.
```

##### ↳ ↳ Re: COBOL with Java

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cad046.3316378@news.enter.net>`
- **References:** `<36c8b0f3.2340188763@news.ozemail.com.au> <36c8b873.87915758@news1.ibm.net>`

```
redsky@ibm.net (Thane Hubbell) wrote:

>On Mon, 15 Feb 1999 23:45:46 GMT, rkumar@msi.com.au (Ram Kumar )
>wrote:
…[18 more quoted lines elided]…
>program.  

Thane's correct.  We have written a compiled Java applet which gets
downloaded to a Web browser and dynamically builds interactive user
interface screens based upon instructions from a COBOL application.

The only problem is that we wrote it to work on a Windows NT web
server, not a UNIX box.

Essentially we implemented our Java Client as follows:

COBOL Application on Server CALLs a server based subroutine and passes
data through a standard CALL USING statement.  The data consists of a
function parameter and a data parameter (both expressed as COBOL WS
variables)

The server based subroutine sends the data block across TCP/IP through
a standard socket connection.

The Java Applet which was downloaded to the web browser then retrieves
the data block into a standard Java data structure and uses the
function parameter and data parameter as instruction codes to
dynamically construct data fields in a web browser.

When the end user completes the data entry session, the Java applet
simply returns the data in the reverse fashion in which it retrieved
the data.

BUT!!!!!!!!!!

<soapbox>

If the original poster is considering a standalone Java applet on the
client, that is one thing, but if he/she is considering using a web
browser based client for the user interface screens, I hope that they
think long and hard about it.

We really do not push the Java Client solution, because we have found
that a Thin Client based COBOL application is much cleaner, much more
easy to maintain, offers much better performance and offers better
user interface features.

</soapbox>

Hope this was helpful.



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
