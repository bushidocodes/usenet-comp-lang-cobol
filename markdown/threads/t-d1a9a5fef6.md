[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic deletion of files in os/390 COBOL

_2 messages · 2 participants · 2002-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Dynamic deletion of files in os/390 COBOL

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-08-12T14:11:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aj8fk5$ji5$1@peabody.colorado.edu>`
- **References:** `<64826f50.0208041811.3a3b5ef6@posting.google.com> <othskug97gafo2pqdifp2d24r5env0pbd3@4ax.com> <64826f50.0208052256.67561afc@posting.google.com> <X2749.1531$SE1.1506@news1.central.cox.net>`

```
The following worked for me:
 0410-IEFBR14-DELETE.
**** DELETE IF IT EXISTS.
     MOVE SPACE                TO C-S-DATA.
     STRING ' ALLOC DD(FILEOUT) '
            'DSN(' MYOUTFILE (1:MYOUTFILE-LENGTH) ')'
         ' MOD UNIT(DEVEDISK) CYL SPACE(05,05) DELETE  '
         DELIMITED BY SIZE
                         INTO C-S-DATA
     PERFORM 9000-CLIST.

     MOVE 'FREE DD(FILEOUT)' TO C-S-DATA.
     PERFORM 9000-CLIST.
**** THE ABOVE ALLOWS THAT FILE TO BE OPENED AGAIN.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 39 Line(s) not Displayed
 9000-CLIST.
*****  I DON'T THINK C-S-LEN IS NEEDED
     PERFORM VARYING C-S-LEN FROM 100 BY -1
               UNTIL C-S-LEN < 2
                  OR C-S-DATA (C-S-LEN:1) > SPACE
     END-PERFORM.
D    DISPLAY 'C-S-DATA="' C-S-DATA (1:C-S-LEN) '"'.
     CALL SUB-PGM USING COMMAND-STRING.
     IF RETURN-CODE = 0
         CONTINUE
D        DISPLAY 'RETURN-CODE ="' RETURN-CODE '"'
      ELSE
         DISPLAY 'RETURN-CODE ="' RETURN-CODE '" FOR "'
                 C-S-DATA(1:C-S-LEN) '"'
         DISPLAY '**** ERROR ABORTING ****'
         MOVE '35'           TO RETURN-CODE
         GOBACK
      END-IF.
```

#### ↳ Re: Dynamic deletion of files in os/390 COBOL

- **From:** ssmith@adelaidebank.com.au (Simon Smith)
- **Date:** 2002-08-13T17:38:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64826f50.0208131638.3e69f053@posting.google.com>`
- **References:** `<64826f50.0208041811.3a3b5ef6@posting.google.com> <othskug97gafo2pqdifp2d24r5env0pbd3@4ax.com> <64826f50.0208052256.67561afc@posting.google.com> <X2749.1531$SE1.1506@news1.central.cox.net> <aj8fk5$ji5$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:<aj8fk5$ji5$1@peabody.colorado.edu>...
> The following worked for me:
>  0410-IEFBR14-DELETE.
…[30 more quoted lines elided]…
>       END-IF.

Hi Howard

This worked and does exactly what I wanted.

Thanks
Simon
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
