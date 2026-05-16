[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ?How to execute a DOS command in MicroFocus Anim.V2??

_3 messages · 3 participants · 2000-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### ?How to execute a DOS command in MicroFocus Anim.V2??

- **From:** "Dirt" <dirt@vh.net>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89u4ge0red@enews4.newsguy.com>`

```
Does anyone know how to execute a DOS command in MF Animator version 2? Is
it with the EXECUTE verb?  The syntax of EXEC is:

>>-------- EXEC ----- text-name text-data---END-EXEC--------><

If this is used for DOS commands, I don't know what text-name and text-data
would be....I am new to this. The command I want to execute is
'C:\WINDOWS\NOTEPAD.EXE c:\textfile.txt'  Any help would be
greatly appreciated...

Steve
```

#### ↳ Re: ?How to execute a DOS command in MicroFocus Anim.V2??

- **From:** "Lucas, Todd" <Todd.Lucas@c-cubed.net>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c3302f_3@news1.prserv.net>`
- **References:** `<89u4ge0red@enews4.newsguy.com>`

```
Look up a call by number routine in the manual - x'91' function 35.  This
soes what you want to do.  You could also invoke a Win32 API to do the same.
If you need more info just email me and I will send an example...

TL

Todd Lucas
email:  Todd.Lucas@C-Cubed.net

C-Cubed Inc.
3629 North Morning Dove
Mesa, AZ  85207

Phone:  (888) 962-8233
Fax:     (888) 962-4658
Web:    http://www.c-cubed.net
Dirt <dirt@vh.net> wrote in message news:89u4ge0red@enews4.newsguy.com...
> Does anyone know how to execute a DOS command in MF Animator version 2? Is
> it with the EXECUTE verb?  The syntax of EXEC is:
…[3 more quoted lines elided]…
> If this is used for DOS commands, I don't know what text-name and
text-data
> would be....I am new to this. The command I want to execute is
> 'C:\WINDOWS\NOTEPAD.EXE c:\textfile.txt'  Any help would be
…[4 more quoted lines elided]…
>
```

#### ↳ Re: ?How to execute a DOS command in MicroFocus Anim.V2??

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kmb6cs85moudhnd4ilcgr6i3qjv8s71cpu@4ax.com>`
- **References:** `<89u4ge0red@enews4.newsguy.com>`

```
02 result pic x comp-x.
02 func-num pic x comp-x value 35.

02 parm.
	03 length pic x comp-x.
	03 exe	pic x(22) value "c:\windows\notepad.exe ".
	03 filename	pic x(8) value "text.txt".

add 22 to 8 giving length
call x"91" using result, func-num, parm



reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
