[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passwords

_7 messages · 3 participants · 2017-08_

---

### Passwords

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-08T19:36:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<euv09lF37ejU1@mid.individual.net>`

```
I read this with some interest:

https://www.theverge.com/2017/8/7/16107966/password-tips-bill-burr-regrets-advice-nits-cybersecurity

Don't you just hate those sites where they enforce a certain password
structure on you "for your own good" because they "know what is accepted
best practice".

Over the years I've had a few "to and fros" with some of these, my main
argument being that it is MY password, not theirs. I should be able to
make whatever I want and if it gets cracked, that is my problem.

(I never "won" any of these arguments because people who blindly follow
what someone says, without thinking about it or considering counter
arguments, simply don't have the imagination to be able to easily change
their practices and procedures once implemented. I don't even really
mind them not dong anything, it is the REASON they do nothing that bugs
me:"We implement our password policy in accordance with what are
considered industry best practices, sorry if you find it inconvenient.")

Even if you made a powerful argument for NOT doing it, they STILL won't
change it.

(BTW, if you register on the PRIMA site we make NO effort to enforce a
password structure on you and you can have whatever you want. It is YOUR
password. You can also change it and unregister yourself easily from our
site. The code that drives this was written from scratch, by me, and so
there is no "standard package javascript login". It does mean that you
should READ any comments which might appear so the process will succeed...)

It's good to see an article that vindicates what I have believed for a
number of years, but don't expect any sites to be changing their login
policy any time soon.

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: Passwords

- **From:** "robertwessel2" <ua-author-4329810@usenetarchives.gap>
- **Date:** 2017-08-08T21:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<euv09lF37ejU1@mid.individual.net>`
- **References:** `<euv09lF37ejU1@mid.individual.net>`

```
On Wed, 9 Aug 2017 11:36:51 +1200, pete dashwood
wrote:

› I read this with some interest:
› 
…[30 more quoted lines elided]…
› policy any time soon.


While I certainly agree than many of the password policies are silly,
and even counterproductive*. But that's not the same as suggesting
*no* requirements. It may be your password, but if I'm a bank and
it's to *your* checking account, I have a major interest in it not
being compromised. You can claim that it'll be your problem if it's
cracked, but it really won't work out that way in the end. So I don't
want you to make the password "pete" or your birthday. Even if just
to protect you from yourself. Plenty of people will chose *really*
bad passwords if you let them.

Again, I'm not saying that many of the policies in place aren't
stupid. And you want stupid? My bank started enforcing complexity
requirements for *account names*. Yeah, so my bank signon now has a
two digit number attached to the account name. They actually made me
change it. This is one of the biggest banks in the world. *sigh*


*A few years ago I had to update the password generator for the
installation program for a Windows service in one of our products. The
service ran under its own login, and that login was never intended to
be used by anyone directly, just to run the service (rights would be
assigned to that user ID, etc.). So we used the Windows CS random
number generator to generate a 32 hex digit string for the password.
Of course we ended up with a customer for whom that failed the
complexity requirements, and where it was politically impossible to
override those for this installation. The generated passwords now
have exactly the same entropy, but the different positions get a
different set of 16 characters to use (position 1/6/11/16/etc. still
has 0-9,a-f, but 2/7/12/17/etc. uses g-u, etc.). The installation
program will now prompt the installer for a password if the random
generator fails a couple of times.
```

##### ↳ ↳ Re: Passwords

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-10T05:44:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7046bcc4bb-p2@usenetarchives.gap>`
- **References:** `<euv09lF37ejU1@mid.individual.net> <gap-7046bcc4bb-p2@usenetarchives.gap>`

```
On 9/08/2017 1:31 PM, Robert Wessel wrote:
> On Wed, 9 Aug 2017 11:36:51 +1200, pete dashwood
> wrote:
…[3 more quoted lines elided]…
>>
https://www.theverge.com/2017/8/7/16107966/password-tips-bill-burr-regrets-advice-nits-cybersecurity
>>
>> Don't you just hate those sites where they enforce a certain password
…[23 more quoted lines elided]…
>> should READ any comments which might appear so the process will
succeed...)
>>
>> It's good to see an article that vindicates what I have believed for a
…[6 more quoted lines elided]…
> *no* requirements.

I think that's a very fair point, which I certainly missed.


It may be your password, but if I'm a bank and
> it's to *your* checking account, I have a major interest in it not
> being compromised. You can claim that it'll be your problem if it's
…[3 more quoted lines elided]…
> bad passwords if you let them.

Yes, there is a big difference between protecting someone's Bank
account, and giving them access to material that the fate of Nations
does not hang on. I take your point.

>
> Again, I'm not saying that many of the policies in place aren't
…[3 more quoted lines elided]…
> change it. This is one of the biggest banks in the world. *sigh*

I guess the key word there is "enforcement". Nobody likes that. I have
to say that if I thought my Bank was being unreasonable, I'd definitely
consider changing Banks... it's not like we don't have a choice... I am
part of a "focus group" for my Bank and they periodically ask questions
about how they can make things better and also new ideas they are
kicking around.

They've started to press getting people to use phone banking more...
(Did you know that the solution to ALL IT problems is to "go to the app
store and buy an app"? The generation who have mobile phones grafted to
their heads at birth can't see what the problem is when IT problems
occur...)

I stated clearly and unequivocally that if they MANDATE the use of phone
banking, I will certainly move my accounts to another provider. As an
OPTION, sure, no problem; REQUIRED, absolutely NOT.

I should mention that online banking with this Bank is a joy, and they
have evolved a brilliant simple, clear, and very useful online Banking
system. I've been using it for nearly 20 years now and watched it get
better and better.

They do have a password pattern requirement but it is not onerous. There
was talk about requiring periodic changes to the password but they
dropped it in response to the Focus Group. (I was pleased to see that
Bill Burr also agrees that it really doesn't help much.) They do use
fuzzy logic to support the password login, and there have been a few
occasions where the system has challenged my login (usually when not
from the usual IP address), but it resolves easily and quickly.


>
>
…[14 more quoted lines elided]…
>
I'm a firm believer (persuaded by experience over about 8 years now)
that the "usual" 32 digit "Licence code" is a very poor way to protect
software. In fact, ANY form of user identification is too easily
bypassed. (I would agree that biosecurity markers are more difficult...)

What is REALLY needed is NOT WHO's running your software, but whether
the software should be allowed to run AT ALL...

ALL PRIMA software is now protected with our Remote Application
Validation (RAV) system. No passwords, no Licence strings, no user
identification (unless you want it in your own application for reasons
of your own.) it is simple: If the software is allowed to run, it runs;
if it is NOT allowed to run, it doesn't. And there are a large number of
possible "levels" of access if you want them, or simple black and white
if you don't.

I wrote the RAV system in response to a client request about 8 years ago
and it has been continually enhanced and improved in the interim. It is
NOT unbreakable (I don't believe that ANY system which has a legitimate
access path is "unbreakable"...); but the effort you would need to go to
in order to break it seems to be enough to deter most people. 128 bit
encryption is scoffed at in some quarters but we find it very useful.

http://primacomputing.co.nz/PRIMAMetro/Rav.aspx

Thanks for your response and some interesting points, Robert,

Pete.--
I used to write COBOL; now I can do anything...
```

#### ↳ Re: Passwords

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-08-09T07:45:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<euv09lF37ejU1@mid.individual.net>`
- **References:** `<euv09lF37ejU1@mid.individual.net>`

```
In article ,
pete dashwood wrote:
› I read this with some interest:
› 
…[8 more quoted lines elided]…
› make whatever I want and if it gets cracked, that is my problem.

Whoever owns the swimming-pool gets to dictate the bathing-suit
requirements... it may be your password, Mr Dashwood, but it is THEIR
system.

DD
```

##### ↳ ↳ Re: Passwords

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-10T05:46:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7046bcc4bb-p4@usenetarchives.gap>`
- **References:** `<euv09lF37ejU1@mid.individual.net> <gap-7046bcc4bb-p4@usenetarchives.gap>`

```
On 9/08/2017 11:45 PM, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[17 more quoted lines elided]…
› 
I swim naked...wherever I legally can and without offending others.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Passwords

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-08-10T14:33:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7046bcc4bb-p5@usenetarchives.gap>`
- **References:** `<euv09lF37ejU1@mid.individual.net> <gap-7046bcc4bb-p4@usenetarchives.gap> <gap-7046bcc4bb-p5@usenetarchives.gap>`

```
In article ,
pete dashwood wrote:
› On 9/08/2017 11:45 PM, doc··f@pa··x.com wrote:
›› In article ,
…[18 more quoted lines elided]…
› I swim naked...wherever I legally can and without offending others.

Being told this enriches my life immeasurably. Permit me to respond in
kind:

Years ago a young woman asked me, with playful seriousness, 'What do you
think of when you Q-tip your ears?'

(explanatory note: a Q-tip is a cotton swab which - despite strong
warnings from the manufacturer and countless paediatricians and sundry
otologists - is used clean ears; in typical American fashion (kleenex,
band-aid, post-it note) the brand name has become the generic... see also
http://www.qtips.com/ )

I responded 'If I'm doing it just right I think 'This is the sensation
which is closest to sex without actually doing it'.'

DD
```

###### ↳ ↳ ↳ Re: Passwords

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-10T22:30:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7046bcc4bb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7046bcc4bb-p6@usenetarchives.gap>`
- **References:** `<euv09lF37ejU1@mid.individual.net> <gap-7046bcc4bb-p4@usenetarchives.gap> <gap-7046bcc4bb-p5@usenetarchives.gap> <gap-7046bcc4bb-p6@usenetarchives.gap>`

```
On 11/08/2017 6:33 AM, doc··f@pa··x.com wrote:
› In article ,
› pete dashwood   wrote:
…[35 more quoted lines elided]…
› which is closest to sex without actually doing it'.'

Gives a whole new dimension to being "hard of hearing"... :-)

Pete.

I used to write COBOL; now I can do anything...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
