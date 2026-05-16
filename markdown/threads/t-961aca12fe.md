[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL tool

_5 messages · 4 participants · 2008-09_

---

### Re: COBOL tool

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-09-05T11:28:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KJ8wk.59402$vn1.15722@fe03.news.easynews.com>`

```
Pete,
  I am not certain that this actually made it to CLC.  If so, I don't think that 
I saw any reply from you.  Any comment?
```

#### ↳ Re: COBOL tool

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-06T01:37:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6icr1nFpssa5U1@mid.individual.net>`
- **References:** `<KJ8wk.59402$vn1.15722@fe03.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:KJ8wk.59402$vn1.15722@fe03.news.easynews.com...
> Pete,
>  I am not certain that this actually made it to CLC.  If so, I don't think 
…[11 more quoted lines elided]…
>>

I didn't see this post before, Bill, but I have already responded as to why 
I don't want to re-process compiler output. Yes, the point Richard made 
regarding compiler options is valid, but we are writing a freeware tool, and 
it doesn't have to be comprehensive, provided the limitations are stated.

I have had (and am having more...) occasions where I really need to have 
offsets and lengths when I am in the middle of developing a COBOL layout 
which must also be converted to a C# structure. It hasn't been compiled yet, 
I am in the middle of doing it and I have a mouse or trackpad available. I 
want to select the parts I'm interested in and know what their offsets and 
lengths are, immediately.



>> Consider:
>>  Pic 9(4) Packed-Decimal
>> in most compilers that I have worked with, this takes 3 bytes of storage, 
>> but SOME do support "even-number unsigned" packed decimal fields without 
>> "sign nibbles".

I don't care :-)  This is not going to be all things to all people and if 
you happen to use a Bendix compiler that runs your washing machine using 
some obscure form of packed, then this isn't for you.
>>
>> Or consider the Micro Focus compiler directive IBM-COMP which impact how 
>> much storage is allocated for
>>   Pic S9(2) Binary

Yes, I considered it.  We can work on binary being 4 or 8 bytes, no problem.

>>
>>  ***
…[7 more quoted lines elided]…
>> me.

I don't disagree. But there are other implications at work here also. You'll 
probably understand better if you go to the website and download it when it 
is released next week.

Actually, my main need for this was as an extension to metadata I already 
generate from a parse of the COBOL data definition source (both SELECT and 
FD). My solution DOES cater for various formats and includes separate signs, 
synchronization, and numeric formats other than short and long floating 
point. I'm really not bothered about compiler options. If they invalidate 
the result that is something I can live with. Most people are NOT using 
esoteric compiler options and most people don't change them frequently.

The exercise with Robert is addressing other considerations as well as the 
obtaining of offset/length data.

Besides, it's a pretty cool exercise to get a mouse selection from C#, 
convert it to a data stream and feed it to a COBOL engine running in the 
.NET framework...:-)

Pete.
```

##### ↳ ↳ Re: COBOL tool

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-06T01:45:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6icrfnFpo4cpU1@mid.individual.net>`
- **References:** `<KJ8wk.59402$vn1.15722@fe03.news.easynews.com> <6icr1nFpssa5U1@mid.individual.net>`

```


"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6icr1nFpssa5U1@mid.individual.net...
>
>
…[47 more quoted lines elided]…
> problem.

Oops! It's late and I'm tired... I completely overlooked the 2 byte 
halfword...

Pete.
```

###### ↳ ↳ ↳ Re: COBOL tool

- **From:** Robert <no@e.mail>
- **Date:** 2008-09-05T12:36:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ipq2c4hn498qa73akbei4jthoa5fnk3a7p@4ax.com>`
- **References:** `<KJ8wk.59402$vn1.15722@fe03.news.easynews.com> <6icr1nFpssa5U1@mid.individual.net> <6icrfnFpo4cpU1@mid.individual.net>`

```
On Sat, 6 Sep 2008 01:45:26 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>
>
…[54 more quoted lines elided]…
>halfword...

Binary s9(2) is one byte under default byte-storage mode in Micro Focus  IBMCOMP puts it
in word-storage mode, where 1 through 4 is rounded up to two bytes. Fujitsu has only
word-storage mode, I'm fairly sure. Realia required non-default SMALLCOMP to get one byte.

SYNCHRONIZED is also involved. 

My parser assumes word-storage mode. I will add NOIBMCOMP, but not as the default.
```

###### ↳ ↳ ↳ Re: COBOL tool

_(reply depth: 4)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-05T16:48:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93a60732-9151-4e83-add1-b7982f69bf6b@o40g2000prn.googlegroups.com>`
- **References:** `<KJ8wk.59402$vn1.15722@fe03.news.easynews.com> <6icr1nFpssa5U1@mid.individual.net> <6icrfnFpo4cpU1@mid.individual.net> <ipq2c4hn498qa73akbei4jthoa5fnk3a7p@4ax.com>`

```
On Sep 6, 5:36 am, Robert <n...@e.mail> wrote:
> On Sat, 6 Sep 2008 01:45:26 +1200, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[59 more quoted lines elided]…
> word-storage mode, I'm fairly sure.

BINARY(BYTE) makes binary use between 1 and 8 bytes.

BINARY(WORD) makes binary use 2, 4 or 8 bytes.


> Realia required non-default SMALLCOMP to get one byte.
>
> SYNCHRONIZED is also involved.
>
> My parser assumes word-storage mode. I will add NOIBMCOMP, but not as the default.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
