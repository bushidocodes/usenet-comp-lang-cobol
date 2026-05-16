[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error encountered in Cobol

_4 messages · 2 participants · 2003-06_

---

### Error encountered in Cobol

- **From:** Souhaibb <member31957@dbforums.com>
- **Date:** 2003-06-26T07:47:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3045033.1056613666@dbforums.com>`

```

Hi All,

I have encountered an error message in cobol as mentioned below.

Load failure <170> on file ADIS

I have checked the error details in addition also copied the ADIS file
to my working directory, the error is still not removed even after no.
of compilations.

Please advice in regard to the above at the earliest.

Best regards,
Souhaibb
```

#### ↳ Re: Error encountered in Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-06-26T22:16:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bdeh76$ad5$1@aklobs.kc.net.nz>`
- **References:** `<3045033.1056613666@dbforums.com>`

```
Souhaibb wrote:

> I have encountered an error message in cobol as mentioned below.
> 
…[4 more quoted lines elided]…
> of compilations.

Let me guess: some form of MicroFocus.

ADIS is the Accept/Display module required when using XOpen screen handling 
such as screen section or DISPLAY ... AT.

With my vesrions of MF I need to link in somehow the ADIS, ADISINIT and 
ADISKEYS objects.  See your System manual for exact details on how to do 
this for how you are building systems.

What did you mean by 'copied the ADIS file' ?  Copying isn't what is 
required.
```

#### ↳ Re: Error encountered in Cobol

- **From:** Souhaibb <member31957@dbforums.com>
- **Date:** 2003-06-27T06:09:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3049515.1056694181@dbforums.com>`
- **References:** `<3045033.1056613666@dbforums.com>`

```

This problem is related to MS Cobol 4.5.

Wht I meant by copying the file into the directory was that I thought
that the ADIS, ADISINIT etc. have to be present in my working directory.
However even after placing the files into my working directory I was
still not able to execute the program.

The below mentioned error still reamains.

Can anybody suggest that how to connect / link the ADIS, ADISINIT etc.
files to my program. ( I don't have the System manual)

In addition, please advice a way on how to use the LINE, COLUMN command
in MS Cobol 4.5. As at this moment I cannot use this command either with
Display or Accept Command.

Thanks & Regards,
Souhaibb
```

##### ↳ ↳ Re: Error encountered in Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-06-27T13:41:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0306271241.5d6ea427@posting.google.com>`
- **References:** `<3045033.1056613666@dbforums.com> <3049515.1056694181@dbforums.com>`

```
Souhaibb <member31957@dbforums.com> wrote

> This problem is related to MS Cobol 4.5.
> 
…[3 more quoted lines elided]…
> still not able to execute the program.

You cannot execute a .OBJ file.  Copying the ADIS.OBJ files will not
work, you need to LINK them into your program or link them together to
make an ADIS.EXE.
 
> The below mentioned error still reamains.

> Can anybody suggest that how to connect / link the ADIS, ADISINIT etc.
> files to my program. ( I don't have the System manual)

LINK program+ADIS+ADISINIT+ADISKEYS;

How hard is that ?  What message are you getting ?
 
> In addition, please advice a way on how to use the LINE, COLUMN command
> in MS Cobol 4.5. As at this moment I cannot use this command either with
> Display or Accept Command.

Is it that you don't know how to write the source ?  Does the compiler
give you errors ?  Or is it that you can't use it because the running
says it can't find the ADIS.

We can't see your screen displays, although you may think they are
just gibberish they do actually mean something.

We also can't see your source code.  Post it if you don't know why the
compiler is giving errors.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
