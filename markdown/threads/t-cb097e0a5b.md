[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# vb.net and cobol.net - passing filenames

_2 messages · 2 participants · 2005-03_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### vb.net and cobol.net - passing filenames

- **From:** "ari" <unikoski@yahoo.com>
- **Date:** 2005-03-28T09:39:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1112031566.887938.40380@o13g2000cwo.googlegroups.com>`

```
I will need to transfer a number of mainframe cobol programs to a
windows environment (fujitsu cobol.net), and write a vb.net control
program to call them.

The cobol programs are called repeatedly for different files: the cobol
programs don't care, as they access the files using

"select input-file assign to infile"

where infile (on the mainframe) is a DDNAME and the physical filename
is a DSNNAME.

Under Micro-focus I could do this by setting an environment variable
setting DDNAME=DSNNAME and it works fine.

Is is possible to do the same here - i.e. have the VB.NET set
environment variables and the cobol program will use to get the
physical filename? Is there another option?

I noticed the post

http://groups-beta.google.com/group/comp.lang.cobol/browse_thread/thread/fa58209d23c06409/c0696c17c6069cd9?q=FILENAME+FUJITSU+COBOL+SELECT&rnum=12#c0696c17c6069cd9


that suggests this will work - but will I always be bothered by the
window popping up the post is asking about - or is is smart enough not
to open the window if it has all the environment variables it needs?

Unfortunately at the moment I don't yet have Fujistu so its hard for me
to make tests at the moment.

Thanks,
```

#### ↳ Re: vb.net and cobol.net - passing filenames

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-03-30T00:07:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3asunsF6cigirU1@individual.net>`
- **References:** `<1112031566.887938.40380@o13g2000cwo.googlegroups.com>`

```
You can assign  files to environment variables in the Fujitsu environment.

But a better way is to use the external Cobol85.cbr file which controls the
environment and also prevents the popups you mentioned.

The external 'environment file' has all the options you could want and can
be maintained with any text editor.

You could easily write this file from VB if you wanted to...

The manuals document the full use of the environment file. It is
comprehensive. Just use what you need; NONE of it is mandatory.

Pete.

TOP POST no more.
"ari" <unikoski@yahoo.com> wrote in message
news:1112031566.887938.40380@o13g2000cwo.googlegroups.com...
> I will need to transfer a number of mainframe cobol programs to a
> windows environment (fujitsu cobol.net), and write a vb.net control
…[19 more quoted lines elided]…
>
http://groups-beta.google.com/group/comp.lang.cobol/browse_thread/thread/fa58209d23c06409/c0696c17c6069cd9?q=FILENAME+FUJITSU+COBOL+SELECT&rnum=12#c0696c17c6069cd9
>
>
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
