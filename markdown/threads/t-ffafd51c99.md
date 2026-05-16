[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ProCobol Outer join

_2 messages · 2 participants · 2008-05_

---

### Re: ProCobol Outer join

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2008-05-10T10:57:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48257FB0.6F0F.0085.0@efirstbank.com>`

```
>>> On 5/8/2008 at 9:25 PM, in message
<mmg7245hbpg6m4ia9t8k3qd48l9mv3598t@4ax.com>, Robert<no@e.mail> wrote:
> On Thu, 8 May 2008 06:58:32 -0700 (PDT), jeff <jmoore207@gmail.com>
wrote:
> 
>>I am having a problem with a left outer join when I add conditionals.
…[36 more quoted lines elided]…
> JOIN. 

I don't know about Oracle, but in DB2 the syntax would be

Select
        A.vehicle,
        B.Vehicle,
        B.acct,
        B.MOYR,
        B.Trancode
 from  Table1 A LEFT OUTER JOIN Table2 B 
                on A.vehicle=B.vehicle
 where B.acct='1234'
  and  B.MOYR = '0502'
  and  B.trancode='80'
 order by a.vehicle

I think.  Not an expert, and i didn't test it.

Frank
```

#### ↳ Re: ProCobol Outer join

- **From:** jeff <jmoore207@gmail.com>
- **Date:** 2008-05-13T06:42:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<205363fd-7486-4813-9c3f-0616fafccab0@k13g2000hse.googlegroups.com>`
- **References:** `<48257FB0.6F0F.0085.0@efirstbank.com>`

```
On May 10, 12:57 pm, "Frank Swarbrick"
<Frank.Swarbr...@efirstbank.com> wrote:
> >>> On 5/8/2008 at 9:25 PM, in message
> <mmg7245hbpg6m4ia9t8k3qd48l9mv35...@4ax.com>, Robert<n...@e.mail> wrote:
…[61 more quoted lines elided]…
> - Show quoted text -

Thanks to all for all the great feedback.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
