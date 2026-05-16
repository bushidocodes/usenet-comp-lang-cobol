[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Load Failure

_4 messages · 4 participants · 2003-07_

---

### Load Failure

- **From:** kyaqub <member31937@dbforums.com>
- **Date:** 2003-07-07T05:38:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3080566.1057556338@dbforums.com>`

```

Greetings:

               Well I am accessing the Oracle DB from my cobol program.
               After writing the program, I have compiled it with the
               Oracle Pro* Cobol Compiler, thus translating all the
               Embeded SQL. Then I compile the output source file with
               the MS Cobol 4.5. The compilation is successfull with no
               errors. Then I make the executable through the Link
               program, and it has generated the executable
               successfully. But when I try to execute the program I
               received the following error message.


             "Load Failure (173) on file C:\Cobol\BINR\ORASQL8"

              Well I am using the oracle 9i Database. I have copied the
              lib files necessary for accessing oracle from the Oracle
              Lib directory folder to my BINR directory, But I am still
              receiving this error.

              Can any body have a clue that why this error message is
              coming. And what is the solution to it????

       Any body please helpppppppppppppppppppppppp.

 Regards
 Kyaqub
```

#### ↳ Re: Load Failure

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-07T19:29:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beb7m8$ibf$1@aklobs.kc.net.nz>`
- **References:** `<3080566.1057556338@dbforums.com>`

```
kyaqub wrote:

>              "Load Failure (173) on file C:\Cobol\BINR\ORASQL8"
> 
…[3 more quoted lines elided]…
>               receiving this error.

Cobol CALLs can be static or dynamic.  A Dynamic CALL, such as CALL "fred" 
tries to laod 'fred' at run time as a file FRED.EXE or FRED.DLL (or similar 
depending on evironment and noting this is MS 4.5).  It looks for these in 
the COBDIR path and the last of these is the BINR directory.

You need to make the CALL to Oracle to being static so that it is linked 
into the program from the .OBJ or .LIB.  

Add the LITLINK directive to the compile to make the calls using literals 
static.  Add the Oracle libraries or objects to the LINK parameters. You 
may need to add the path to the Oracle library directory to the LIB=.

Note: MS Cobol 4.5 is a 16 bit product for DOS, Windows 3.1 and OS/2 2.x.  
You need DOS Libraries for Oracle.
```

#### ↳ Re: Load Failure

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-07-07T09:52:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bebbrl$vv0$1@hyperion.microfocus.com>`
- **References:** `<3080566.1057556338@dbforums.com>`

```
This is a known bug in the Oracle 9i precompiler. It should be embedding
calls to 'ORASQL9', but in fact embeds calls to 'ORASQL8'.

If within your Oracle\BIN directory, you copy ORASQL9.DLL to ORASQL8.DLL,
your app will execute correctly.

Simon.
```

#### ↳ Re: Load Failure

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-07T05:47:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307070447.2ab63cac@posting.google.com>`
- **References:** `<3080566.1057556338@dbforums.com>`

```
It continues to baffle me how people can afford the cost of ownership
of an Oracle 9i (and other) databases, but they don't go out and buy a
modern, up to date, and supported COBOL compiler.

You need a new compiler.  Both Fujitsu and Micro Focus 32 bit
compilers are supported by the Oracle PRO*COBOL Precompiler.  Your
Micfosoft COBOL 4.5 is an old - very old - 16 bit product and cannot
call the 32 bit modules provided by Oracle.

kyaqub <member31937@dbforums.com> wrote in message news:<3080566.1057556338@dbforums.com>...
> Greetings:
> 
…[24 more quoted lines elided]…
>  Kyaqub
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
