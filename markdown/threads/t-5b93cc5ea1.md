[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Anti-virus conclusions

_4 messages · 2 participants · 2013-01_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Anti-virus conclusions

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-01-21T18:55:12+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<am43i1Ft5hvU1@mid.individual.net>`

```
I have now completed weeks of my own testing on various anti-virus programs.

The main conclusion:

"Don't believe what they say... the ONLY real test is how it runs on YOUR 
systems..."

I won't go into all the tests I did or what products I did them on because 
some people are likely to get completely different results and it isn't 
really fair for my opinions to possibly cloud someone else's experience.

What I CAN say is:

1. Some products scan much quicker than others.
2. Some products install much quicker than others.
3. Some products install much easier than others.
4. Sadly, too many of these systems just will not uninstall properly. I 
already mentioned Norton which simply destroyed the entire system when an 
attempt was made to uninstall it, but they are not alone...
5. Some of these systems (written in C or C++) distribute incompatible C 
runtimes that mean that exceptions in the processing are not handled and the 
results are less than you would want. (Frequent popups complaining about 
missing entry points in the C runtime library  (msvcrt32.dll) don't inspire 
confidence in a product...)
6. After having to "hand wash" the registry on at least 2 occasions, not to 
mention usng a very good Registry cleaner on others, I have come to the 
conclusion that some of these products should be banned... It is no fun 
going through 100 or more registry entries because the files referred to 
cannot be removed (even with industrial strength unlockers applied to 
them...)

BOTTOM LINE:

1. Use a free trial and see how it works on your system. If they don't have 
a free trial, don't entertain buying or using it.
2. Before installing any of these products make sure you have a system 
restore point and, ideally, a partition image of your boot drive.
3. Be prepared to pay for full protection; free is nice, but it isn't enough 
if you spend a lot of time connected to networks.

What did I end up with?

AVG (paid version). It was the only one that uninstalled sweetly and 
cleanly, had all of the functionality I require, and is unobtrusive, does 
not slow the booting and running of the system excessively, and is stable. 
It is not the fastest, and it is not the cheapest, but it meets my 
requirements.

(This is NOT a general endorsement; as noted above, results on YOUR system 
may be completely different...)

Pete.
```

#### ↳ Re: OT: Anti-virus conclusions

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-01-21T07:47:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc8e7163-88b0-436d-a8d9-9b008017a689@googlegroups.com>`
- **In-Reply-To:** `<am43i1Ft5hvU1@mid.individual.net>`
- **References:** `<am43i1Ft5hvU1@mid.individual.net>`

```
On Monday, January 21, 2013 5:55:12 AM UTC, Pete Dashwood wrote:
> I have now completed weeks of my own testing on various anti-virus programs. 

Thanks for the info Pete. Did you try Zonealarm's antivirus?
```

##### ↳ ↳ Re: OT: Anti-virus conclusions

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-01-22T12:09:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<am6068FcarrU1@mid.individual.net>`
- **References:** `<am43i1Ft5hvU1@mid.individual.net> <fc8e7163-88b0-436d-a8d9-9b008017a689@googlegroups.com>`

```
Alistair Maclean wrote:
> On Monday, January 21, 2013 5:55:12 AM UTC, Pete Dashwood wrote:
>> I have now completed weeks of my own testing on various anti-virus
>> programs.
>
> Thanks for the info Pete. Did you try Zonealarm's antivirus?

No. I used it many years ago (as a firewall) and was not impressed.

That. of course, is totally unfair to the product in its present 
incarnation. But I couldn't test every product with my own systems and it 
became very tedious manually removing the ones that wouldn't uninstall 
properly, to regain a clean system for the next one.

I tested a total of 5, some of which are not household names. In the end I 
decided AVG would be good for me and it is. I ran a complete scan of the 
main development machine last night (nearly 3 million files, but it was 
configured to scan only "infectable" file types and the number was somewhere 
in the high 500,000s). It found a bunch of tracking cookies and nothing 
actually harmful. I got a good deal for two years and have paid up (it was 
less than Norton who I have just had to write off...)

My post here is intended to relay only my own experience. I am not a testing 
lab for anti-virus any more than I intend to become a help desk for Windows 
8... :-)

Pete..
```

###### ↳ ↳ ↳ Re: OT: Anti-virus conclusions

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-01-22T03:36:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b94a9c0-33c1-4963-9050-a0f348d2cda0@googlegroups.com>`
- **In-Reply-To:** `<am6068FcarrU1@mid.individual.net>`
- **References:** `<am43i1Ft5hvU1@mid.individual.net> <fc8e7163-88b0-436d-a8d9-9b008017a689@googlegroups.com> <am6068FcarrU1@mid.individual.net>`

```
On Monday, January 21, 2013 11:09:58 PM UTC, Pete Dashwood wrote:
> In the end I decided AVG would be good for me and it is. I ran a complete scan of the main development machine last night (nearly 3 million files, but it was configured to scan only "infectable" file types and the number was somewhere in the high 500,000s). It found a bunch of tracking cookies and nothing actually harmful. 

Thanks Pete. I have recently used AVG to scan for rootkits on a donated (old) laptop. It found 28 occurences of one rootkit. I cleaned up the system and it ran much faster. However, it still crawls when doing windows updates.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
