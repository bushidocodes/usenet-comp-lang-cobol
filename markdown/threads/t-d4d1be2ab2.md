[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Netexpress 3.0 and WWW

_5 messages · 3 participants · 2000-06_

---

### Netexpress 3.0 and WWW

- **From:** "Carlos Ruivo Ferreira" <carlos@mb2s.com>
- **Date:** 2000-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8i3kk3$g24$1@srvlis16.teleweb.pt>`

```
I have a simple program just to validate a number and a password. As I'am
not very good in english, this is the message from my ISP (i'am in Portugal
and my site is in USA) surprised ? you must see the prices for 100mb of web
space in my country...,
Thanks in advance for your time and  if you have any anwser for that problem
pls let me know
CArlos Ferreira
carlos@mb2s.com

Message from ISP:
Hello,
Your .exe script (cgi-bin/pcontrol_server.exe) is causing our perl.exe and
some other server components to crash. Please check out what is going on, if
this happened again I will need to suspend your CGI access.
Thank you for your cooperation.
-Uri Foox
CFM Web Hosting http://www.cfmwebhost.com

>REsponse
I don't understand what can be happening. Our .exe is a big one because it
has all dll�s and run-time stuff linked to it. The only thing that the
program does is to accept three fields from an input form (number, number
and password). Then it reads a sequential file to validate the information
and if everything is OK the file is closed and nothing more happens. If the
information is not correct, the program displays an output form with an
error message. Nothing more simple then this.
We use Merant Netexpress 3.0 and we have some complex applications running
in NT servers (in the web) and as far as I know nobody as ever complains. I
can upload the source program in our site if you want (I must advise you
that Netexpress is Cobol.and I don't know how old are you :-)
PS. we are not accessing our site since 16:30 (Portugal) 11:30 (New York)
For now we are only testing and nobody knows that mb2s.com exists (I think)
```

#### ↳ Re: Netexpress 3.0 and WWW

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-06-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1f51e4bc.a5f91ff7@usw-ex0103-018.remarq.com>`
- **References:** `<8i3kk3$g24$1@srvlis16.teleweb.pt>`

```
Carlos,

What is the folder structure of your web site. I have several
sites using COBOL cgi (NetExpress) and have had no problems, but
the web site has it's own cgi-bin folder. All of the sites run
on Windows NT.

Rich

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

##### ↳ ↳ Re: Netexpress 3.0 and WWW

- **From:** "Carlos Ruivo Ferreira" <carlos@mb2s.com>
- **Date:** 2000-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394d0a34@212.18.160.197>`
- **References:** `<8i3kk3$g24$1@srvlis16.teleweb.pt> <1f51e4bc.a5f91ff7@usw-ex0103-018.remarq.com>`

```
My web site as it's own cgi-bin folder with the right permissions. The
problem is that my ISP (CFM Web Host) says that everytime someone excutes my
cobol cgi program the server has problems. I don�t know what to do and they
want to cancel my permission to execute cgi.
Thanks for your time and concern

CArlos
carlos@mb2s.com

"Rich Rohde" <richNOriSPAM@richware.net.invalid> wrote in message
news:1f51e4bc.a5f91ff7@usw-ex0103-018.remarq.com...
> Carlos,
>
…[7 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

###### ↳ ↳ ↳ Re: Netexpress 3.0 and WWW

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<394D7371.1E6F9564@zip.com.au>`
- **References:** `<8i3kk3$g24$1@srvlis16.teleweb.pt> <1f51e4bc.a5f91ff7@usw-ex0103-018.remarq.com> <394d0a34@212.18.160.197>`

```
Carlos Ruivo Ferreira wrote:
> 
> My web site as it's own cgi-bin folder with the right permissions. The
…[3 more quoted lines elided]…
> Thanks for your time and concern

1.  Run yourself from the command line.  Does it work?

2.  Wrap another CGI around it, and just put a text header on top of
what you are sending, run that and try and understand the results?

3.  Ask you ISP what debugging options they have on their web server. 
There is often an option that will send messages back.  What about the
log files, what do they contain?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Netexpress 3.0 and WWW

- **From:** Rich Rohde <richNOriSPAM@richware.net.invalid>
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<05d39e55.cd17b665@usw-ex0102-084.remarq.com>`
- **References:** `<8i3kk3$g24$1@srvlis16.teleweb.pt> <1f51e4bc.a5f91ff7@usw-ex0103-018.remarq.com> <394d0a34@212.18.160.197>`

```
"Carlos Ruivo Ferreira" <carlos@mb2s.com> wrote:
>The
>problem is that my ISP (CFM Web Host) says that everytime
someone excutes my
>cobol cgi program the server has problems. I don�t know what to
do and they
>want to cancel my permission to execute cgi.

Have you thought of changing ISPs? If so, you may wish to
contact http://www.pcez.com. I use them for my COBOL apps
without any problems. Their number is (503) 639-0828 and ask for
Marcus (tell him I referred you, it won't buy you anything, but
at least he will understand your situation). Sorry for the
advertisment, but if they can help solve the problem, why not.

Regards,
Rich



Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
