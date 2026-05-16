[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# why there is difference in ASCII code?

_5 messages · 4 participants · 2003-02_

---

### why there is difference in ASCII code?

- **From:** yauyau <member23982@dbforums.com>
- **Date:** 2003-02-10T20:43:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2509418.1044909791@dbforums.com>`

```

I find that the ASCII code system used in Fujisi COBOL85 is different
from the code system that I use usually...

because for the code:

display FUNCTION CHAR( 33 )

it shows on the screen a space character....
but I check the ASCII table in Fortran... it should be '!'
instead of space.

Is it because I run the programme in WINDOW XP?

but that's strange....
```

#### ↳ Re: why there is difference in ASCII code?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-10T22:49:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e482aec.180539703@news.optonline.net>`
- **References:** `<2509418.1044909791@dbforums.com>`

```
yauyau <member23982@dbforums.com> wrote:

>I find that the ASCII code system used in Fujisi COBOL85 is different
>from the code system that I use usually...
…[9 more quoted lines elided]…
>Is it because I run the programme in WINDOW XP?

It's because the Fujitsu function uses a subscript into a table which goes 1
through 256, the COBOL norm, rather than 0 thru 255. ASCII 32, at the 33rd
position in the table, is space.  Use 34 to get !

Better yet, forget the function, use x'21'. 


>but that's strange....
>
>--
>Posted via http://dbforums.com
```

##### ↳ ↳ Re: why there is difference in ASCII code?

- **From:** ronglaz6@aol.comnojunk (Ron Glazier)
- **Date:** 2003-02-11T03:41:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030210224139.04592.00000480@mb-ct.aol.com>`
- **References:** `<3e482aec.180539703@news.optonline.net>`

```
    I dont know if this relates to what you posted but I sometimes find
problems with the part of the file after the end of the cobol program.  If a
special character is some how in there yet not visible.  we can not then see
it.  I used to solve this problem by deleting with backspace key from point
right at end upto the dot at the end of the last sentence, then give about 5
enters ( 5 lines) and save it.  
But also did some times use diskedit to look at the program and with diskedit,
one can see the unnsee able invisible item. (and so delete it, once found).
  this kind of thing can take place when code from one program is run on a
different compiller than before. (like microfocus and cobol 650 being different
compillers) you could get a message like this
 " cant read character in column 7 " ( which is after the end of the program on
the line before).
  Does not happen very much though.
how I found out about this was that I found a program with a lot of right
pointing arrows after the end of it, so like a good boy scout, I deleted them. 
the program then would not re compile as illegal character in position 7 (after
end of the program code itself) yet not visible !  And my version of diskedit
will not work on windows xp as well !!   The only way I could fix the problem
and get the program fixed was to re copy a backup of the program (which was a
copy before the change) to overite the one I tried to correct by deleting the
arrows.  So it still now has the arrows at the end (but it works )  !
        Ron
RonGlaz@juno.com
```

###### ↳ ↳ ↳ Re: why there is difference in ASCII code?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-11T04:29:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e487aa8.200954648@news.optonline.net>`
- **References:** `<3e482aec.180539703@news.optonline.net> <20030210224139.04592.00000480@mb-ct.aol.com>`

```
ronglaz6@aol.comnojunk (Ron Glazier) wrote:

>    I dont know if this relates to what you posted but I sometimes find
>problems with the part of the file after the end of the cobol program.  If a
…[19 more quoted lines elided]…
>arrows.  So it still now has the arrows at the end (but it works )  !

This is not a COBOL problem, it's a text editor problem. COBOL wants source to
be plain ASCII text. 

The extra characters at the end are an artifact of some screwy text editor. 
Try editing your source with WordPad or NotePad.

Robert
```

###### ↳ ↳ ↳ Re: why there is difference in ASCII code?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-11T06:50:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q6WcnQYPe47QbNWjXTWclg@giganews.com>`
- **References:** `<3e482aec.180539703@news.optonline.net> <20030210224139.04592.00000480@mb-ct.aol.com>`

```

"Ron Glazier" <ronglaz6@aol.comnojunk> wrote in message
news:20030210224139.04592.00000480@mb-ct.aol.com...
>     I dont know if this relates to what you posted but I sometimes find
> problems with the part of the file after the end of the cobol program.  If
a
> special character is some how in there yet not visible.  we can not then
see
> it.  I used to solve this problem by deleting with backspace key from
point
> right at end upto the dot at the end of the last sentence, then give about
5
> enters ( 5 lines) and save it.


> But also did some times use diskedit to look at the program and with
diskedit,
> one can see the unnsee able invisible item. (and so delete it, once
found).
>   this kind of thing can take place when code from one program is run on a
> different compiller than before. (like microfocus and cobol 650 being
different
> compillers) you could get a message like this
>  " cant read character in column 7 " ( which is after the end of the
program on
> the line before).
>   Does not happen very much though.
> how I found out about this was that I found a program with a lot of right
> pointing arrows after the end of it, so like a good boy scout, I deleted
them.
> the program then would not re compile as illegal character in position 7
(after
> end of the program code itself) yet not visible !  And my version of
diskedit
> will not work on windows xp as well !!   The only way I could fix the
problem
> and get the program fixed was to re copy a backup of the program (which
was a
> copy before the change) to overite the one I tried to correct by deleting
the
> arrows.  So it still now has the arrows at the end (but it works )  !

The arrow is an end-of-file marker.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
