[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Building Common Solutions

_2 messages · 2 participants · 2003-09_

---

### Building Common Solutions

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-08T22:08:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030908180803.16646.00000655@mb-m02.aol.com>`

```
I hereby abolish the thread "Re: Building a wall for division..."
And instantiate this new gizmo instead.

The idea is to discuss how COBOL and OOP, most probably Java, are going to
cohabit our business world.

There is a call for examples. Well they are hard to conjure only if you are
still in denial.

Take inventory systems in a major corporation that has a number of product
lines.There is politics in the divisions of the corp, and an inertia to the
distinct traditions of the markets the several divisions service.  

So certain things about basic inventory records are common, but some are unique
to specific divisions.  The common stuff goes in an inheritable super Class the
inheritors can be specific by adding entirely new methods and fields or doing
some overriding by same name.

Order processing may well reflect some of those division to division
differences, but Order processing can have its own way of making life mixed up
too. Some products, lets say, by company policy can be ordered as a single
order, others must be itemized distinctly, .. still others may allow for
distinct request dates within a single item (whereas that might be forbidden on
other product lines).  'Order' is common to all, 'Item' common to several, and
'date-request' applicable only to things in that 'class' (which would be called
final in oopese..

The examples simply abound. Just begin to look at all the stuff you already
know. If there is anything like a relational database or a hierarchical
database being used for what you know about. then class structures can
gravitate towards the same arrangement.

It is a certainty the folks who speak oopese are going to flood into the
business shops because that is the only thing the academic institutions are
'building.' This might well have been a gradual phenomemnon if we had had
continuous growth, but the slow sustained slow down means we are probably going
to have aburst of culture shock sometime soon. 

More generally, if there is anything in an app that you know that has data
arranged
1-to-n or n-to-m, it could be reasonable to apply OOD to future soultions for
those systems. 

The point of OOP tools is that they make the generation of programs efficient,
and infact
displace a tedious programming effort. It would be a shame to see the baby go
out with
the bath water.  OO tools are definitely an automation of the computer system
construction task.  It matters not if one resists.  Here it comes.

You want examples, we got examples. A bank has customers.  You only need one
set of manipulators for Customer.  The ATM account is a distinct class. The
Demand Deposit Account is a distinct class.  You'll have arguments trying to
inherit one form the other. You will have a food fight over single inheritance
versus multiple inheritance. Then someone will say Aspect Programming.  But you
are still in there flailing away withh your flow chart template to satiate you
flatlander COBOLese tendencies, and your personal hard copy JVM instruction set
list in the other to placate your urge to keep up with the Jones; being the
guru that you are, you know it will work ... and then someone steps up and says
"internet access to customer data and accounts, including actual fiduciaries
(transfers let's say) and establishment of repetitive payment authorizations".
Yeah, you say, we can inherit what we need, that's none of that silly GUI
stuff, we are just talking about the account methods and the customer methods.
We can fit that together!
Surely we don't want to rewrite all the account code, etc. We must be able to
glue it all together.

The best thing to build towards is an ability to THINK OBJECT.  You can not do
that
if you resist. If you are professional, an access point for you if you still
see this dimly, is that it is a very good idea to automate data processing. The
issue is not the efficiency of 
the machine, the issue is the efficiency of staff. 

Among the religions that are necessary to work in business DP are a belief in
structured code, and a belief in re-usable code. OO tools tend to force
structure into code, although it may actually tend to modularize too much.
Balance should be the goal. OO tools get people to think about code re-use from
the very start, which may well lead to more success in achieving the goal of
cost containment through code re-use. 

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: Building Common Solutions

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-09T12:25:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TEj7b.132091$0v4.9661965@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<20030908180803.16646.00000655@mb-m02.aol.com>`

```
I've read it, and I'll probably have more comments later (I agree with most
of it), but there is one issue I'd like to address now.

"RKRayhawk" <rkrayhawk@aol.com> wrote in message
news:20030908180803.16646.00000655@mb-m02.aol.com...
| I hereby abolish the thread "Re: Building a wall for division..."
| And instantiate this new gizmo instead.
<<sniped some "must read" comments>>

| The best thing to build towards is an ability to THINK OBJECT.  You can
not do
| that
| if you resist. If you are professional, an access point for you if you
still
| see this dimly, is that it is a very good idea to automate data
processing. The
| issue is not the efficiency of
| the machine, the issue is the efficiency of staff.

I agree in part. Programmer efficiency is a critical issue.
(My feeling is that we will move to system modeling tools that will generate
the source coding for us. In the mean time, I will design with code reuse in
mind. My definition of components differs from Mr. Dashwood's, but I do
build components which are easily plugged into new programs. They are not
OO.)

Efficiency of the machine is still important, and will be for at least a few
more years.

The newer machines are faster, and larger, and inefficiency can sometimes be
corrected by getting a faster, bigger machine.
But, there are still mission critical systems that must run as quickly as
possible.
Seconds aren't important, but minutes are.

When I do address efficiency problems, it is usually an I/O issue.
I expect that the I/O bottleneck will become less of an issue when we have
mammoth machines which keep frequently/recently accessed data in memory.
(IMHO. With more machines moving to 64 bit addressing, the mammoths are
coming to an installation near you soon. )
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
