[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to use 'CBL_ERROR_PROC'?

_5 messages · 2 participants · 1999-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to use 'CBL_ERROR_PROC'?

- **From:** shanmugam@my-dejanews.com
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a9ncj$rb5$1@nnrp1.dejanews.com>`

```
How to use 'CBL_ERROR_PROC' call_by_name function in MFCOBOL on UNIX
platform. I was trying the sample code given in the manual, but I couldn't
succeeded. Please help me.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: How to use 'CBL_ERROR_PROC'?

- **From:** jm.bain-cornu@sis-france.com (jean-michel)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ca7a57.2141045@news.easynet.fr>`
- **References:** `<7a9ncj$rb5$1@nnrp1.dejanews.com>`

```
On Mon, 15 Feb 1999 18:00:55 GMT, shanmugam@my-dejanews.com wrote:

>platform. I was trying the sample code given in the manual, but I couldn't
>succeeded. Please help me.

Please join your sample, i will answer
```

##### ↳ ↳ Re: How to use 'CBL_ERROR_PROC'?

- **From:** shanmugam@my-dejanews.com
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aeul7$bbd$1@nnrp1.dejanews.com>`
- **References:** `<7a9ncj$rb5$1@nnrp1.dejanews.com> <36ca7a57.2141045@news.easynet.fr>`

```
In article <36ca7a57.2141045@news.easynet.fr>,
  jm.bain-cornu@sis-france.com (jean-michel) wrote:
> On Mon, 15 Feb 1999 18:00:55 GMT, shanmugam@my-dejanews.com wrote:
>
…[4 more quoted lines elided]…
>
Program-1:
      *This program is triggered from errtest.cbl. Before RTS error
      *this program has to send a mail to 'dshan' user-id with error
      *Message.
       program-id.  errproc.
       1 rmail pic x(50) value
         'echo "`date` error in sytol"| rmail dshan ' & X'00'.
       linkage section.
       1  err-param.
          5  err-msg     pic X(325).
          5  err-no      pic X(3).
       procedure division.
       10.
           display "Installing error procedure"
           exit program.

           entry "myerr" using err-param.
           IF err-no = "SUB"
              call "system" using rmail.
           move 0 to return-code.
           exit program.
------------------------------------------------------------------------------
Program-2:
       identification division.
       program-id.    errtest.
       working-storage section.
       1 z pic x occurs 10.
       1 x pic 9.
       1 y pic 9 value 1.
       1 t pic 9 value 0.

       1  install-flag      pic x  comp-x value 0.
       1  install-address   usage procedure-pointer.
       1  status-code       pic 9(4) comp value zeros.

       Linkage section.
       1  err-param.
          5  err-msg     pic X(325).
          5  err-no      pic X(3).

       procedure division using err-param.
       01.
           set install-address to entry "errproc".
           set install-address to entry "myerr".
           call "CBL_ERROR_PROC" using install-flag
                                       install-address
                                returning status-code.

       10.
          PERFORM varying x from 1 by 1 until x > 4
             move "SUB" to err-no
             display z(t)
             PERFORM varying y from 1 by 1 until y > 4
                 IF y >= 3
                    exit perform CYCLE
                 END-IF
             END-PERFORM
          END-PERFORM.
          stop run.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: How to use 'CBL_ERROR_PROC'?

- **From:** jm.bain-cornu@sis-france.com (jean-michel)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cd541c.17308407@news.easynet.fr>`
- **References:** `<7a9ncj$rb5$1@nnrp1.dejanews.com> <36ca7a57.2141045@news.easynet.fr> <7aeul7$bbd$1@nnrp1.dejanews.com>`

```
Here is a first program, which do an error after call of the second
program:
       working-storage section.

       01 prog pic x(10) value "stupid".

       procedure division.

       call "tstErr2"

       *>--a stupid call, which hang
       call prog


Here is the second, which manage the error:
       *>------------------------------------------------

       working-storage section.

       01 install-flag       pic x comp-x value 0.

       01 install-address    usage procedure-pointer.

       *>------------------------------------------------

       linkage section.

       01 err-msg            pic x(325).

       *>------------------------------------------------

       procedure division.

       set install-address to entry "err-proc".

       call "CBL_ERROR_PROC" using install-flag install-address

       exit program

       stop run.   *> not mandatory
       *>------------------------------------------------

       entry "err-proc" using err-msg.

       display "we HAVE the error now"

       move 1 to return-code

       exit program

       stop run.


You have to compile with:
cob -x tstErr1.cbl tstErr2.cbl
And then try with:
tstErr1

If you try with animate, this NOT works. It's work with cobrun.
A last thing: if you include err-proc in tstErr1, you will have a
recursive call error when the error will happens.

Best regards
:-) jm
```

###### ↳ ↳ ↳ Re: How to use 'CBL_ERROR_PROC'?

_(reply depth: 4)_

- **From:** shanmugam@my-dejanews.com
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ak7ic$v5m$1@nnrp1.dejanews.com>`
- **References:** `<7a9ncj$rb5$1@nnrp1.dejanews.com> <36ca7a57.2141045@news.easynet.fr> <7aeul7$bbd$1@nnrp1.dejanews.com> <36cd541c.17308407@news.easynet.fr>`

```
In article <36cd541c.17308407@news.easynet.fr>,
  jm.bain-cornu@sis-france.com (jean-michel) wrote:
> Here is a first program, which do an error after call of the second
> program:
…[60 more quoted lines elided]…
>
================================================================================
Hi JM,

Thank you for time & effort. Whatever you have said is true and I got all
those errors while I was testing. What I want to do is, I want to pass some
value to errproc and in errproc evaluate the passed value and execute a
routine (as explanined in my code)

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
