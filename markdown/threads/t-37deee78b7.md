[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# rmcobol call "SYSTEM"

_6 messages · 4 participants · 1999-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### rmcobol call "SYSTEM"

- **From:** helpless@my-dejanews.com
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cbclu$fp9$1@nnrp1.dejanews.com>`

```
I am using RMCOBOL 6.61 on a aix box.  I am trying to use the call "system"
to run a ksh shell which will prompt for entry from the screen.

I cannot get the shell to stop and wait for entry. Any suggestions.

thanks

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: rmcobol call "SYSTEM"

- **From:** frederico@memosis.pt (Frederico Fonseca)
- **Date:** 1999-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36e96085.765408@news.indigo.ie>`
- **References:** `<7cbclu$fp9$1@nnrp1.dejanews.com>`

```
On Fri, 12 Mar 1999 15:42:57 GMT, helpless@my-dejanews.com wrote:

>I am using RMCOBOL 6.61 on a aix box.  I am trying to use the call "system"
>to run a ksh shell which will prompt for entry from the screen.
>
>I cannot get the shell to stop and wait for entry. Any suggestions.
>
Why exactly does the ksh to stop for input.
depending on that maybe we can help.

Best

Frederico Fonseca
```

##### ↳ ↳ Re: rmcobol call "SYSTEM"

- **From:** helpless@my-dejanews.com
- **Date:** 1999-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cln26$346$1@nnrp1.dejanews.com>`
- **References:** `<7cbclu$fp9$1@nnrp1.dejanews.com> <36e96085.765408@news.indigo.ie>`

```
In article <36e96085.765408@news.indigo.ie>,
  frederico@memosis.pt wrote:
> On Fri, 12 Mar 1999 15:42:57 GMT, helpless@my-dejanews.com wrote:
>
…[10 more quoted lines elided]…
> Frederico Fonseca
I display a list of companies and ask for a choice.
Set enviroments by choice then continues to run the script
which runs a report writer and comes back to cobol program.
liant says it is a unix problem so they cannot help.
Thanks.
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: rmcobol call "SYSTEM"

- **From:** frederico@memosis.pt (Frederico Fonseca)
- **Date:** 1999-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f0e8fe.1082744@news.indigo.ie>`
- **References:** `<7cbclu$fp9$1@nnrp1.dejanews.com> <36e96085.765408@news.indigo.ie> <7cln26$346$1@nnrp1.dejanews.com>`

```

>> Frederico Fonseca
>I display a list of companies and ask for a choice.
…[3 more quoted lines elided]…
>Thanks.
Can you send me (or post here) the shell script and all the scripts 
that get called by the first one, in case they also need input,
so I can study them and eventually sugest a solution.

Thanks

Frederico Fonseca
```

###### ↳ ↳ ↳ Re: rmcobol call "SYSTEM"

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36ee7f14.2825916@news.enteract.com>`
- **References:** `<7cbclu$fp9$1@nnrp1.dejanews.com> <36e96085.765408@news.indigo.ie> <7cln26$346$1@nnrp1.dejanews.com>`

```
I remeber all our "SYSTEM" calls in RMCobol had a trailing byte with
LOW-VALUES in it.  You might want to try this to see if it helps.
Somehting like:

     01 SYS-CMD
         03 FILLER         PIC X(11) VALUE "sh myscript".
         03 FILLER         PIC X(1) VALUE LOW-VALUES.
.
.
.
.

   CALL "SYSTEM" USING SYS-CMD.


Hope this helps,

Paul


On Tue, 16 Mar 1999 13:41:28 GMT, helpless@my-dejanews.com wrote:

>In article <36e96085.765408@news.indigo.ie>,
>  frederico@memosis.pt wrote:
…[21 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own    

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

###### ↳ ↳ ↳ Re: rmcobol call "SYSTEM"

- **From:** Albert Ratzlaff <albert@conexion.com.py>
- **Date:** 1999-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36EF8F83.575FB0DB@conexion.com.py>`
- **References:** `<7cbclu$fp9$1@nnrp1.dejanews.com> <36e96085.765408@news.indigo.ie> <7cln26$346$1@nnrp1.dejanews.com>`

```
helpless@my-dejanews.com wrote:

> I display a list of companies and ask for a choice.
> Set enviroments by choice then continues to run the script
> which runs a report writer and comes back to cobol program.
> liant says it is a unix problem so they cannot help.
> Thanks.

I don't know about AIX, but RM/COBOL is supposed to be pretty much the same on all
platforms. One of the problems with the system call is that RM/COBOL need certain
terminal settings for the ACCEPT and DISPLAY statements. When you do a CALL
"SYSTEM", it has to restore the terminal settings to normal, and after returning
it has to reset them again. If you are not calling an interactive script or
program, you don't need all that. So there is a special argument to the system
call that turns off those resetings. Maybe that is what is happening.
Try a calling a short script, something like:

"who
echo Press ENTER
read answer"

Regards
Albert Ratzlaff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
