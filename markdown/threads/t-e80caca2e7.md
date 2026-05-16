[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Random number generator

_6 messages · 6 participants · 2006-08 → 2006-09_

---

### Random number generator

- **From:** "djeanne" <djeanne75@gmail.com>
- **Date:** 2006-08-23T07:59:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`

```
Hi all,

I am looking for a way to generate random numbers with good quality.
The system the generator should be working on is an MVS system.

Does anyone have a clue of how to do it ?

Thanks in advance,

Djeanne.
```

#### ↳ Re: Random number generator

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2006-08-23T11:49:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h5uoe2lvhs37dbqau44pgh7kusuiaku09q@4ax.com>`
- **References:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`

```
On 23 Aug 2006 07:59:21 -0700, "djeanne" <djeanne75@gmail.com>
enlightened us:

>Hi all,
>
…[7 more quoted lines elided]…
>Djeanne.

In your Cobol manual look up Function Random (x).

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I can levitate birds. No one cares."
--Steven Wright
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: Random number generator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-08-23T17:02:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JS%Gg.649707$C62.450163@fe12.news.easynews.com>`
- **References:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com> <h5uoe2lvhs37dbqau44pgh7kusuiaku09q@4ax.com>`

```
although the Intrinsic Function "RANDOM" is available with all currently 
supported COBOL's on MVS (z/OS), there is also an LE callable service for it 
too.  As I recall, the two do NOT generate the same series of numbers - so you 
can use either one (or a combination of the two <G>).
```

#### ↳ Re: Random number generator

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-08-24T22:14:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_wpHg.10619$395.7985@edtnps90>`
- **References:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`

```

"djeanne" <djeanne75@gmail.com> wrote in message 
news:1156345158.905954.300540@74g2000cwt.googlegroups.com...
> Hi all,
>
…[3 more quoted lines elided]…
> Does anyone have a clue of how to do it ?

    Define "good quality". There are RNGs that are cryptographically secure, 
although lead to poor stastistical behaviour for simulations, and vice versa 
(good for statistical simulations, but cryptographically poor).

    - Oliver
```

#### ↳ Re: Random number generator

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-08-25T05:14:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1HvHg.691144$Fs1.64054@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`
- **References:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`

```


djeanne wrote:
> Hi all,
> 
…[8 more quoted lines elided]…
> 

There's lots of resources on the web:
http://en.wikipedia.org/wiki/Pseudorandom_number_generator

Linear Congruence was described by Donald Knuth over 30 years ago, and 
would be relatively simple to implement in COBOL.  It's fairly good 
for simulations, not good at all for cryptographic purposes.
http://en.wikipedia.org/wiki/Linear_congruential_generator

You might consider researching RC4 if you need a Pseudo-Random Number 
generator that has some desireable qualities for cryptography.  It can 
also be implemented in COBOL, with a little work.
http://en.wikipedia.org/wiki/RC4
```

#### ↳ Re: Random number generator

- **From:** Paddy.Coleman@microfocus.com
- **Date:** 2006-09-06T08:08:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1157555310.590118.122730@m73g2000cwd.googlegroups.com>`
- **References:** `<1156345158.905954.300540@74g2000cwt.googlegroups.com>`

```

djeanne wrote:
> Hi all,
>
…[7 more quoted lines elided]…
> Djeanne.

Hi Djeanne,

Saw your posting about random numbers.  I created the following
programs under Micro Focus Net Express but they should move to MVS OK.

This program should be created and saved as CALLRAND.CBL.

       working-storage section.

       01  ws-max                      pic 9(3).
       01  ws-result                   pic 9(3).
       01  ws-coords.
           03  ws-y-coord              pic 9(2).
           03  ws-x-coord              pic 9(2).
       01  ws-results-table.
           03  ws-results              pic 9(3) occurs 255.
       01  ws-counter                  pic x(2) comp-5.

       procedure division.

           display
              spaces at 0101
              "Random Number Generator" at 0101
           end-display.

           move 255 to ws-max.
           move 3 to ws-y-coord.
           move 1 to ws-x-coord.
           initialize ws-results-table.

           perform 352 times

              call "calcrand"
                 using ws-max
                       ws-result
              end-call

              display ws-result at ws-coords
              add 1 to ws-results(ws-result)

              if ws-y-coord < 24
                 add 1 to ws-y-coord
              else
                 move 3 to ws-y-coord
                 add 5 to ws-x-coord
              end-if

           end-perform.

           stop " ".

           display spaces at 0101.

           perform varying ws-counter from 1 by 1
                 until ws-counter > 255
              display ws-counter "   " ws-results(ws-counter)
           end-perform.

           stop run.

This program should be created and saved as CALCRAND.CBL.

       working-storage section.

       01  ws-first-time               pic 9(1) value 0.
       01  ws-rnd-seed-x               pic x(8).
       01  ws-rnd-seed-9               redefines ws-rnd-seed-x
                                       pic 9(8).
       01  ws-rnd-dbl                  comp-2.
       01  ws-rnd-int                  pic x(1) comp-x.

       linkage section.

       01  ls-max                      pic 9(3).
       01  ls-result                   pic 9(3).

       procedure division using ls-max
                                ls-result.

      * -- Generate the random seed value.

           if ws-first-time = 0

              move 32768 to ws-rnd-seed-9

              perform until ws-rnd-seed-9 < 32768
                 accept ws-rnd-seed-x from time
                 move function reverse(ws-rnd-seed-x) to ws-rnd-seed-x
                 compute ws-rnd-seed-9 = ws-rnd-seed-9 / 3060
              end-perform

              compute ws-rnd-dbl = function random(ws-rnd-seed-9)
              move 1 to ws-first-time

           end-if.

      * -- Generate a random number between 1 and LS-Max.

           compute ws-rnd-dbl = function random().
           compute ws-rnd-int = ws-rnd-dbl * ls-max.
           move ws-rnd-int to ls-result.
           add 1 to ls-result.

           exit program.
           stop run.

I hope this helps.  If you have any questions then drop me a line.

Paddy Coleman
Micro Focus Product Support
Newbury, UK
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
