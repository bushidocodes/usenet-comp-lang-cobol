[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Cobol / using Windows "Start in" property

_10 messages · 6 participants · 2003-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Cobol / using Windows "Start in" property

- **From:** mr.kyle@prodigy.net (Mr. Kyle)
- **Date:** 2003-09-26T08:59:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```
I've been searching manuals, web pages and adtools.com for a way to
use Window's desktop property "start in" to pass my initial file
directory location to my application.  Can't find a thing about it and
I'm guessing it can't be done (or it's right under my nose and I can't
see it).

Has anybody done this?

Thanks.  Kyle
```

#### ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-09-26T17:13:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```

Mr. Kyle <mr.kyle@prodigy.net> wrote in message news:dcb682e3.0309260759.5f266a77@posting.google.com...
> I've been searching manuals, web pages and adtools.com for a way to
> use Window's desktop property "start in" to pass my initial file
…[6 more quoted lines elided]…
> Thanks.  Kyle


Have you created a Desktop shortcut to your executable?

If so, what exactly do you not understand?
```

##### ↳ ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** mr.kyle@prodigy.net (Mr. Kyle)
- **Date:** 2003-09-26T15:18:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcb682e3.0309261418.714eb48d@posting.google.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com> <Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message news:<Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net>...
> Mr. Kyle <mr.kyle@prodigy.net> wrote in message news:dcb682e3.0309260759.5f266a77@posting.google.com...
> > I've been searching manuals, web pages and adtools.com for a way to
…[12 more quoted lines elided]…
> If so, what exactly do you not understand?

Yes, I have the Desktop shortcut and can execute the application okay.
 Within the shortcut's properties, is a "Start in" value that, in
other Windows applications, allows a file sub-directory to be
established and passed to the application.  I want to know how the
receive that "start in" value in my application.
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-09-26T22:59:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ww3db.160212$3o3.11458506@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com> <Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net> <dcb682e3.0309261418.714eb48d@posting.google.com>`

```

Mr. Kyle <mr.kyle@prodigy.net> wrote in message news:dcb682e3.0309261418.714eb48d@posting.google.com...
> "Hugh Candlin" <no@spam.com> wrote in message news:<Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net>...
> > Mr. Kyle <mr.kyle@prodigy.net> wrote in message news:dcb682e3.0309260759.5f266a77@posting.google.com...
…[18 more quoted lines elided]…
> receive that "start in" value in my application.

This might give you an idea

http://www.pacificdb.com.au/MVP/Code/CreateShortcut.htm
```

###### ↳ ↳ ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-27T00:35:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7h9nvg3seqdtc7oeo01re4fplua18ilfe@4ax.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com> <Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net> <dcb682e3.0309261418.714eb48d@posting.google.com>`

```
On 26 Sep 2003 15:18:12 -0700, mr.kyle@prodigy.net (Mr. Kyle) wrote:

>"Hugh Candlin" <no@spam.com> wrote in message news:<Xs_cb.153990$0v4.11492191@bgtnsc04-news.ops.worldnet.att.net>...
>> Mr. Kyle <mr.kyle@prodigy.net> wrote in message news:dcb682e3.0309260759.5f266a77@posting.google.com...
…[19 more quoted lines elided]…
>receive that "start in" value in my application.
The "start in" value just means that before the application is started
the OS is going to issue a "change dir" to that particular directory.

So you just need to get the "current directory" as of the start of
your app.

Using the CBL routines

 ENVIRONMENT     DIVISION.
 DATA            DIVISION.
 WORKING-STORAGE SECTION.
 01 path-name PIC X(200).
 01 path-name-length PIC 9(4) BINARY value 200.
 01 status-code PIC S9(4) COMP-5.
 01 drive PIC X.
 01 path1 pic x(203).
 PROCEDURE       DIVISION.
     CALL "PC_READ_DRIVE"
     USING drive
     RETURNING status-code.
     CALL "CBL_READ_DIR"
      USING path-name
      path-name-length

      RETURNING status-code.
      move spaces to path1.
      string drive ":\"
             path-name delimited by size
             into path1.
      Display "Start path = " path1.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-26T18:07:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<byadnev6gN0GW-miU-KYgA@giganews.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```
Mr. Kyle wrote:
> I've been searching manuals, web pages and adtools.com for a way to
> use Window's desktop property "start in" to pass my initial file
…[6 more quoted lines elided]…
> Thanks.  Kyle

Sure, we do it all the time.

In PowerCOBOL it's a property of POW-SELF (CommandLine).

In COBOL97, from one of FJ's samples:

---- begin

 IDENTIFICATION DIVISION.
 PROGRAM-ID. commandline.

 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SPECIAL-NAMES.
     console is crt
     ARGUMENT-NUMBER   IS COMMAND-LINE-NUMBER
     ARGUMENT-VALUE    IS COMMAND-LINE-VALUE.

 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01 number-of-arguments   pic 99    value 0.
 01  command-line-arguments.
  05 a-command-line-argument pic x(80) occurs 1 to 99 depending on
number-of-arguments.
 01 arg-no       pic 99    value 0.
 01 line-no      pic 999   comp  value 3.
 01 output-line     pic x(80).

 PROCEDURE DIVISION.
   display spaces upon crt.
*
* Get the number of arguments passed to the program
*
  accept number-of-arguments from command-line-number
  move spaces to output-line
  string number-of-arguments delimited by size
      " Arguments were passed to this program" delimited by size
   into output-line

  display output-line at 0101
*
* Now, let's show the arguments to the user
*
  display " ".

  perform varying arg-no from 1 by 1 until arg-no > number-of-arguments
   accept a-command-line-argument (arg-no) from command-line-value
   move spaces to output-line
   string "Argument Number " delimited by size
        arg-no delimited by size
        " = " delimited by size
        a-command-line-argument (arg-no) delimited by size
    into output-line
   display output-line at line line-no column 1
   add 1 to line-no
  end-perform.
```

#### ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-26T16:16:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309261516.52efae4e@posting.google.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```
mr.kyle@prodigy.net (Mr. Kyle) wrote

> I've been searching manuals, web pages and adtools.com for a way to
> use Window's desktop property "start in" to pass my initial file
> directory location to my application.  Can't find a thing about it and
> I'm guessing it can't be done (or it's right under my nose and I can't
> see it).

The 'start in' directory is simply the directory that will be made
'current' _before_ your program is started.  It is not 'passed' to
your program.  The equivalent DOS commands are:

      cd startdirectory
      yourprog parameters
```

#### ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-26T16:28:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309261528.68fdfd1@posting.google.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```
mr.kyle@prodigy.net (Mr. Kyle) wrote

> I've been searching manuals, web pages and adtools.com for a way to
> use Window's desktop property "start in" to pass my initial file
> directory location to my application.  Can't find a thing about it and
> I'm guessing it can't be done (or it's right under my nose and I can't
> see it).

If you want to know where this has placed you then get the current directory with 
   
     CALL "GetCurrentDirectoryA" USING ..

See samples on Fujitsu site 'GETDIR.ZIP'.

or:
     CALL "CBL_READ_DIR" USING ...

See samples on Fujitsu site for CBL routines.
```

##### ↳ ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** mr.kyle@prodigy.net (Mr. Kyle)
- **Date:** 2003-09-29T11:52:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcb682e3.0309291052.1c4ed75d@posting.google.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com> <217e491a.0309261528.68fdfd1@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0309261528.68fdfd1@posting.google.com>...
> mr.kyle@prodigy.net (Mr. Kyle) wrote
> 
…[14 more quoted lines elided]…
> 
Thanks Richard - I don't think I mentioned I was trying to do this
with PowerCOBOL.  Learned a bit about linking here.  I couldn't figure
out how to use WINLINK in PowerCOBOL for GetCurrentDirectory, but the
"CBL_READ_DIR" worked out fine.  Didn't know the "Start in" set the
current directory either.
My thanks to all who posted responses.


> See samples on Fujitsu site for CBL routines.
```

#### ↳ Re: Fujitsu Cobol / using Windows "Start in" property

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-09-26T18:20:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0309261550.6fd4d7b6@posting.google.com>`
- **References:** `<dcb682e3.0309260759.5f266a77@posting.google.com>`

```
01  Directory-name pic X(255).
01  Directory-Length Pic S9(4) comp-5 value 255.

CALL "GetCurrentDirectory" with STDCALL using by value
Directory-length by reference Directory-Name

mr.kyle@prodigy.net (Mr. Kyle) wrote in message news:<dcb682e3.0309260759.5f266a77@posting.google.com>...
> I've been searching manuals, web pages and adtools.com for a way to
> use Window's desktop property "start in" to pass my initial file
…[6 more quoted lines elided]…
> Thanks.  Kyle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
