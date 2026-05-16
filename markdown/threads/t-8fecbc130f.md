[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# multiple tape volumes in Jcl

_7 messages · 5 participants · 2001-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### multiple tape volumes in Jcl

- **From:** jayam@odin.pdx.edu (Karthik)
- **Date:** 2001-09-06T13:37:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<527408ca.0109061237.4e27861@posting.google.com>`

```
This is C&P from my JCL
//           UNIT=TAPE,                                        
//  VOL=SER=(064098,064257,064318,064478,064521,064620,064670) 

I need to add more vol sers and i am not sure how to continue in the next line.

Any help forthcoming would be appreciated.
```

#### ↳ Re: multiple tape volumes in Jcl

- **From:** "Al Shannon" <shannon@allover.com>
- **Date:** 2001-09-06T14:26:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BSRl7.1$RC.4822@news.sjc.globix.net>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com>`

```
The OS/390 manuals are available online from IBM.  Try
 http://www-1.ibm.com/servers/s390/os390/bkserv/
and look for the JCL reference for the version of OS/390 or MVS you are
using.
Good luck.
Al...
"Karthik" <jayam@odin.pdx.edu> wrote in message
news:527408ca.0109061237.4e27861@posting.google.com...
> This is C&P from my JCL
> //           UNIT=TAPE,
> //  VOL=SER=(064098,064257,064318,064478,064521,064620,064670)
>
> I need to add more vol sers and i am not sure how to continue in the next
line.
>
> Any help forthcoming would be appreciated.
```

#### ↳ Re: multiple tape volumes in Jcl

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-09-06T21:28:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iURl7.7098$4z.31687@www.newsranger.com>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com>`

```
Hi Jay,

You can try this: keep coding to col 71. Don't put anything in 72. create the
next card wih // in 1-2 and the next character in your 
string in col 16. E.g:
//xxx vol=ser=(999999,999999,999999,99
//             9999,999999)

Let me know how you made out.

Jack
In article <527408ca.0109061237.4e27861@posting.google.com>, Karthik says...
>
>This is C&P from my JCL
…[5 more quoted lines elided]…
>Any help forthcoming would be appreciated.
```

##### ↳ ↳ Re: multiple tape volumes in Jcl

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-09-06T22:24:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pISl7.7179$4z.31952@www.newsranger.com>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com> <iURl7.7098$4z.31687@www.newsranger.com>`

```
No reason the split up the actual number on the volser - this works:

// VOL=SER=(202194,203539,203538,215426,215612,212176,215609,            
//          201916,223265,201919,201918,200209,201013)                   



In article <iURl7.7098$4z.31687@www.newsranger.com>, John H Sleight Jr says...
>
>Hi Jay,
…[20 more quoted lines elided]…
>
```

#### ↳ Re: multiple tape volumes in Jcl

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-09-07T03:15:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B983B18.E6E07E21@neo.rr.com>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com>`

```
Karthik wrote:
> 
> This is C&P from my JCL
…[5 more quoted lines elided]…
> Any help forthcoming would be appreciated.

//ddname dd disp=old,
//          unit=tape,
//          vol=ser=(064098,064257,064318,064478,
//          064521,064620,064670)

Three caveats:

1) JCL is expected to be UPPERCASE
2) The continued line must start with cc=4 but before cc=17
(cc= card column)
3) You may find that there is another parameter that must be
specified to use more than 10 volumes (I can't remember it
off the top of my head this late at night). It has been a
year or two since I've had to specify more than 4 volsers
for tape for one DD statement.
```

##### ↳ ↳ Re: multiple tape volumes in Jcl

- **From:** "Jayashree Karthik" <jayam@odin.pdx.edu>
- **Date:** 2001-09-07T07:01:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nak0r$k47$1@starbug.oit.pdx.edu>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com> <3B983B18.E6E07E21@neo.rr.com>`

```
I guess i didn't follow the rule that says contiuation must not begin after
cc 17th. It works now. Thanks for all ur tips.

"Steve Thompson" <sthompson_2@neo.rr.com> wrote in message
news:3B983B18.E6E07E21@neo.rr.com...
> Karthik wrote:
> >
…[4 more quoted lines elided]…
> > I need to add more vol sers and i am not sure how to continue in the
next line.
> >
> > Any help forthcoming would be appreciated.
…[20 more quoted lines elided]…
> 330/335-9907 office
```

#### ↳ Re: multiple tape volumes in Jcl

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-09-07T12:23:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010907082318.00533.00000394@mb-fk.aol.com>`
- **References:** `<527408ca.0109061237.4e27861@posting.google.com>`

```
Karthik,

I see you've already gotten answers to your query.

How about a JCL class [or Advanced JCL, where we discuss multi-volume data sets
among other things]?

Here's a link, see if would be of interest:

http://www.trainersfriend.com/B120descrpt.htm

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
