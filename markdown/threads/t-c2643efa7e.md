[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and Perl

_1 message · 1 participant · 1998-08_

---

### Re: COBOL and Perl

- **From:** scott@softbase.com
- **Date:** 1998-08-27T00:00:00
- **Newsgroups:** comp.lang.perl.misc,comp.lang.cobol
- **Message-ID:** `<35e57697.0@news.new-era.net>`
- **References:** `<6r7fi0$9a7$1@nnrp1.dejanews.com> <6rldhj$na5@lotho.delphi.com> <6rr8ge$5a9$1@nnrp1.dejanews.com> <35E16365.CF280FEC@hankel.mersinet.co.uk> <6rs4dd$3ft$1@nnrp1.dejanews.com> <35E1ABCE.363550E1@cks.ssd.k12.wa.us> <6ru2dm$639$3@news.enterprise.net>`

```
Shaun C. Murray (scm@enterprise.net) wrote:
> >I know no COBOL, but I work in an environment where I am surrounded by
> >COBOL people.  A 'real world' example: Recently one of these poor COBOL
> >slaves (that's a term of endearment, really) came to me with a extract
> >file from a small database from one of our departments.  He was dismayed
> >that the file format was not fixed width, but tab delineated. 

> I'd be dismayed at your COBOL programmers if that was a valid complaint.  
> Post your perl code and I'm sure the group can do it in less lines in COBOL. 
> Then give it to your PCS and tell him to take a refresher course.

You have to remember:

	1) variable length record "free format" files such as UNIX
	and every OS after UNIX (Windows, OS/2, etc) uses are
	almost unknown on the mainframe. Using them is possible
	("unformatted" files are used for executable code, etc and
	can be user-created) but is poorly supported.

	2) a single COBOL program doesn't exist in isolation -- it
	is part of a system which can include other COBOL programs,
	sort utilities, etc. Even if you rewrote this one program
	in Perl, it wouldn't do you any good. You'd have to 
	rewrite everything.

People who are used to the UNIX file system and all the OSes created
after this file system became widely known just can't appreciate how
bizarre the mainframe really is.

Scott
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
