[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GOBACK (was: Perform Thru/Go to vs. Perform - Compile Speed

_5 messages · 3 participants · 2004-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: GOBACK (was: Perform Thru/Go to vs. Perform - Compile Speed

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-20T04:41:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40ac2267.209277935@news.optonline.net>`
- **References:** `<108r50eojhdo57@corp.supernews.com> <217e491a.0405131229.614f6cb0@posting.google.com> <40a55e57.325467891@news.optonline.net> <217e491a.0405151217.40a0de91@posting.google.com> <40a6b384.412821264@news.optonline.net> <c8anu7$4ct$1@peabody.colorado.edu> <40a9176d.9829986@news.optonline.net> <217e491a.0405171838.3d7d72e2@posting.google.com> <40a997e8.42726445@news.optonline.net> <217e491a.0405181224.6051451e@posting.google.com> <40aab7c6.116430589@news.optonline.net> <217e491a.0405182314.6d07d36d@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote 
>
…[4 more quoted lines elided]…
>each release. 

Dot Net fully supports VB6, including mixed-mode .NET programs calling VB6
programs.There is no requirement to rewrite older code. 

> In any case VB isn't BASIC, it is just one of dozens,
>or hundreds, of implementations.

VB and VBScript dominate the Basic marketplace.

>I wouldn't have the programmer do anything in particular, but then I'm
>not a control freak trying to impose my 'better ideas'.

There is truth in this statement. You don't offer many better ideas.

>Now you have invented a completely different situation which may or
>may not be better with a parameter, or may be perfectly usable with a
>shared data item.

I must add 'shared data item' to my lexicon. Definition: a temporary variable to
which data must be copied because the language is incapable of passing the
original variable.

>If you want to CALL using some parameters _and_ to use shared data in
>WS, then nested programs do that, especially if the code is of no use
>elsewhere.  Perhaps you should look up 'GLOBAL' as it applied to
>nested programs.

I dislike GLOBAL because it is variant of EXTERNAL and 'blank common'. It's a
mechanism to defeat 'data hiding' by passing data by stealth rather than
explicitly.

>Which is just silly.  There will be only one LOCAL-STORAGE SECTION and
>one LINKAGE SECTION, data will have to be distributed amongst these
>very carefully and care taken as to which items are valid at any
>particular time.

The ENTRY header lists the linkage section variables being passed. The compiler
_could_ diagnose errors. Local-Storage is setup complete for each instance,
therefore all references are valid.

>> >> Re-entrancy is for multi-threading. Windows callbacks are not an example
of
>> >> multi-threading.
> 
…[14 more quoted lines elided]…
>> OS/2). It was not supported by Win9x and certainly not by Win3. MF support
for
>> reentrancy alone was not adequate. You needed a dispatcher and a way to lock
>> shared data.
…[20 more quoted lines elided]…
>release stuff when 3.0 was just out.

Your argument and counter-example are based on a 'cooperative' (i.e. not
preemptive) operating system that was obsolete ten years ago. This is irrelevant
in a discussion about contemporary operating systems, where multitasking is the
norm.

>> >I doubt there is much call to make existing programs thread-safe.
> 
…[4 more quoted lines elided]…
>procedures.  These are specifically written for the task.

My client has many 'external procedures' written in Cobol and dispatched via a
primative 'listener' daemon talking through an 'Oracle pipe'. Procedures and the
pipe itself are single threaded. All users and procedures are blocked while a
procedure executes. The technology wasn't home-grown; it is and continues to be
delivered by SAP. 

Oracle provides an alternative 'listener' that IS multithreaded and assumes the
procedures are thread-safe, not just reentrant. The challenge is to make
existing Cobol procedures thread-safe.

IBM mainframers have a large volume of similar programs because DB2 makes it
easier. It supports Stored Procedures written in Cobol. It doesn't require them
to be External Procedures. It doesn't require the programmer do anything special
because it constructs a Working-Storage for each instance. In effect, it turns
Working-Storage into Local-Storage. CICS does the same.

>You should learn how machines with a single CPU do multi-tasking, it
>is called timeslicing. 

The operating system I wrote knew how to timeslice.

>> If you want to do more advanced things, such as parallel processing to make
>> your application SCALABLE, you can't do it with PERFORMed paragraphs. 
…[5 more quoted lines elided]…
>out-of-line.

Suppose the program needs to do process A, B and C. A traditional Cobol program
would say:
perform A
perform B
perform C
Execution time would be the sum of A+B+C. 

A multithreaded program would say:
start A
start B
start C
wait for A and B and C
Execution time would be the longest of the three.

>Your analogy is inappropriate, I may trust another dog's better ideas.

Quotation kept for its bile content.
```

#### ↳ Re: GOBACK

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-05-20T05:13:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40AC3E68.9050105@optonline.net>`
- **In-Reply-To:** `<40ac2267.209277935@news.optonline.net>`
- **References:** `<108r50eojhdo57@corp.supernews.com> <217e491a.0405131229.614f6cb0@posting.google.com> <40a55e57.325467891@news.optonline.net> <217e491a.0405151217.40a0de91@posting.google.com> <40a6b384.412821264@news.optonline.net> <c8anu7$4ct$1@peabody.colorado.edu> <40a9176d.9829986@news.optonline.net> <217e491a.0405171838.3d7d72e2@posting.google.com> <40a997e8.42726445@news.optonline.net> <217e491a.0405181224.6051451e@posting.google.com> <40aab7c6.116430589@news.optonline.net> <217e491a.0405182314.6d07d36d@posting.google.com> <40ac2267.209277935@news.optonline.net>`

```
Robert Wagner wrote:
> riplin@Azonic.co.nz (Richard) wrote:
> 
…[173 more quoted lines elided]…
> Execution time would be the longest of the three.

Wait a second here. Has the Perform been promoted to
the program level?  Much of the code, it seems to me,
would not produce correct output if the system began
to execute the code in a list of perform statements
without some knowledge of the dependence of one on another.

Perhaps the problem here is that terminology has not
been settled upon. Just because you hear a quack,
you can't conclude that a duck is in the room.

Warren Simmons


> 
> 
…[3 more quoted lines elided]…
> Quotation kept for its bile content.
```

##### ↳ ↳ Re: GOBACK

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-21T00:30:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40ad4c46.285544927@news.optonline.net>`
- **References:** `<108r50eojhdo57@corp.supernews.com> <217e491a.0405131229.614f6cb0@posting.google.com> <40a55e57.325467891@news.optonline.net> <217e491a.0405151217.40a0de91@posting.google.com> <40a6b384.412821264@news.optonline.net> <c8anu7$4ct$1@peabody.colorado.edu> <40a9176d.9829986@news.optonline.net> <217e491a.0405171838.3d7d72e2@posting.google.com> <40a997e8.42726445@news.optonline.net> <217e491a.0405181224.6051451e@posting.google.com> <40aab7c6.116430589@news.optonline.net> <217e491a.0405182314.6d07d36d@posting.google.com> <40ac2267.209277935@news.optonline.net> <40AC3E68.9050105@optonline.net>`

```
Warren Simmons <wsimmons5@optonline.net> wrote:

>Robert Wagner wrote:
 
>> Suppose the program needs to do process A, B and C. A traditional Cobol
program
>> would say:
>> perform A
…[15 more quoted lines elided]…
>without some knowledge of the dependence of one on another.

The assumption is no dependence. For example:

perform get-customer-information
perform get-product-information
perform get-order-form-template
.. followed by ..
perform present-order-form

Surely you've seen Cobol code like that. I have.

>
>Perhaps the problem here is that terminology has not
…[11 more quoted lines elided]…
>> Quotation kept for its bile content.
```

###### ↳ ↳ ↳ Re: GOBACK

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-05-21T04:27:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40AD8517.2080400@optonline.net>`
- **In-Reply-To:** `<40ad4c46.285544927@news.optonline.net>`
- **References:** `<108r50eojhdo57@corp.supernews.com> <217e491a.0405131229.614f6cb0@posting.google.com> <40a55e57.325467891@news.optonline.net> <217e491a.0405151217.40a0de91@posting.google.com> <40a6b384.412821264@news.optonline.net> <c8anu7$4ct$1@peabody.colorado.edu> <40a9176d.9829986@news.optonline.net> <217e491a.0405171838.3d7d72e2@posting.google.com> <40a997e8.42726445@news.optonline.net> <217e491a.0405181224.6051451e@posting.google.com> <40aab7c6.116430589@news.optonline.net> <217e491a.0405182314.6d07d36d@posting.google.com> <40ac2267.209277935@news.optonline.net> <40AC3E68.9050105@optonline.net> <40ad4c46.285544927@news.optonline.net>`

```
Robert Wagner wrote:
> Warren Simmons <wsimmons5@optonline.net> wrote:
> 
…[54 more quoted lines elided]…
> 
In the context of the presentation in either case
does not IMHO insure that these paragraphs can be
executed in this manner. There must be some other
indication. Otherwise, anyone reading your message
would have a good notion that this applied to
successfully listed performs in a source. I expect
you will ignore my comment, but I suggest you provide
more detail when you "explain" things to any group
for a greater degree of clarity.

Warren Simmons
```

###### ↳ ↳ ↳ Re: GOBACK

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-20T22:48:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405202148.2dc86b18@posting.google.com>`
- **References:** `<108r50eojhdo57@corp.supernews.com> <c8anu7$4ct$1@peabody.colorado.edu> <40a9176d.9829986@news.optonline.net> <217e491a.0405171838.3d7d72e2@posting.google.com> <40a997e8.42726445@news.optonline.net> <217e491a.0405181224.6051451e@posting.google.com> <40aab7c6.116430589@news.optonline.net> <217e491a.0405182314.6d07d36d@posting.google.com> <40ac2267.209277935@news.optonline.net> <40AC3E68.9050105@optonline.net> <40ad4c46.285544927@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote 

> The assumption is no dependence. For example:

You assume that at your peril.
 
> perform get-customer-information
> perform get-product-information

In my systems the customer type or class is used to set the price when
the product is retrieved.  An order usually has several products, so
that would follow on.

> perform get-order-form-template
> .. followed by ..
> perform present-order-form
> 
> Surely you've seen Cobol code like that. I have.

'Like that' maybe, without dependencies, no.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
