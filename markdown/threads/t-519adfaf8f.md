[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Concat array elements into a string

_4 messages · 3 participants · 2007-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Concat array elements into a string

- **From:** charles.leviton@gmail.com
- **Date:** 2007-04-19T11:53:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com>`

```
Hi,
This seems straightforward but I can't seem to figure it out.
Basically, I have a table of elements and I want to string them all
together into a single text variable.

Here is the pseudocode

txtvar PIC X(30)
arrayvar [10]
do varying index from 1 by 1
    txtvar = Rtrim(txtvar) || arrayvar(index) where || represents a
concatenation operator
until index = 10

I tried something like this in COBOL

perform varying ws-counter from 1 by 1 until ws-counter = 10
    string  txtvar ',' arrayvar(ws-counter)
    delimited by size into txtvar
end-perform

But I just got spaces in txtvar at the end of it, presumably because I
don't have a trim function that I can use in COBOL (or is there one
that I just don't know of?)

I searched this forum and the web too on things like
"string array elements together" and didn't find anything useful.

Any ideas?
```

#### ↳ Re: Concat array elements into a string

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-04-19T15:27:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UJWdndPIKrUTX7rbnZ2dnUVZ_j6dnZ2d@golden.net>`
- **In-Reply-To:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com>`
- **References:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com>`

```
charles.leviton@gmail.com wrote:
> Hi,
> This seems straightforward but I can't seem to figure it out.
…[27 more quoted lines elided]…
> 
   move space to txtvar.
 > perform varying ws-counter from 1 by 1 until ws-counter = 10
 >     string  txtvar delimited by space (or size)
       ',' delimited by size
       arrayvar(ws-counter) delimited by size
 >        into txtvar
 > end-perform

Donald
```

#### ↳ Re: Concat array elements into a string

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-04-19T13:06:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177013205.810156.226190@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com>`
- **References:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com>`

```
On Apr 20, 6:53 am, charles.levi...@gmail.com wrote:
> Hi,
> This seems straightforward but I can't seem to figure it out.
…[24 more quoted lines elided]…
> "string array elements together" and didn't find anything useful.

When you use 'delimited by size' then you are telling it to use the
size of the variable, ie 30 characters or whatever arrayvar is. You
need to use a delimiting character or perhaps "  " (two spaces. You
also need to look at the 'with pointer' clause which specifies where
the string is to start.

You need to space fill the output first. Set the pointer to 1.
I upper cased the added parts.  Note I removed txtvar from the string
input list.  Txtpoint will be updated by each string to give
concatenation.

  MOVE SPACES TO TXTVAR
  MOVE 1  TO TXTPOINT
  perform varying ws-counter from 1 by 1 until ws-counter = 10
        IF ( WS-COUNTER > 1 )
              STRING "," DELIMITED BY SIZE
                    INTO TXTVAR WITH POINTER TXTPOINT
        END-IF
        string arrayvar(ws-counter) delimited by "  "
            into txtvar WITH POINTER TXTPOINT
  end-perform
```

##### ↳ ↳ Re: Concat array elements into a string

- **From:** charles.leviton@gmail.com
- **Date:** 2007-04-19T14:00:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1177016415.332526.40100@o5g2000hsb.googlegroups.com>`
- **In-Reply-To:** `<1177013205.810156.226190@o5g2000hsb.googlegroups.com>`
- **References:** `<1177008787.610865.322920@y80g2000hsf.googlegroups.com> <1177013205.810156.226190@o5g2000hsb.googlegroups.com>`

```
On Apr 19, 4:06 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Apr 20, 6:53 am, charles.levi...@gmail.com wrote:
>
>
>

> When you use 'delimited by size' then you are telling it to use the
> size of the variable, ie 30 characters or whatever arrayvar is. You
…[18 more quoted lines elided]…
>   end-perform

Thank you both.  Especially for the addnl logic to avoid the leading
comma.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
