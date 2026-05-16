[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Intertest 6.1 Problem with Cobol Optimize Parm

_3 messages · 3 participants · 2005-08_

---

### Intertest 6.1 Problem with Cobol Optimize Parm

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-08-02T20:29:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14a9f$42f00fdd$43f291c1$22875@DIALUPUSA.NET>`

```
We have IBN Enterprise Cobol for z/OS 3.3.1 and when we use the Optimize 
compiler option we are getting breakpoints set at the wrong place.  Has 
anyone else experienced this.  So far our only way around it is to turn off 
optimize in development.
```

#### ↳ Re: Intertest 6.1 Problem with Cobol Optimize Parm

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-08-02T21:49:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f0c537tpako07@news.supernews.com>`
- **References:** `<14a9f$42f00fdd$43f291c1$22875@DIALUPUSA.NET>`

```
charles hottel wrote:
> We have IBN Enterprise Cobol for z/OS 3.3.1 and when we use the
> Optimize compiler option we are getting breakpoints set at the wrong
> place.  Has anyone else experienced this.  So far our only way around
> it is to turn off optimize in development.

Which is not surprising. Optimization moves code around. For example:

PERFORM 50 TIMES
  MOVE 1 TO INDX
  ...
  END-PERFORM

Becomes:

MOVE 1 TO INDX
PERFORM 50 TIMES
  ...
  END-PERFORM.

To move a constant expression outside a loop.

Breakpoints can't really keep up with all this to-ing and fro-ing.
```

#### ↳ Re: Intertest 6.1 Problem with Cobol Optimize Parm

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-03T04:54:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D6YHe.31402$iG6.28257@tornado.tampabay.rr.com>`
- **References:** `<14a9f$42f00fdd$43f291c1$22875@DIALUPUSA.NET>`

```

"charles hottel" <jghottel@yahoo.com> wrote in message 
news:14a9f$42f00fdd$43f291c1$22875@DIALUPUSA.NET...
> We have IBN Enterprise Cobol for z/OS 3.3.1 and when we use the Optimize 
> compiler option we are getting breakpoints set at the wrong place.  Has 
> anyone else experienced this.  So far our only way around it is to turn 
> off optimize in development.

First....
I assume when you say optimize you're using the CA-Optimizer as it _should_ 
produce the necessary symbolics for Intertest in which case I'd be baffled ?

Then....

http://listserv.meduniwien.ac.at/cgi-bin/wa?A2=ind0501&L=cics-l&D=0&T=0&P=32591

I'm not sure about the assertion that it is not a problem for other 
tools....

For the debug tool which I use (cheaper for us that CA):

Usually, when you specify TEST in combination with any other suboptions 
(except NONE), the compiler options NOOPTIMIZE and OBJECT automatically go 
into effect, preventing you from debugging optimized programs. However, if 
you specify TEST(NONE,SYM) you can specify OPT, allowing you to debug 
optimized programs.

I'm not sure the benefit of having something OPTIMIZED _with_ debug 
hooks....so this makes sense.

JCE
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
