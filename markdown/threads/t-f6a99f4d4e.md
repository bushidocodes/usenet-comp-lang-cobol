[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# problem linking cobol dll

_3 messages · 2 participants · 1999-08_

---

### problem linking cobol dll

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7q1fi5$9bj$1@nnrp1.deja.com>`

```
 Using Microfocus Cobol 4.0.07 on Windows NT 4.0 ��

I have a pgm that currently is compiled and linked as a DLL and is
called by Powerbuilder and VisualBasic apps.  Now I would like to
separate one of the functions into its own pgm, to be called by the
orginal as well as by other PB, VB, and Cobol pgms.

If I started with this:

Program-id. IRMP0332
Perform do-some-work
Perform get-a-value
Perform do-more work.


I now have this:
Program-id. IRMP0332.
Perform do-some-work
*     	call "nmmcrypt.dll"   *> make api available when animating
     	call APIENTRY "decrypt" using
             by reference wrk-lex-strg
        Perform do-more work.

Program-id. NMMCRYPT.
       Entry decrypt.
       Perform get-a-value.

But when I try to link IRMP0332, the link fails with these msgs:
irmp0332.obj : error LNK2001: unresolved external symbol "_decrypt@4"
irmp0332.obj : error LNK2001: unresolved external symbol "_nmmcrypt.dll"

I am compiling and linking with

CBLLINK -v -d -k -l -o IRMP0332 IRMP0332.cbl+cobintfn.obj advapi32.lib

And have LITLINK set in the source code.

Any ideas on what I need to do to make this work?
```

#### ↳ Re: problem linking cobol dll

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JXYw3.32956$C6.389847@news2.rdc1.on.home.com>`
- **References:** `<7q1fi5$9bj$1@nnrp1.deja.com>`

```
Upgrade to MF COBOL 4.0.38. Merant fixed CBLLINK and the way they mangle
names 'round about 4.0.26. Also, your link statement doesn't seem to include
nmmcrypt.lib or a .DEF file with some import statements so the linker knows
where to find the missing entrypoints.


Ed Stevens <Ed.Stevens@nmm.nissan-usa.com> wrote in message
news:7q1fi5$9bj$1@nnrp1.deja.com...
> Using Microfocus Cobol 4.0.07 on Windows NT 4.0 ..
 >
…[42 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: problem linking cobol dll

- **From:** Ed Stevens <Ed.Stevens@nmm.nissan-usa.com>
- **Date:** 1999-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7q68r8$lau$1@nnrp1.deja.com>`
- **References:** `<7q1fi5$9bj$1@nnrp1.deja.com> <JXYw3.32956$C6.389847@news2.rdc1.on.home.com>`

```
OK.  We have another workgroup working with NetExpress, and they were
able to get clean links, but I don't understand one of the things they
had to do.  The call from pgm-a to pgm-b was changed from

          call APIENTRY "decrypt" using ....

to
          call APIENTRY "decrypt.dll" using ....

What's confusing is that "decrypt" is the entry point (one of several)
within the DLL.  The name of the DLL itself is NMMCRYPT.DLL.  The pgm
is working, but there is no reference at all to the name of the DLL
file, so I'm not understanding how the entry point is located.  Is the
system having to search every DLL in the path?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
