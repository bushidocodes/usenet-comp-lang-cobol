[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-question

_2 messages · 2 participants · 1997-01_

---

### MF-question

- **From:** "ari..." <ua-author-17071987@usenetarchives.gap>
- **Date:** 1997-01-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cs6ra$1un@pravda.tisip.no>`

```

I have two questions about Micro Focus cobol. I'm using MF workbench 4.0
and Dialog System 2.5.64 (all 32-bits).

1:Printing
When I used MF workbench 3.2 (16bit), the print-option worked fine.
I used functions like "PC_WIN_WRITE_PRINTER", "PC_WIN_OPEN_PRINTER"
"PC_WIN_CLOSE_PRINTER" etc. In the beginning of the program, I create
a pointer like "set Mfprn-ptr to entry mfprnt16" All this stuff
worked fine. Now, in my 32bit environment, it won't work. I have tried
to replace the mfprnt16 with mfprnt32, but the printer allways
print garbage. What to I need to do in my 32bit environment ?

2:resource-intensive Micro Focus cobol ?
We have a customer who are testing our MF application. Last week the
told us that when they are running our application, all memory is
beeing used by our program on their server. I know one reason can be
the way we are building our application. We do like this:
We have an exe-trigger file, who start the application. Our application
consist of about 90 screenset, witch is build into one lbr-file, named
gs.lbr. Then, our gnt-files, is build into 6 different lbr-files. In our
exe-cfg-file, we are loading all this files. (in our trigges configuration-
file) Is there any other way to do this. As you see, we are using
MF library facility to create or lbr-file, and "Build" to create our
exe-trigger-file.
Hope anyone have experience with this. I desperately want to reduce the
memory usage !

Thank's a lot

Regards

Arild Andersen
Trondheim, Norway
```

#### ↳ Re: MF-question

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-01-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fbcfd521ac-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5cs6ra$1un@pravda.tisip.no>`
- **References:** `<5cs6ra$1un@pravda.tisip.no>`

```

Arild Andersen wrote:
› 
› I have two questions about Micro Focus cobol. I'm using MF workbench 4.0
› and Dialog System 2.5.64 (all 32-bits).
 
› 2:resource-intensive Micro Focus cobol ?
›  We have a customer who are testing our MF application. Last week the
…[6 more quoted lines elided]…
›  exe-cfg-file, we are loading all this files.

RE: reducing memory requirements -

I doubt that it's the packaging that's the problem (when you open LBR
files,
we do not load the whole file into memory, we just register the
catalogue
entries so you can CALL/open the programs within them).
However, because your programs are all dynamically loaded, you can free
up
the memory they are using with the CANCEL verb. Using this method you
get
a slower, but more memory efficient way of calling your sub-programs
(once
CANCELled, a program's memory can be used by the next program called).
Also, see the "CBL_SUBSYSTEM" call-by-name routine in your docs to see
how
to automatically get the system to "group" call hierachies for you to
CANCEL
in one go. Of course, you need to be aware of the CANCEL semantics such
as
re-initialisation of working-storage/closing of files etc.

One other point to mention about CANCEL in the 32-bit products (so even
if
you're already using it, this is important) is that there's a program
cache
in operation. When you CANCEL a program, it's memory is not actually
freed to
the OS until (a) the OS will not give your process more memory or (b) a
settable upper-limit is reached.
The limit is set with the configuration tuneable "dynamic_memory_limit".
You can set this to the special value of zero to completely disable the
program cache (then only situation (a) above will give you an out of
memory error).

Cheers,
Kev.






›  Thank's a lot
› 
…[3 more quoted lines elided]…
›  Trondheim, Norway
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
