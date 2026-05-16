[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rm/cobol under sco openserver 5.0.4

_2 messages · 2 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### rm/cobol under sco openserver 5.0.4

- **From:** Dave Trausch <aceco@ginetworks.com>
- **Date:** 1999-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F57842.51896536@ginetworks.com>`

```
os = SCO Openserver Rel. 5.0.4
compiler version = Liant rm/cobol

What I need is a little script that will run on top of existing compiled

scripts.  Basically I want the script to be able to enter data out of a
comma
delimited ascii (or .dbf) file.  The script would enter the data as so:

 existing function                            wanna-be script function

1. Enter Part Number                    123456789
2. Enter Cross Reference               987654321
3. Weight                                       12 kilos
4. Price                                           20,000

and so on.

What I'm trying to do is take price listings out of manufacturer price
lists
in .dbf form and plug them into fields in a cobol compiled database.

I don't want free custom programming, but what I do want is some
guidance
into how to accomplish this.  I know it's probably not difficult (wait,
enter,
wait, enter).  Really, if this sounds absolutely retarded, I apologize
in
advance.
Thank you!

Dave Trausch
dave@appliedcontrols.net
```

#### ↳ Re: rm/cobol under sco openserver 5.0.4

- **From:** Albert Ratzlaff <albert@conexion.com.py>
- **Date:** 1999-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F6185A.396BA5D6@conexion.com.py>`
- **References:** `<36F57842.51896536@ginetworks.com>`

```
Dave Trausch wrote:

> os = SCO Openserver Rel. 5.0.4
> compiler version = Liant rm/cobol
…[30 more quoted lines elided]…
> dave@appliedcontrols.net

Easy (if I understand your problem right).

"runcobol program < datafile"

If you need extra "confirm operation" answers, beside the actual data items,
it also can be done - just a little more complicated.

Regards
Albert Ratzlaff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
