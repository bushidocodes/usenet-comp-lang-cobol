[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# .NET and COBOL

_4 messages · 3 participants · 2003-04_

---

### .NET and COBOL

- **From:** "scorpion53061" <mjk@charter.net>
- **Date:** 2003-04-20T09:02:36-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,microsoft.public.cn.dotnet.languages.vb
- **Message-ID:** `<va5a3vhl9oceaf@corp.supernews.com>`

```
Please help me brainstorm on this question.

In a vb.net windows app I would like to call the cobol executable(and
specify the parameters needed to run the program) ,specify the username and
password to connect, and get the results and use them somehow. I am not sure
on the syntax.

In vb.net there is a System.Process. Start command. Can that be used here?

I know it has to be possible because I can run these programs over the
internet in a command prompt window.

Please help........
```

#### ↳ Re: .NET and COBOL

- **From:** Bat Guano <bat.guano@talk21.com>
- **Date:** 2003-04-20T17:19:13+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,microsoft.public.cn.dotnet.languages.vb
- **Message-ID:** `<va5i44pc9o5811@corp.supernews.com>`
- **In-Reply-To:** `<va5a3vhl9oceaf@corp.supernews.com>`
- **References:** `<va5a3vhl9oceaf@corp.supernews.com>`

```
scorpion53061 wrote:
> Please help me brainstorm on this question.
> 
…[12 more quoted lines elided]…
> 

Are you trying to call a COM component from .NET?

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dndotnet/html/callcomcomp.asp
```

##### ↳ ↳ Re: .NET and COBOL

- **From:** "scorpion53061" <mjk@charter.net>
- **Date:** 2003-04-20T13:55:43-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,microsoft.public.cn.dotnet.languages.vb
- **Message-ID:** `<va5r9is5j1prec@corp.supernews.com>`
- **References:** `<va5a3vhl9oceaf@corp.supernews.com> <va5i44pc9o5811@corp.supernews.com>`

```
Hi bat thanks for your response.

I am not sure to be honest with you.
Starting at the beginning, what com reference would I need to add to be able
to run and capture data within a vb.net program?

"Bat Guano" <bat.guano@talk21.com> wrote in message
news:va5i44pc9o5811@corp.supernews.com...
> scorpion53061 wrote:
> > Please help me brainstorm on this question.
> >
> > In a vb.net windows app I would like to call the cobol executable(and
> > specify the parameters needed to run the program) ,specify the username
and
> > password to connect, and get the results and use them somehow. I am not
sure
> > on the syntax.
> >
> > In vb.net there is a System.Process. Start command. Can that be used
here?
> >
> > I know it has to be possible because I can run these programs over the
…[8 more quoted lines elided]…
>
http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dndotnet/ht
ml/callcomcomp.asp
>
```

###### ↳ ↳ ↳ Re: .NET and COBOL

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-04-21T21:12:21-07:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol,microsoft.public.cn.dotnet.languages.vb
- **Message-ID:** `<b11feff.0304212012.7c96429e@posting.google.com>`
- **References:** `<va5a3vhl9oceaf@corp.supernews.com> <va5i44pc9o5811@corp.supernews.com> <va5r9is5j1prec@corp.supernews.com>`

```
The MSDN link provided earlier (by the earlier poster) is a really
good link.

---------------------------

If you are interested, I wrote a book that explains this COM Interop
feature of .NET. Pardon this obvious attempt at self promotion...

The book that I wrote is called: "COBOL and Visual Basic on .NET: A
Guide for the Reformed Mainframe Programmer". It is best described as
a comprehensive guide to help mainframe programmers successfully
complete a .NET retraining effort. This book targets the COBOL/CICS
mainframe community comprised of programmers seeking a complete
transition off of the mainframe to .NET, or for those who simply wish
to broaden their knowledge with .NET.

http://www.amazon.com/exec/obidos/ASIN/1590590481/eclecticsoftw-20

http://www.eclecticsoftwaresolutions.com

http://apress.com/book/bookDisplay.html?bID=112

--------------------------
Otherwise, It sounds like you have already gotten off to a good start
with your .NET training effort. However, as part of your design, have
you considered optionally running the COBOL EXE in COM+ (Enterprise
Services) as an Out-of-process application or having it as part of a
Web Service?  Perhaps these options do not apply to your particular
situation.

In reading your emails, I would have to assume that the COBOL code is
unmanaged (non .NET). I don't think that was stated. You did say COBOL
Executable. Is your COBOL executable using Fujitsu's new COBOL.NET and
therefore is running as a managed object? If it is, then all of the
COM Interop discussion does not apply. Hence the question from the
earlier poster that asked the question "Are you trying to call a COM
component from .NET?
". 

I'm sure that the earlier poster or myself could be of more assistance
with more details about your exact business objective/requirements and
your application configuration.



"scorpion53061" <mjk@charter.net> wrote in message news:<va5r9is5j1prec@corp.supernews.com>...
> Hi bat thanks for your response.
> 
…[31 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
