[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "new style" ODO's

_6 messages · 4 participants · 2011-01_

---

### "new style" ODO's

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2011-01-06T12:27:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com>`

```
Just as a follow-up on the "nested ODO" thread.

The current draft (ISO stage "FCD") of the COBOL revision includes

"Dynamic Capacity Tables"

These are similar to ODO's but do provide the "long requested/expected" 
feature that the actual "storage allocation" changes (grows or shrinks) 
based on the CURRENT number of occurrences specified.  (This is a very brief 
summary of a fairly complex feature.)

Such items MAY be nested (and may be nested in a "traditional" ODO)

Another (sort-of) related new feature is "any length" elementary items. 
(The structure may have a prefix or a delimiter - both existing features in 
other programming languages)

As usual,

A) The revision is a "work in progress" - so who knows how it will end up

B) Who knows which implementors (vendors or open source) will ever implement 
these features when/if the revision gets approved

C) This (like many other chagnes in this and recent Standards) is a 21st 
century solution to a 1970's problem.  I have to think that MOST businesses 
will/shyould use XML and RDB rather than "new style" ODO's.

However, I did think that I should mention the work being done in this area.

For those who are still paying for maintenance on vendor COBOL's or who are 
involved in Open Source COBOL's, you may want to contact your "implementor 
of choice" and see what their plans are for implementing dynamic capacity 
tables.  If you need "rererences" to the FCD specification of this, feel 
free to contact me off-line.
```

#### ↳ Re: "new style" ODO's

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-01-06T12:23:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7df3cbdb-6c06-47f5-8d94-44bf21416e13@i25g2000prd.googlegroups.com>`
- **References:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com>`

```
On Jan 7, 7:27 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com> wrote:
> Just as a follow-up on the "nested ODO" thread.
>
…[23 more quoted lines elided]…
> century solution to a 1970's problem.

More like an '80s solution to a '70s problem in that many languages
had those 30 years ago.

A '90s solution would have list processing built in, a 21C solution
would include tuples and dictionaries.


> I have to think that MOST businesses
> will/shyould use XML and RDB rather than "new style" ODO's.

If you have a problem and decide to use XML then you have two
problems.

There was a proposal for XML in COBOL, and I haven't cared enough to
know its status, that the XML structure be implemented in W-S and a
hierarchy where the field names are used as tag names and this is
supposed to work for input and output. While this is a COBOLy way of
doing things it seems broken by design to me.

I do read and write XML, mostly in other languages but have done it in
COBOL. Writing is easy: use a template and the program neither knows
nor cares whether the output is XML, HTML, EDIFACT or CSV. Reading
should (IMHO) be done using a parser that steps through each tag and
attribute.


> However, I did think that I should mention the work being done in this area.
>
…[4 more quoted lines elided]…
> free to contact me off-line.
```

##### ↳ ↳ Re: "new style" ODO's

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-07T12:41:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8on29mFv7tU1@mid.individual.net>`
- **References:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com> <7df3cbdb-6c06-47f5-8d94-44bf21416e13@i25g2000prd.googlegroups.com>`

```
Richard wrote:
> On Jan 7, 7:27 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com> wrote:
>> Just as a follow-up on the "nested ODO" thread.
…[33 more quoted lines elided]…
>

I agree.

>
>> I have to think that MOST businesses
>> will/shyould use XML and RDB rather than "new style" ODO's.
>

XML is a convenient solution to the transfer and manipulation of NODE 
collections. But it has been around for a very long time.


> If you have a problem and decide to use XML then you have two
> problems.
…[5 more quoted lines elided]…
> doing things it seems broken by design to me.

Yes, at the time it was proposed to include it into COBOL I simply couldn't 
see the point. There were existing 3rd party XML handling facilities and on 
Windows systems Microsoft provided a very good one. (I had been using it for 
a couple of years when the COBOL proposal came out, and I was probably a 
late adopter in this regard.)

I read through the proposed spec and I completely agree with you, it was a 
poor imitation of what was actually needed. I therefore went on record as 
being against it. It seemed a whole heap easier to simply CALL a facility 
for handling it, especially as the standard was still in some flux and could 
change.

Having become used to CALLing for XML service it was a simple step onward to 
CALL for SOAP service. I see no reason for COBOL to intrinsically include 
these facilities. I think the CICS solution is ugly, but that's just me...
>
> I do read and write XML, mostly in other languages but have done it in
…[4 more quoted lines elided]…
>

I agree with you about templated writes and Fujitsu's ISAPI and CGI 
solutions are based around this. I used it when I first developed a COBOL 
driven Web Site and found it excellent, but then I moved on to ASP.NET which 
I like more.

As for stepping through each tag and attribute on a READ, again, I agree and 
the Stream readers in C# do exactly that, with pre-written methods that save 
a whole lot of time.

It really comes down to the fact that you CAN do it in COBOL, but it is 
simply easier to do it with something else.

Pete.
```

#### ↳ Re: "new style" ODO's

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-07T12:22:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8on156FpctU1@mid.individual.net>`
- **References:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com>`

```
Bill Klein wrote:
> Just as a follow-up on the "nested ODO" thread.
>
…[32 more quoted lines elided]…
> specification of this, feel free to contact me off-line.

It's interesting, Bill.

Thanks for posting it.

It's a bloody shame that the skill, energy, and vision of many people 
(including yourself) who have lived and breathed COBOL and who have made it 
their life's work to improve COBOL, has been simply thwarted by a moribund 
and cynical standards process.

While I recognise that COBOL must decline, I have nothng but respect and 
admiration for the people who worked so hard to make it better.

My position on ODO is a matter of record and I posted recently to show 
exactly WHY COBOL sucks at things like web services.

(It requires non-trivial COBOL code to get anything like a reasonable 
solution, and even then, it is far from perfect...)

The problem that Pakku is experiencing would be solved in a few lines of C# 
and probably even less with Python...

Nevertheless, there are still a few years of COBOL ahead for many people. I 
would be very pleased if somebody DID implement the 2002 standard and if 
they then went on to include some of the features you mention, that would be 
a bonus.

However, I can't see it ever being a major player in this century.

Pete.
```

##### ↳ ↳ Re: "new style" ODO's

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-01-06T18:32:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8rci61gjmero9vjiu8hqmsk1l0soutsmn@4ax.com>`
- **References:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com> <8on156FpctU1@mid.individual.net>`

```
On Fri, 7 Jan 2011 12:22:11 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>It's a bloody shame that the skill, energy, and vision of many people 
>(including yourself) who have lived and breathed COBOL and who have made it 
>their life's work to improve COBOL, has been simply thwarted by a moribund 
>and cynical standards process.

I'm not 100% sure I agree with you.    Sometimes it is better to let
the old technology get replaced.
```

###### ↳ ↳ ↳ Re: "new style" ODO's

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-01-07T18:29:20+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8onmljFthhU1@mid.individual.net>`
- **References:** `<pQnVo.547603$pX3.528391@en-nntp-11.dc1.easynews.com> <8on156FpctU1@mid.individual.net> <f8rci61gjmero9vjiu8hqmsk1l0soutsmn@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 7 Jan 2011 12:22:11 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> the old technology get replaced.

It's a fair argument, Howard.

I just get amazed at the energy that was poured into COBOL, and the talented 
people who did it, over the 50 years. Some people are still doing it.

( I still think that adding OO support to COBOL was the most amazing piece 
of software engineering that I have seen in my lifetime.) I know there is 
nothing to be gained by raking over ashes of the past, but sometimes I DO 
feel sad that we lost something that was simple and good, and it wasn't 
ENTIRELY because the paradigm changed. )

I can agree to your point and I'll even agree it wasn't ENTIRELY down to the 
laughable Standards committee(s) that lost sight of where COBOL was supposed 
to be going. It was a bit like a "perfect storm" really, I guess. A number 
of factors all coming together at once that simply made COBOL non-viable.

Never mind. Tomorrow is another day and I have to say that the tools I am 
using this century are far better than the ones I had last century.

Progress is inexorable and it cannot happen without change.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
