[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Learning OO COBOL

_5 messages · 4 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Re : Learning OO COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DC4080.C5EB116D@home.com>`

```
Thane's at it again :-)  :-

> Been doing my homework.

DD will LUVVVV you ;-)

>Can you take a quick gander in chapter 2 of your Wilson Price OO 
>COBOL book at the section titled: MicroFocus and Ansi 
>Comparison and tell me what you see there as far as Properties, 
>Object and our other apparent differences?  Gimme a summary?

Dead easy - not too much to type :-

--------------------------------------------------------------------
As you learned earlier in this chapter, Micro Focus and ANSI use
different approaches to relating class names to external files.

Micro Focus :
	Environment Division.		*> I don't use either of these.
	Object Section.			*> Am I missing something ?
	Class-Control.
		 class-name is calls "external-name"

ANSI Standard :
	Environment Division.
	Repository.
		 class-name is calls "external-name"

ANSI specifies that a class's object data is defined under the
Working-Storage Section of the Object definition. This is permissible
with Micro Focus but only if the following compiler directive is
included prior to the first statement in the program.

	$set ooctrll(+w)

Unfortunately, this directive appears to malfunction  at times, so it is
not used in this book.......

----------------------------------------------------------------------
 Personally :-

1. I stick with M/F default directives - so no future surprises.
   Similarly I don't use any $set.....

2. Unlike a structured, my global Working-Storage is absolutely minimal
and consists primarily of copyfiles

3. I freely inter-mix Working-Storage Section and Local-Storage section
in methods :-

	*>--------------------
	method-id "method-1".
	*>--------------------
	Local-storage section.
	78 ls-value1 			value 12.
	01 ls-value2			pic 9(03)v9(02) comp-3.
	Linkage section.
	01 lnk-ReceivingValue		pic 9(02)v9(01) comp-3.
	01 lnk-Result			pic 9(03)v9(02) comp-3.
	Procedure Division using lnk-ReceivingValue
			   returning lnk-Result.
           compute ls-value2 rounded = 
		lnk-Receiving-Value * ls-value1
	   move ls-value2 to lnk-Result

	OR

	*>---------------------
	method-id. "method-2".
	*>----------------------
	Working-Storage section.
	01 ws-MessageTitle pic x(22) value "Inspection Report - ".
	Local-Storage section.
	01 ls-Title2		pic x(xx).
	01 ls-Title3		pic x(xx).
	01 ls-FinalTitle	pic x(xx).
	Linkage section.
	01 lnk-SecondTitle	pic x(xx).
	01 lnk-DateTitle	pic x(xx).
	Procedure Division using lnk-SecondTitle lnk-DateTitle.
	  move lnk-SecondTitle to ls-Title2
	  move lnk-DateTitle   to ls-Title3
	  string ws-MessageTitle delimited by size
		 ls-Title2 delimited by 2spaces
		 ls-Title3 delimited by 1space 
		 into ls-FinalTitle
	  End-string
	 
	  invoke os-Prinfile "print-title" using ls-FinalTitle
	  etc.....
----------------------------------------------------------------------

Whoops !- nearly missed it because you pointed me at Chapter 2. Then
thought I'll check his index before I finish. In his Chapter 8 he talks
about working with objects, in-line invocation :: (I think Ken
referenced this somewhere to do with C++ ????) and Properties - but he
is generalizing about OO - not specifically Merant. I hope he is -
otherwise I missed it !

The nearest I find is Vocabularies a Merant technique that let's you
write code in 'shorthand' or paraphrase the syntax, if you like - and
that makes reference to PUT and FETCH - close to GET and SET - no cigar
????

Jimmy
```

#### ↳ Re: Re : Learning OO COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38dce25c.1429001765@news.cox-internet.com>`
- **References:** `<38DC4080.C5EB116D@home.com>`

```
Posted and mailed.

On Sat, 25 Mar 2000 04:34:39 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Whoops !- nearly missed it because you pointed me at Chapter 2. Then
>thought I'll check his index before I finish. In his Chapter 8 he talks
…[3 more quoted lines elided]…
>otherwise I missed it !

This is in the standard, and is a way to get a returned value not
using a GET or SET - which means I COULD do what Ken talked about
earlier (having the GET do the calc) but not use the GET and still use
an inline shortcut to pass the data and return the response.


>
>The nearest I find is Vocabularies a Merant technique that let's you
…[3 more quoted lines elided]…
>

Not quite but porbably close.  When was NE 3.0 released?  Do you have
current maint so that you will get the update when 4.0 comes out?
```

#### ↳ Re: Re : Learning OO COBOL

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DD5BF0.6C31AE8@zip.com.au>`
- **References:** `<38DC4080.C5EB116D@home.com>`

```
> 
> In his Chapter 8 he talks about working with objects, in-line
> invocation :: (I think Ken referenced this somewhere to do with C++
> ????) and Properties - but he is generalizing about OO - not
> specifically Merant. I hope he is - otherwise I missed it !

1.  Inline (as defined in C++) is a method to do very small pieces of
code in the interface copybook so that you do not have overhead.  The
compiler put the code into your program much like a macro.  Macros
have some funny features though because they are text expansion, not
programming per se.

bad example:

you set method is:
...
	set index-property up by 1.
...

This is one line of code, doing a call is horribly inefficient, put
the code inline and there is no difference.

The other thing is that compilers typically switch off inline when
debugging to make it easier to debug (inlines confuse the hell out of
a trace).

2.  I can only generalize, I am working on a backwards OO compiler on
MVS :-}  and I do not have a recent PC compiler.

I apologize for being C++ oriented, I hope I add value to the
discussions despite my obvious ignorance of cobol specifics.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Re : Learning OO COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bmte9$43g$1@nntp9.atl.mindspring.net>`
- **References:** `<38DC4080.C5EB116D@home.com> <38DD5BF0.6C31AE8@zip.com.au>`

```
In the draft COBOL Standard the term "inline object invocation" is used to
distinguish between an explicit INVOKE statement (out-of-line) with a
reference to the returned value from an object reference.  Therefore, you can
have,

Out-of-line -
  Invoke Whatever "meth1" Using Parm-1
        returning temp-field
  Move temp-field to real-output.

  versus
InLine

Move Whatever::"meth1" Using Parm1 to Real-Output

(the "::" - double colons - are the "inline invocation operator")
```

###### ↳ ↳ ↳ Re: Re : Learning OO COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFD8CA.1F50E86E@home.com>`
- **References:** `<38DC4080.C5EB116D@home.com> <38DD5BF0.6C31AE8@zip.com.au> <8bmte9$43g$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> In the draft COBOL Standard the term "inline object invocation" is used to
…[15 more quoted lines elided]…
> 
Thanks for example Bill - as somebody once said on M/F Compuserve Forum,
"One example is worth a million words".

I haven't checked back on Will Price's text - but I'm sure he was saying
the same as you, had I bothered to digest it slowly.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
