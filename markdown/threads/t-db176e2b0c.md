[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LE Runtime or COBOL Intrinsic? That is the Question.

_2 messages · 2 participants · 1999-09_

---

### LE Runtime or COBOL Intrinsic? That is the Question.

- **From:** Bill Thompson <wthompson@my-deja.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sdh88$ade$1@nnrp1.deja.com>`

```


Consider this a philosophical question:  If there are two supported
ways to do something, a LE runtime service and a COBOL intrinsic
function, and though both work differently, if either provided the
result needed, which one should be used?

Consider this also:  If there are two supported ways to do something, a
LE runtime service and a COBOL extended function, and though both work
differently, if either provided the result needed, which one should be
used?

Would the answers be different if platform independence was a desired
goal?

Would the answers be different if upward release independence was a
desired goal?

TIA
	Bill
```

#### ↳ Re: LE Runtime or COBOL Intrinsic? That is the Question.

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ed9a4e@eeyore.callnetuk.com>`
- **References:** `<7sdh88$ade$1@nnrp1.deja.com>`

```
(Dons saffron robe and sips herb tea as he formulates response to Honourable
Tommo's question)

Comments interspersed...

Bill Thompson wrote in message <7sdh88$ade$1@nnrp1.deja.com>...
>
>
…[3 more quoted lines elided]…
>result needed, which one should be used?

As a philosopher, I can state without hesitation, use the COBOL intrinsic
function.
(Platform independence is a goal which is highly under recognised and
undervalued by COBOL programmers at the moment. If events unfold in the way
us philosophers predict they will, this skill will be critical to the
careers of many of today's programmers. Start thinking Universal COBOL
across platforms; don't be seduced by extensions, environments, and promises
of "much greater efficency" into staying on one vendor's platform. Get in
the habit of writing code which requires the minimum amount of change to run
on anything. Ask yourself, if your career image is to be a "390 programmer",
a "DEC VAX programmer",  a "Bendix 200 programmer, or a "computer
programmer". Philosophically, which answer shows the most vision?)


>
>Consider this also:  If there are two supported ways to do something, a
…[3 more quoted lines elided]…
>

Considered it at length. Don't use either. Invoke the old "imagination" or
"lateral thinking" function inherent in the carbon based processor you have
inside your head, and find a solution in standard COBOL, which can run on
anything...

>Would the answers be different if platform independence was a desired
>goal?
>
What do you mean, "IF"? Platform independendence HAS to be a desired goal...

>Would the answers be different if upward release independence was a
>desired goal?
>
Using standard COBOL does not obviate upward release independence. (Vendors
would go broke if it did...)

So, now you're thinking "Pete's certainly got a bee in his bonnet about
platform independence."

I'll tell you why in non-philosophical terms. Machines and environments come
and go. The heart of the language has to remain stable to accommodate this
change in the real world. If you intend to make programming your life's work
(and I wouldn't advise it if you think you are likely to live longer than
the next 15 years...) then you better learn to ignore the BS from vendors
and get comfortable in ANY environment.

Secondly, and much more importantly, every time you code a module you are
producing a solution to a specific business problem. When you move on from
your current employer (or he politely asks you to do so because the cost of
maintaining the computer system has bankrupt the company...) you will move
to another business which may well ask you to solve the same (or very
similar) problem. You could start over and rebuild the solution for the new
platform, some people are happy to do this.

Us lazy philosophers like to take the line of least resistance and provide
solutions which are general and re-usable so we don't have to do them over
again. This gives us much more time to philosophize about really important
things, like the taste of beer, and where your lap goes when you stand up...

The point is, that code which is standard and platform independent has at
least a fighting chance of running on any platform which your career changes
may require it to. If you DO have to change it, the changes are likely to be
minimal and you can soon get back to philosophizing... Maybe, you can spend
the extra time thinking about some design changes to the next system you are
going to develop...???

Seriously, I have had numerous occasions in my career where I was able to
utilize code I had written somewhere else (especially if you ascribe to the
philosophy of keeping things small and modular). After a while I learned to
think about the actual problem (rather than just do what the spec. said) and
predict what enhancements they were likely to want. Ensure the hooks are in
there and when they come back crying you can tell them to dry their eyes
because you're going to make it all better by Friday...

The business have their requirements; we, as programmers, have some of our
own. Platform independence is right at the top of mine. (I also require that
it will not be a boring job and will not cut into my drinking time and I
will be a hero if I finish it by Friday...)

Truly, the frog feels only the moonlight as he protects the lotus blossom.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
