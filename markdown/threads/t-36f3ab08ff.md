[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DISP for optional file

_6 messages · 4 participants · 2003-02_

---

### DISP for optional file

- **From:** abhikush@rediffmail.com (maverick)
- **Date:** 2003-02-25T05:15:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8501a81.0302250515.27a44c8c@posting.google.com>`

```
Hi,
What is the DISP parameter for optional file? I used DISP=OLD but that
did not work out. Got a JCL error.
```

#### ↳ Re: DISP for optional file

- **From:** Terry Sambrooks <terry@kmsitltd.co.uk>
- **Date:** 2003-02-25T08:40:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5b725e$1_8@news.onlynews.com>`
- **References:** `<8501a81.0302250515.27a44c8c@posting.google.com>`

```
Hi,

What is meant by optional file.

From a program's perspective a file may be optional in that it may be
OPENED or NOT OPENEd according to the logica flow.

If it is OPENED and there is no DD statement, then an IEC message of
some type will be issue. (An abend will also occur if I/O is attempted,
so DD DUMMY or DSN=NULLFILE would be the order of te day.) If it is not
OPENED then no DD statement is required.

From a JCL point of view OPTIONAL doesn't arise if the file is required
a DD statement must be present. The parameters will depend upon whether
the file exists or not. If the file exists, the disposition would
logically be either OLD or SHR. If the data sets doesn't exist it would
seem logical to code DISP=NEW.

For temporary data sets at least it is possible to edge one's bets and
code DISP=MOD, then if the data set exists the new data will be
appended, and if it doesn't exist, MOD will be treated as NEW.

The error message is not mentioned in detail, but was it perhaps "data
set not found".

Regards - Terry
```

##### ↳ ↳ Re: DISP for optional file

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-26T08:37:08+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ggne$kf0$1@aklobs.kc.net.nz>`
- **References:** `<8501a81.0302250515.27a44c8c@posting.google.com> <3e5b725e$1_8@news.onlynews.com>`

```
Terry Sambrooks wrote:

> What is meant by optional file.

An OPTIONAL file is one that need not exist when the file is OPENed.

IF an OPTIONAL file is OPENed INPUT and does not physically exist then the 
file open is successful with a status of '05' and any READ statement will 
take the AT END or INVALID KEY branch.

That is, it will act as if the file is present but empty.

If the file is OPENed I-O or EXTEND it will be created as an empty file.  

Note that a non-OPTIONAL file that does not exist should fail with a status 
'35' - file not present (or other if not '85 standard).

Some systems, such as MF, have compiler options that cause non-OPTIONAL 
files to be created automatically when OPENed I-O or EXTEND.
```

##### ↳ ↳ Re: DISP for optional file

- **From:** abhikush@rediffmail.com (maverick)
- **Date:** 2003-02-25T21:08:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8501a81.0302252108.d8c38b9@posting.google.com>`
- **References:** `<8501a81.0302250515.27a44c8c@posting.google.com> <3e5b725e$1_8@news.onlynews.com>`

```
I posted this question in www.mvshelp.com too and there too I did not
specify the error message. But for whatever it is worth give yourself
a pat in the back you did get the error message write. When I posted
this question I was in hurry dying to get back to home and hence the
lack of details.

The problem I have is I am not sure whether or not the file will be
present when I run the job. So I was planning to use "optional" in the
select statement. I gave disposition as OLD(SHR) in the JCL and there
I got the error which you have so successfully guessed. I was hoping
that with the file being optional this would work but as it turned out
this was not ANSI comittee had in mind when they designed this verb.

Anyway now I am coded an "IF" statement in the JCL checking whether
the file exists or not. I am executing this step only if the file
exists which renders the optional verb in my program useless.

Thanks for your time.

Terry Sambrooks <terry@kmsitltd.co.uk> wrote in message news:<3e5b725e$1_8@news.onlynews.com>...
> Hi,
> 
…[23 more quoted lines elided]…
> Regards - Terry
```

###### ↳ ↳ ↳ Re: DISP for optional file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-26T13:53:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HF37a.612$rM4.68362@newssrv26.news.prodigy.com>`
- **References:** `<8501a81.0302250515.27a44c8c@posting.google.com> <3e5b725e$1_8@news.onlynews.com> <8501a81.0302252108.d8c38b9@posting.google.com>`

```
"maverick" <abhikush@rediffmail.com> wrote in message
news:8501a81.0302252108.d8c38b9@posting.google.com...
>
> The problem I have is I am not sure whether or not the file will be
…[5 more quoted lines elided]…
> exists which renders the optional verb in my program useless.

Sorry I was unable to address this sooner, but I would have told you that
the OPTIONAL clause in a COBOL SELECT is totally, absolutely, completely
unrelated to the JCL.

(See also $ELSE)

MCM
```

###### ↳ ↳ ↳ Re: DISP for optional file

_(reply depth: 4)_

- **From:** abhikush@rediffmail.com (maverick)
- **Date:** 2003-02-26T19:44:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8501a81.0302261944.4e954e98@posting.google.com>`
- **References:** `<8501a81.0302250515.27a44c8c@posting.google.com> <3e5b725e$1_8@news.onlynews.com> <8501a81.0302252108.d8c38b9@posting.google.com> <HF37a.612$rM4.68362@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<HF37a.612$rM4.68362@newssrv26.news.prodigy.com>...
> "maverick" <abhikush@rediffmail.com> wrote in message
> news:8501a81.0302252108.d8c38b9@posting.google.com...
…[15 more quoted lines elided]…
> MCM

Thanks a ton everyone.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
