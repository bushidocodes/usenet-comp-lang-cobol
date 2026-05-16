[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCobol - launch simple data entry app within a browser?

_4 messages · 4 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### AcuCobol - launch simple data entry app within a browser?

- **From:** rghcomputg@aol.com (Rghcomputg)
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981128182032.07074.00002049@ng-fu1.aol.com>`

```
Greetings:

What is required to launch a simple data entry app within a browser? Initially,
this app would serve in an intranet, but ideally also on the internet. Are
there coding issues for IE vs Netscape?
```

#### ↳ Re: AcuCobol - launch simple data entry app within a browser?

- **From:** mattr@mentis.com.au
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73t362$8r5$1@nnrp1.dejanews.com>`
- **References:** `<19981128182032.07074.00002049@ng-fu1.aol.com>`

```
In article <19981128182032.07074.00002049@ng-fu1.aol.com>,
  rghcomputg@aol.com (Rghcomputg) wrote:
> Greetings:
>
> What is required to launch a simple data entry app within a browser?
Initially,
> this app would serve in an intranet, but ideally also on the internet. Are
> there coding issues for IE vs Netscape?
>

Probably the most robust method would be using the AcuCobol-GT Web-Plugin,
maybe add AcuServer when you go Internet.  There aren't any worries about
whether it's Netscape or IE, everything inside the program is controlled by
the runtime.

If you were going to use CGI (built into AcuCobol-GT 4.0), the only IE vs
Netscape issues will be HTML formating.

AcuCorp has a book called The Programmers Guide to the Internet, which you
might find useful.

Matt Robinson
Support Consultant, Mentis Technologies
---------------------------------------
<insert something witty here>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: AcuCobol - launch simple data entry app within a browser?

- **From:** "David Sanders" <dsanders@synkronix.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3662ef6c$0$220@nntp1.ba.best.com>`
- **References:** `<19981128182032.07074.00002049@ng-fu1.aol.com>`

```
Use PERCobol (www.synkronix.com), your code will generally run "as is" on
the net.  (No plug-in needed..)

David



Rghcomputg wrote in message
<19981128182032.07074.00002049@ng-fu1.aol.com>...
>Greetings:
>
>What is required to launch a simple data entry app within a browser?
Initially,
>this app would serve in an intranet, but ideally also on the internet. Are
>there coding issues for IE vs Netscape?
>
>
>
```

##### ↳ ↳ Re: AcuCobol - launch simple data entry app within a browser?

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36630e14.0@news1.ibm.net>`
- **References:** `<19981128182032.07074.00002049@ng-fu1.aol.com> <3662ef6c$0$220@nntp1.ba.best.com>`

```
>Rghcomputg wrote in message
><19981128182032.07074.00002049@ng-fu1.aol.com>...
…[3 more quoted lines elided]…
>>there coding issues for IE vs Netscape?


yes, there are some IE/Netscape issues. But with AOL's recent purchase
of Netscape and its decision to keep IE as its main browser, the
IE/Netscape issues may go away shortly as IE finally wins. I'm no
Micro$oft fan, but IE has since version 3.0 been the better browser
(faster, less buggy, more standards compliant, free, etc).


If you want to get a feeling for what a browser interface to a simple
data-entry program looks like and to see what kind of HTML could
be generated, go to http://www.etk.com and download the
"Web interface in 30 seconds"  fully functioning demo that
will take one of your file layouts (copybook) and generate
the browser/data-entry program automatically.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
