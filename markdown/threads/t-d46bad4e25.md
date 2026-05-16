[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

_9 messages · 8 participants · 1999-04 → 1999-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** "DEDALO S.a.s." <dedalo@mtrade.com>
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it>`

```
Dear friends,
i ask you for this questions?

I have a sequential file created in Cobol2 on IBM Mainframe platform, this
file has PIC S9(9) fileds, i transfer it with IND$FILE command on Microsoft
NT Server machine with ASCII conversion options,
this file transferred are read by a Cobol program on NT that dumping
reading this s9(9) field - "Not numeric"!!!!!.
Where is the problem?
Is a transfer problem o is a conversion error To Charset EBCDIC-ASCII?.
Help Me!!!!!!!!!!!!!!!

Thank you all!!!
Bye Gianluca
```

#### ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** pitchl@tdbank.ca (Lew Pitcher)
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371f1c58.5521064@news21.bellglobal.com>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it>`

```
On Thu, 22 Apr 1999 14:03:54 +0200, "DEDALO S.a.s."
<dedalo@mtrade.com> wrote:

>Dear friends,
>i ask you for this questions?
…[8 more quoted lines elided]…
>Help Me!!!!!!!!!!!!!!!


Many COBOL formats are neither ASCII nor EBCDIC. If the field is
defined as USAGE IS DISPLAY, then characterset conversion may be used,
otherwise you have to cope with binary and/or packed decimal numbers
which cannot be altered by characterset conversion.

Additionally, NT natively interprets binary numbers differently from
the interpretation IBM mainframes use. Look up "big endian", "little
endian", and "endianness" before you do anything. NT doesn't have
native support for COMP-3 (PACKED DECIMAL) numbers at all, so you'll
have to accomodate that as well.

You don't say what tool will use the file on the NT platform; if you
are processing the file through a COBOL program on NT, there is a good
chance that the COBOL program can be written and/or compiled to a
mainframe compatability mode, which will process the data correctly.

Otherwise, the simplest way to fix the problem is to get the mainframe
file regenerated without the binary/packed fields, either by dropping
that data, or by converting it to DISPLAY prior to writing it to file.
This would permit EBCDIC-to-ASCII conversion to work properly (such as
it is), and should give you a better looking file. Remember,
characterset conversion is incomplete (there are characters in EBCDIC
that don't exist in ASCII, and vice-versa), so even with changes like
these, you still may wind up with an unreadable file.



Lew Pitcher
System Consultant, Development Services
Toronto Dominion Bank

(Opinions expressed are my own, not my employers')
```

#### ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371F27E9.16C0A471@zip.com.au>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it>`

```
DEDALO S.a.s. wrote:
> 
> Dear friends,
…[12 more quoted lines elided]…
> Bye Gianluca

EBCDIC x'F0'  becomes a } on the PC, etc after ascii ebcdic
translation.

Make your signs separate -9(9) and download that.

Ken
```

##### ↳ ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3732c4ec.24274044@news.netvision.net.il>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it> <371F27E9.16C0A471@zip.com.au>`

```
On Thu, 22 Apr 1999 23:45:13 +1000 Ken Foskey <waratah@zip.com.au> wrote:

:>> Dear friends,
:>> i ask you for this questions?
 
:>> I have a sequential file created in Cobol2 on IBM Mainframe platform, this
:>> file has PIC S9(9) fileds, i transfer it with IND$FILE command on Microsoft
:>> NT Server machine with ASCII conversion options,
:>> this file transferred are read by a Cobol program on NT that dumping
:>> reading this s9(9) field - "Not numeric"!!!!!.
:>> Where is the problem?
:>> Is a transfer problem o is a conversion error To Charset EBCDIC-ASCII?.
:>> Help Me!!!!!!!!!!!!!!!
 
:>> Thank you all!!!
:>> Bye Gianluca

:>EBCDIC x'F0'  becomes a } on the PC, etc after ascii ebcdic
:>translation.

No, it does not.

x'F0' is a character zero.

The issue probably is that the last digit of the number is signed so that
instead of being 0-9 (x'F0'-x'F9') is x'C0'-X'C9' for positive numbers (first
unprintable, rest being A-I) or x'D0'-x'D9' for negative numbers (first
unprintable, rest being J-R).

You can probably write a routine to edit the numbers. If the last digit is
A-I, you can safely convert to 1-9 and know the number is positive. If the
last digit is J-R you can safely convert to 1-9 and know the number is
negative. Some research will be required to determine what x'C0' and x'D0'
look like when downloaded in ASCII.

:>Make your signs separate -9(9) and download that.

A good approach if you can massage the data on the mainframe.
```

#### ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** "Paul Tabour" <ptabour@worldnet.att.net>
- **Date:** 1999-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7guqjq$a1k$1@bgtnsc03.worldnet.att.net>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it>`

```
Hello all --

I also have a file conversion issue from MVS to WinNT.  My issue involves a
file with multiple record layouts containing binary and COMP-3 data.  I
would like to avoid massaging the data on the mainframe, so this is what I
would like to do: bring the file down without translation, and use some
utility to read it in.

I found one called FilePort, from a company called SyncSort; this product
takes the file and a COBOL copybook and knows how to convert it to ASCII.
The catch?  It only runs on UNIX right now.

My question is this: do any of you know of a product that does a similar
thing for NT?  Even if it doesn't take copybooks, I'd appreciate information
about any utility that can handle binary and COMP-3 fields and multiple
record layouts.

Thanks,
Paul
ptabour@worldnet.att.net
```

##### ↳ ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-lpb0mf0uTJ3U@Dwight_Miller.iix.com>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it> <7guqjq$a1k$1@bgtnsc03.worldnet.att.net>`

```
On Fri, 7 May 1999 13:39:54, "Paul Tabour" <ptabour@worldnet.att.net> 
wrote:

> Hello all --
>> My question is this: do any of you know of a product that does a 
similar
> thing for NT?  Even if it doesn't take copybooks, I'd appreciate information
> about any utility that can handle binary and COMP-3 fields and multiple
> record layouts.

If you use a MicroFocus product, such as NetExpress there is a tool 
called WFL.  

With this, you transfer your file using BINARY, so that no 
EBCDIC/ASCII conversion is performed, then you run it through the WFL 
(You can even write a program that calls it, so it is not a manual 
process).  With WFL you define the "Profile" and the "Mask".  The 
"Mask" can be generated for you from the FD.  This mask is then used 
for the conversion.  I used this extensively and have seen no better 
product for the task.  It is fast and accurate.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** "Paul Tabour" <ptabour@worldnet.att.net>
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h6rtk$o4k$1@bgtnsc03.worldnet.att.net>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it> <7guqjq$a1k$1@bgtnsc03.worldnet.att.net> <Jl0PnHJ5PvPd-pn2-lpb0mf0uTJ3U@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote in message ...
>On Fri, 7 May 1999 13:39:54, "Paul Tabour" <ptabour@worldnet.att.net>
>wrote:
…[4 more quoted lines elided]…
>> thing for NT?  Even if it doesn't take copybooks, I'd appreciate
information
>> about any utility that can handle binary and COMP-3 fields and multiple
>> record layouts.
>
>If you use a MicroFocus product, such as NetExpress there is a tool
>called WFL.


Thanks for your idea.  Unfortunately, we are not using a Microfocus
product -- our platform is Netscape Application Server running on WinNT.  I
don't have the flexibility to change application servers (or add other
large-ticket products to the platform), so apparently WFL is not an option
for me.

Any other ideas?  Thanks for helping me out.

Paul Tabour
ptabour@worldnet.att.net
```

##### ↳ ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help Me!!!!!!!!!!

- **From:** Laura Sabourin <laura@ragdolls.net>
- **Date:** 1999-05-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3734789F.170A3E97@ragdolls.net>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it> <7guqjq$a1k$1@bgtnsc03.worldnet.att.net>`

```
Did anyone reply to this ? I have a similar problem but we don't even have the
code from the COBOL systems which has produced the files which we would like to
use to populate an ACCESS database. Anyone know of a PC/DOS based file dump that
I could use to figure out the file out ?

Paul Tabour wrote:

> Hello all --
>
…[17 more quoted lines elided]…
> ptabour@worldnet.att.net
```

##### ↳ ↳ Re: File conversion from IBM Mainframe to Windows NT platform!!!Help

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3737299d.23484551@news.enter.net>`
- **References:** `<7fn2q3$6um$1@fe2.cs.interbusiness.it> <7guqjq$a1k$1@bgtnsc03.worldnet.att.net>`

```
Laura Sabourin <laura@ragdolls.net> wrote:

>Did anyone reply to this ? I have a similar problem but we don't even have the
>code from the COBOL systems which has produced the files which we would like to
>use to populate an ACCESS database. Anyone know of a PC/DOS based file dump that
>I could use to figure out the file out ?

Laura:

Please forgive me for holding my nose while providing this advice, but
it is very important for me to be completely honest with you.

"Hode on dow whide I grab by node"  ;-)

Ok...the answer you seek might be found at:

http://www.datajunction.com/

Data Junction has tools to extract data from various types of COBOL
files and automatically convert them to other files types (such as
Microsoft Axes Files).

Before you go out and buy a copy of Data Junction, you should also be
aware of the following:

A.  It is highly likely that you will need to know the record layout;
and

B.  I also suspect that you will need to know the specific compiler
which was used to compile the COBOL program which you have been using
to date.

...and now for the reason I hold my nose...

Unless you have somewhat "smallish" file sizes, I suspect that you
will not be happy using Access considering that you came from COBOL.
I know that this may sound completely backwards, but if you do have
large files or do a tremendous amount of file I/O, going from COBOL to
Access is kind of like trading in your Ferrari for a 1965 Plymouth
Valiant.

(my own humble opinion)





>
>Paul Tabour wrote:
…[21 more quoted lines elided]…
>

Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
