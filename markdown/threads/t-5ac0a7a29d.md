[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cariage return line feed

_5 messages · 4 participants · 1999-08_

---

### Cariage return line feed

- **From:** yatno@my-deja.com
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7oqhj0$8ok$1@nnrp1.deja.com>`

```
I am using COBOL/400 standard (not ILE) in AS400
what i need is how to fill Cariage return line feed (break page) in
working-storage value.
i am trying using alt+012 and alt+014, it doesn`t work  :-)



Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: Cariage return line feed

- **From:** docdwarf@clark.net ()
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G26s3.157$km4.8884@iad-read.news.verio.net>`
- **References:** `<7oqhj0$8ok$1@nnrp1.deja.com>`

```
In article <7oqhj0$8ok$1@nnrp1.deja.com>,  <yatno@my-deja.com> wrote:
>I am using COBOL/400 standard (not ILE) in AS400
>what i need is how to fill Cariage return line feed (break page) in
>working-storage value.
>i am trying using alt+012 and alt+014, it doesn`t work  :-)

01  WS-CRLF.
    05  WS-CRLF-CR PIC X VALUE X'0D'.
    05  WS-CRLF-LF PIC X VALUE X'0A'.

DD
```

#### ↳ Re: Cariage return line feed

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37b180eb@eeyore.callnetuk.com>`
- **References:** `<7oqhj0$8ok$1@nnrp1.deja.com>`

```

yatno@my-deja.com wrote in message <7oqhj0$8ok$1@nnrp1.deja.com>...
>I am using COBOL/400 standard (not ILE) in AS400
>what i need is how to fill Cariage return line feed (break page) in
>working-storage value.
>i am trying using alt+012 and alt+014, it doesn`t work  :-)
>

Try this:
01   HexCR        pic xx value x'0D0A'.

If the AS400 compiler wont accept a hex literal try this:

01  NumericCR  pic s9(4) binary value 3338.
01 NumCR  redefines NumericCR pic xx.

You can then use NumCR or HexCR in STRING statements to cause a carriage
return.

like this:

move spaces to message-text
string
   'This is a message....'
           delimited by size
   HexCR
           delimited by size
  'This is line 2 of the same message...'
           delimited by size
                 into message-text
end-string

Hope this helps,

Pete.



>
>
>Sent via Deja.com http://www.deja.com/
>Share what you know. Learn what you don't.
```

#### ↳ Re: Cariage return line feed

- **From:** "Jonathan Roberts" <zimboon @ hotmail . com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37b1d947$0$19549@fountain.mindlink.net>`
- **References:** `<7oqhj0$8ok$1@nnrp1.deja.com>`

```
I usually make a 78 level for these.

78  const-lf      value X'0A'.
78  const-cr    value X'0D'.

RBA.

> I am using COBOL/400 standard (not ILE) in AS400
> what i need is how to fill Cariage return line feed (break page) in
…[6 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: Cariage return line feed

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7osm5b$hbe@dfw-ixnews10.ix.netcom.com>`
- **References:** `<7oqhj0$8ok$1@nnrp1.deja.com> <37b1d947$0$19549@fountain.mindlink.net>`

```
EXTENSION ALERT (suggestion does not match the question's compiler)

The original question talked about COBOL/400.  The answer uses a level-78.
These two items do NOT match (unless COBOL/400 has had a change that I don't
know about).

You can use a 77-level in COBOL/400 (or any other "conforming" compiler) -
and you can "use it" as a constant - even if that isn't what it is required
to be.  (Then again, you can use an 01-level, or an 02 thru 49-level as a
constant.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
