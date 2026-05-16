[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking if Directori Exists in Power

_4 messages · 2 participants · 2003-05_

---

### Checking if Directori Exists in Power

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-27T20:58:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2928560.1054069086@dbforums.com>`

```

hi.

 01 wsg-dadosdoarquivo is global.
     03 wsg-nomeatestar    PIC X(255).
     03 wsg-name-length    PIC 9(4) BINARY.
     03 wsg-status-code     PIC S9(4) COMP-5.

     move    Pow-Text  of wpath  to wsg-filename.

     move  wsg-filename   to wsg-nomeatestar
     CALL "CBL_READ_DIR"
           USING    by reference
                    wsg-nomeatestar
                    wsg-name-length
           RETURNING wsg-status-code.

     if  wsg-status-code  not = zeros


if the Directory exist, wsg-status-code Should be ZEROS

this routine  always return wsg-status-code =  -0001

where is my mistake.

by the way  ui have already check the help and Books
and  I did not see anything suspect.

Tks

Carlos Lages
```

#### ↳ Re: Checking if Directori Exists in Power

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-27T20:34:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tidnQMzwLa-j0mjXTWJig@giganews.com>`
- **References:** `<2928560.1054069086@dbforums.com>`

```

"Carlos lages" <member129@dbforums.com> wrote in message
news:2928560.1054069086@dbforums.com...
>
> hi.
…[25 more quoted lines elided]…
> and  I did not see anything suspect.

---------

You've got the parameters reversed (and you don't need "by reference").

CALL "CBL_READ_DIR" USING
    wsg-name-length
   wsg-nomeatestar
   RETURNING wsg-status-code.
```

##### ↳ ↳ Re: Checking if Directori Exists in Power

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-28T10:44:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2930547.1054118693@dbforums.com>`
- **References:** `<2928560.1054069086@dbforums.com> <8tidnQMzwLa-j0mjXTWJig@giganews.com>`

```

I checked and doesnt work
Now all status is +0000 ,
by the way Fujistu manual instrution below

Parameter data definition
01 path-name PIC X(n).
01 path-name-length PIC 9(4) BINARY.
01 status-code PIC S9(4) COMP-5.
80 Chapter 4. File Routines
Calling format
CALL "CBL_READ_DIR"
USING path-name
path-name-length
RETURNING status-code.

Carlos Lages[


You've got the parameters reversed (and you don't need "by reference").

CALL "CBL_READ_DIR" USING
    wsg-name-length
   wsg-nomeatestar
   RETURNING wsg-status-code. 
```

##### ↳ ↳ Re: Checking if Directori Exists in Power

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-05-28T21:38:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2933379.1054157929@dbforums.com>`
- **References:** `<2928560.1054069086@dbforums.com> <8tidnQMzwLa-j0mjXTWJig@giganews.com>`

```

I found out where my mistake was.

CBL_read_dir  , reads the current directory only

I  thought  it  reads any directory
Fujtisu manual is not clear about this

in other words , if you want to check i a Directory exists
you must use CBL_CHANGE_DIR

if was changed , OK
 if was not , Not OK

Carlos Lages
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
