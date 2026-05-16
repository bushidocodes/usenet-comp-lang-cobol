[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Syntax for embedded sql

_14 messages · 4 participants · 2005-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Syntax for embedded sql

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-09T10:10:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com>`

```
I am writing a program and need to know the correct syntax inside Cobol
for SUBSTR.

Insert into catable
   (member, namekey, namekey6, namekey10, name)
   Select substr(name, 1, 2), name, 1, 6)
   From Member
   Where members not = "0000000000"
   Order by Members
EXEC-END.

Is this Correct?
```

#### ↳ Re: Syntax for embedded sql

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-09T10:13:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118337196.741809.129880@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com>`

```
I meant END-EXEC.
```

#### ↳ Re: Syntax for embedded sql

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-06-09T19:30:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fl2ha19fq66cnqi401ne9ppha0d9cosmi7@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com>`

```
On 9 Jun 2005 10:10:56 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>I am writing a program and need to know the correct syntax inside Cobol
>for SUBSTR.
…[9 more quoted lines elided]…
>Is this Correct?
Which COBOL vendor/version, which Pre-compiler, which OS and which
Database.

Syntax will vary depending on all of the above.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Syntax for embedded sql

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-09T11:46:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118342812.188855.158970@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<fl2ha19fq66cnqi401ne9ppha0d9cosmi7@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fl2ha19fq66cnqi401ne9ppha0d9cosmi7@4ax.com>`

```
Sorry I guess I should have included all of that,   Oracle 9.1
Pro*Cobol  Micro-Focus Cobol on an HP9000.
```

#### ↳ Re: Syntax for embedded sql

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-06-09T20:09:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com>`

```
On 9 Jun 2005 10:10:56 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>I am writing a program and need to know the correct syntax inside Cobol
>for SUBSTR.
…[9 more quoted lines elided]…
>Is this Correct?

There is not specific way of doing it with Oracle on ESQL.

so the following is correct


exec sql
insert into my_tbl (name)
select substr(name, 1, 2) from my_other_tbl
end-exec.

Note that you may have an extra ")" on your previous code.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Syntax for embedded sql

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-09T12:33:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118345628.324968.180670@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com>`

```
Insert into catable
>   (member, namekey, namekey6, namekey10, name)
>   Select substr(name, 1, 2, name, 1, 6, name, 1, 10)
…[3 more quoted lines elided]…
>EXEC-END.


If I have multiple substrings like above, can I place them in 1 set of
( ) or do them individually? Thank you for getting back with me so
quickly
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-09T12:37:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118345870.728539.174640@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1118345628.324968.180670@g49g2000cwa.googlegroups.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com>`

```
         EXEC SQL INSERT INTO CANAMEDETL
           ( NAMEKEY, NAMEKEY6, NAMEKEY10, NAME, MBRSEP,
            IMAXSOFT13_PATH_01, IMAXSOFT13_PATH_02, IMAXSOFT13_PATH_03,
               IMAXSOFT13_PATH04, IMAXSOFT13_SEQ_NO )
              SELECT SUBSTR(NAME, 1, 2), SUBSTR(NAME, 1, 6),
                  SUBSTR(NAME, 1, 10), NAME, MBRSEP, 0, 0, 0, 0
                 FROM MBRSEPMSTR
                 WHERE MBRSEP NOT = '0000000000'
                 ORDER BY NAME, MBRSEP
          END-EXEC.

Frederico,

I have tried looking through the Pro*Cobol book and I cannot find
examples this detailed. Is this Code ok? This is what I meant to post
the first time.
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 4)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-06-09T21:47:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com>`

```
On 9 Jun 2005 12:37:50 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>         EXEC SQL INSERT INTO CANAMEDETL
>           ( NAMEKEY, NAMEKEY6, NAMEKEY10, NAME, MBRSEP,
…[13 more quoted lines elided]…
>the first time.

Yes, but the number of parameters do not match.

you have 10 field names, and only 9 select fields.

I think you better try the SQL first on SQL*Plus and then use it
within the COBOL program, as this is a simple SQL without host
variables.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 5)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-10T03:50:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118400614.115227.74490@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com>`

```
I missed a 0 on one of the imaxsoft fields. Thanks for your help, I
really appreciate it.
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 6)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-10T07:35:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118414154.524679.315460@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<1118400614.115227.74490@z14g2000cwz.googlegroups.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com> <1118400614.115227.74490@z14g2000cwz.googlegroups.com>`

```
Frederico,

I have written the program and I do a

 procob /cadevel/symbolic/sortjm.cbl  /cadevel/symbolic/sortjm.cob
I get the message

System default option values taken from:
/u00/app/oracle/product/10.1.0/client/p
recomp/admin/pcbcfg.cfg

When I do a ncobol sortjeff

I get 10 errors:

005166     EXEC SQL BEGIN DECLARE SECTION END-EXEC.
* 149-S********
     **
**    No SQL directives have been set
005176     EXEC SQL END DECLARE SECTION END-EXEC.
* 149-S********
     **
**    No SQL directives have been set
005180     EXEC SQL
* 149-S********
     **
**    No SQL directives have been set
005183     EXEC SQL
* 149-S********
     **
**    No SQL directives have been set
005198     EXEC SQL
* 149-S********
     **
**    No SQL directives have been set

What am I missing? There is nobody here who has embedded sql in Cobol
or tried to connect thru Cobol etc.
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 7)_

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2005-06-10T15:59:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8ca9k$fj3$1@hyperion.microfocus.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com> <1118400614.115227.74490@z14g2000cwz.googlegroups.com> <1118414154.524679.315460@o13g2000cwo.googlegroups.com>`

```
> When I do a ncobol sortjeff
>
…[5 more quoted lines elided]…
> **    No SQL directives have been set

<snip>

You appear to be compiling the original, unprocessed source here, rather 
than the output from the precompiler.

cob -it sortjm.cob

should compile the correct source (I assume that ncobol is a shell script?).

SimonT.
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 7)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-06-10T17:56:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fhja19tc7bc4negdv1a5j1cib9lnqistn@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com> <1118400614.115227.74490@z14g2000cwz.googlegroups.com> <1118414154.524679.315460@o13g2000cwo.googlegroups.com>`

```
On 10 Jun 2005 07:35:54 -0700, "Jeff" <jmoore207@hotmail.com> wrote:

>Frederico,
>
…[7 more quoted lines elided]…
>recomp/admin/pcbcfg.cfg

Within the Oracle/product/... structure you should have a few
makefiles and samples of how to compile a .pco ESQL source.

Search for them and see how it is done within your system.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 8)_

- **From:** "Jeff" <jmoore207@hotmail.com>
- **Date:** 2005-06-15T05:19:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118837995.357293.6970@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<8fhja19tc7bc4negdv1a5j1cib9lnqistn@4ax.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com> <1118400614.115227.74490@z14g2000cwz.googlegroups.com> <1118414154.524679.315460@o13g2000cwo.googlegroups.com> <8fhja19tc7bc4negdv1a5j1cib9lnqistn@4ax.com>`

```
I am trying to run my script. It does the truncate table part

SQL> select count(*) from coboltest;

  COUNT(*)
----------
         0

Elapsed: 00:00:00.01

When it tries to do the first insert, I get the error message below.
       01  SQ0001 GLOBAL.
           02  FILLER PIC X(25) VALUE "truncate  TABLE COBOLTEST".


       01  SQ0002 GLOBAL.
           02  FILLER PIC X(150) VALUE "insert into
COBOLTEST(MBRSEP,IMA
      -    "XSOFT13_PATH_01,IMAXSOFT13_SEQ_NO)(select MBRSEP  ,0  ,0
f
      -    "rom MBRSEPMSTR where MBRSEP<>'0000000000' order by
MBRSEP)".

           EXEC SQL INSERT INTO COBOLTEST
               ( MBRSEP, IMAXSOFT13_PATH_01, IMAXSOFT13_SEQ_NO)
               (SELECT MBRSEP, 0, 0
                  FROM MBRSEPMSTR
                  WHERE MBRSEP !=  '0000000000'
                  ORDER BY MBRSEP)
           END-EXEC.
           CALL "SQLADR" USING SQ0002 SQL-STMT
           MOVE 1 TO SQL-ITERS
           MOVE 20 TO SQL-OFFSET
           MOVE 0 TO SQL-OCCURS
           CALL "SQLADR" USING
               SQLCUD
               SQL-CUD
           CALL "SQLADR" USING
               SQLCA
               SQL-SQLEST

06/15/05 BEGIN BILLING DATABASE SORT 08:13 AM

ORACLE ERROR DETECTED:

ORA-00907: missing right parenthesis

Does anyone have any thoughts of what I am doing wrong? I am kind of
out on an island with nobody to go to! Any help would be greatly
appreciated.
```

###### ↳ ↳ ↳ Re: Syntax for embedded sql

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-06-15T12:10:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1118862635.200511.172760@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1118837995.357293.6970@g49g2000cwa.googlegroups.com>`
- **References:** `<1118337056.344429.73090@g49g2000cwa.googlegroups.com> <fo4ha11sgpuvd7nvkpvd56pr1t64jconuq@4ax.com> <1118345628.324968.180670@g49g2000cwa.googlegroups.com> <1118345870.728539.174640@g44g2000cwa.googlegroups.com> <9kaha1pf74je8ng1d7vq1jeepnc2tttft4@4ax.com> <1118400614.115227.74490@z14g2000cwz.googlegroups.com> <1118414154.524679.315460@o13g2000cwo.googlegroups.com> <8fhja19tc7bc4negdv1a5j1cib9lnqistn@4ax.com> <1118837995.357293.6970@g49g2000cwa.googlegroups.com>`

```
02  FILLER PIC X(150) VALUE "insert into

Perhaps the literal is more than 150.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
