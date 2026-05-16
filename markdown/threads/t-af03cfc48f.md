[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using reference modification in Inspect tallying command

_20 messages · 10 participants · 2003-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Using reference modification in Inspect tallying command

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-21T00:36:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305202336.d82bd86@posting.google.com>`

```
Hi !

Does anyone know if it is possible to use reference modification in a
inspect tallying command using AS400 cobol ?

Example :

INSPECT text TALLYING idx FOR CHARACTERS BEFORE INITIAL
searchitem(x:y).

Regards

Eric
```

#### ↳ Re: Using reference modification in Inspect tallying command

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-21T16:40:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305211540.3ecaca8b@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com>`

```
Hi Eric,

My manual says "Subscripting and reference-modification associated
with ANY (emphasis mine) identifier is evaluated only once as the
first operation in the execution of the INSPECT statement."

Why don't you give it a try and let us know how it worked?

Jack.


evanstaalduinen@chello.nl (Eric) wrote in message news:<d4075dc9.0305202336.d82bd86@posting.google.com>...
> Hi !
> 
…[10 more quoted lines elided]…
> Eric
```

##### ↳ ↳ Re: Using reference modification in Inspect tallying command

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-22T00:27:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305212327.3edef096@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com>`

```
Thanx Jack !
I did try (at least if I understand the manual correctly) but it did not work..

Regards

Eric


jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0305211540.3ecaca8b@posting.google.com>...
> Hi Eric,
> 
…[22 more quoted lines elided]…
> > Eric
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2003-05-22T14:02:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com>`

```
"Eric" <evanstaalduinen@chello.nl> wrote in message
news:d4075dc9.0305212327.3edef096@posting.google.com...
> Thanx Jack !
> I did try (at least if I understand the manual correctly) but it did not
work..

Why don't you post what you tried.  Suggestions may be forthcoming.

Best regards,
Tom Morrison
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 4)_

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-23T03:21:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305230221.17ee5ab6@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com>`

```
"Tom Morrison" <t.morrison@liant.com> wrote in message news:<FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com>...
> "Eric" <evanstaalduinen@chello.nl> wrote in message
> news:d4075dc9.0305212327.3edef096@posting.google.com...
…[7 more quoted lines elided]…
> Tom Morrison

I tried something like

INSPECT text TALLYING idx FOR ALL searchitem(x:y).
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 5)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-23T13:24:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305231224.bffe7f9@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com>`

```
Hi Eric,

It's always a good idea to post the code EXACTLY as you used it,
including the data defs of the variables. I use cut & paste to do
that.

It's happened that what a poster related was NOT the actual code he
used. Using cut and paste can avoid that.

Regards, Jack.    

evanstaalduinen@chello.nl (Eric) wrote in message news:<d4075dc9.0305230221.17ee5ab6@posting.google.com>...
> "Tom Morrison" <t.morrison@liant.com> wrote in message news:<FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com>...
> > "Eric" <evanstaalduinen@chello.nl> wrote in message
…[12 more quoted lines elided]…
> INSPECT text TALLYING idx FOR ALL searchitem(x:y).
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-05-23T15:46:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bam1e4$ehk$1@slb5.atl.mindspring.net>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com>`

```
Eric,
  From page VI-95 of the '85 Standard, the following syntax rule appears

"(2) Identifier-3, . . . , identifier-n must reference an elementary item
described, implicitly or explicitly, as USAGE IS DISPLAY."

Where identifier-3 is the item in the phrase where you want to use reference
modification.  Now there are "certain" debates about when a reference
modified data item is and is not an "elementary item" - but I assume that
your compiler is assuming that it is not.

I would be interested in knowing which other compilers do and do not accept
a referenced modified field for that operand of INSPECT.
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 5)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-25T08:30:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED0C58D.2020802@Knology.net>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com>`

```
Eric wrote:
> "Tom Morrison" <t.morrison@liant.com> wrote in message news:<FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com>...
> 
…[16 more quoted lines elided]…
> INSPECT text TALLYING idx FOR ALL searchitem(x:y).

I would expect something like this to return, given...

searchitem = "ABCDEFG"
text = "DEF JAM RECORDS IS THE DEFFEST"
x = 4
y = 3

... to add 2 to idx.  Is that what you're trying to accomplish?  Or, are 
you trying to tally something for all occurrences of text (1 character, 
maybe?) within x:y of searchitem?
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 6)_

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-26T03:26:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305260226.5d592e62@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net>`

```
> > 
> > I tried something like
…[12 more quoted lines elided]…
> maybe?) within x:y of searchitem?

That is exactly what i am trying to accomplish(idx=2). But the inspect
statement does not allow me to use reference modification on the
searchitem...
I just can't imagine it is not possible..

Eric
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-05-26T06:03:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0305260503.6aad2c50@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com>`

```
Eric, 

I hit the same problem on a project years ago using the Ca-Realia 4.2
(16 bit) compiler.   Here is my solution.

001440 01  SEARCH-FIELD.
001450     03  SF-20.
001460      04  SF-19.
001470       05  SF-18.
001480        06  SF-17.
001490         07  SF-16.
001500          08  SF-15.
001510           09  SF-14.
001520            10  SF-13.
001530             11  SF-12.
001540              12  SF-11.
001550               13  SF-10.
001560                14  SF-9.
001570                 15  SF-8.
001580                  16  SF-7.
001590                   17  SF-6.
001600                    18  SF-5.
001610                     19  SF-4.
001620                      20  SF-3.
001630                       21  SF-2.
001640                        22  SF-1.
001650                         23  FILLER PIC X.
001660                        22  FILLER PIC X.
001670                       21  FILLER PIC X.
001680                      20  FILLER PIC X.
001690                     19  FILLER PIC X.
001700                    18  FILLER PIC X.
001710                   17  FILLER PIC X.
001720                  16  FILLER PIC X.
001730                 15  FILLER PIC X.
001740                14  FILLER PIC X.
001750               13  FILLER PIC X.
001760              12  FILLER PIC X.
001770             11  FILLER PIC X.
001780            10  FILLER PIC X.
001790           09  FILLER PIC X.
001800          08  FILLER PIC X.
001810         07  FILLER PIC X.
001820        06  FILLER PIC X.
001830       05  FILLER PIC X.
001840      04  FILLER PIC X.

000670 01  SFF-1 PIC X(1).
000680 01  SFF-2 PIC X(2).
000690 01  SFF-3 PIC X(3).
000700 01  SFF-4 PIC X(4).
000710 01  SFF-5 PIC X(5).
000720 01  SFF-6 PIC X(6).
000730 01  SFF-7 PIC X(7).
000740 01  SFF-8 PIC X(8).
000750 01  SFF-9 PIC X(9).
000760 01  SFF-10 PIC X(10).
000770 01  SFF-11 PIC X(11).
000780 01  SFF-12 PIC X(12).
000790 01  SFF-13 PIC X(13).
000800 01  SFF-14 PIC X(14).
000810 01  SFF-15 PIC X(15).
000820 01  SFF-16 PIC X(16).
000830 01  SFF-17 PIC X(17).
000840 01  SFF-18 PIC X(18).
000850 01  SFF-19 PIC X(19).
000860 01  SFF-20 PIC X(20).


Figure out the length being searched and use it to decide which
inspect to use.
(Clear "Tally" first)

004500           EVALUATE S-LENG
004510             WHEN 1
004520                MOVE SF-1 TO SFF-1
004530                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-1
004540             WHEN 2
004550                MOVE SF-2 TO SFF-2
004560                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-2
004570             WHEN 3
004580                MOVE SF-3 TO SFF-3
004590                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-3
004600             WHEN 4
004610                MOVE SF-4 TO SFF-4
004620                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-4
004630             WHEN 5
004640                MOVE SF-5 TO SFF-5
004650                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-5
004660             WHEN 6
004670                MOVE SF-6 TO SFF-6
004680                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-6
004690             WHEN 7
004700                MOVE SF-7 TO SFF-7
004710                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-7
004720             WHEN 8
004730                MOVE SF-8 TO SFF-8
004740                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-8
004750             WHEN 9
004760                MOVE SF-9 TO SFF-9
004770                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-9
004780             WHEN 10
004790                MOVE SF-10 TO SFF-10
004800                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-10
004810             WHEN 11
004820                MOVE SF-11 TO SFF-11
004830                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-11
004840             WHEN 12
004850                MOVE SF-12 TO SFF-12
004860                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-12
004870             WHEN 13
004880                MOVE SF-13 TO SFF-13
004890                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-13
004900             WHEN 14
004910                MOVE SF-14 TO SFF-14
004920                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-14
004930             WHEN 15
004940                MOVE SF-15 TO SFF-15
004950                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-15
004960             WHEN 16
004970                MOVE SF-16 TO SFF-16
004980                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-16
004990             WHEN 17
005000                MOVE SF-17 TO SFF-17
005010                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-17
005020             WHEN 18
005030                MOVE SF-18 TO SFF-18
005040                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-18
005050             WHEN 19
005060                MOVE SF-19 TO SFF-19
005070                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-19
005080             WHEN 20
005090                MOVE SF-20 TO SFF-20
005100                INSPECT W-KEY TALLYING TALLY FOR ALL SFF-20
005110           END-EVALUATE



evanstaalduinen@chello.nl (Eric) wrote in message news:<d4075dc9.0305260226.5d592e62@posting.google.com>...
> > > 
> > > I tried something like
…[19 more quoted lines elided]…
> Eric
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-05-26T17:13:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED24795.AA7B61A7@shaw.ca>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <bfdfc3e8.0305260503.6aad2c50@posting.google.com>`

```


Thane Hubbell wrote:

> Eric,
>
…[12 more quoted lines elided]…
> 001530             11  SF-12.

<snip>

I guess COBOL *IS* verbose <G>
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-05-27T02:51:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c323fa$e6b00f80$15c2f943@chottel>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <bfdfc3e8.0305260503.6aad2c50@posting.google.com>`

```
How refreshing! Imagine actual COBOL code in a COBOL newsgroup.

Thane Hubbell <thaneh@softwaresimple.com> wrote in article
<bfdfc3e8.0305260503.6aad2c50@posting.google.com>...
> Eric, 
> 
…[136 more quoted lines elided]…
> evanstaalduinen@chello.nl (Eric) wrote in message
news:<d4075dc9.0305260226.5d592e62@posting.google.com>...
> > > > 
> > > > I tried something like
…[10 more quoted lines elided]…
> > > ... to add 2 to idx.  Is that what you're trying to accomplish?  Or,
are 
> > > you trying to tally something for all occurrences of text (1
character, 
> > > maybe?) within x:y of searchitem?
> > 
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 7)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-26T09:10:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED22073.1010607@Knology.net>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com>`

```
Eric wrote:
>>>I tried something like
>>>
…[17 more quoted lines elided]…
> I just can't imagine it is not possible..

That is really strange.  Of course, it's a little more code, but you can 
make a "variable-length" item...  (Replace [Max-Nbr] below with the 
maximum size your length of the search item could be)

=-=-=-=-=

01  WS-SearchItem.
     03  WS-SearchItem-Tbl  Occurs 1 to [Max-Nbr] Times
                              Depending on y  Pic X(01).
...
Move searchitem (x:y) to WS-SearchItem

Inspect text Tallying idx For All WS-SearchItem

=-=-=-=-=

Maybe that would work...  The occurs...depending on actually makes 
WS-SearchItem a variable-length field.  Since you've already got y 
defined, it'll expand or shrink based on y, and you can move the text to 
it, and use it without reference modification in the inspect statement.

Let me know if this works...  You've got my curiosity up now.  :)
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 8)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-05-26T09:53:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0305260853.5d1ff406@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <3ED22073.1010607@Knology.net>`

```
I'll be interested to hear it your idea works as well.  I like it a
whole lot better than my method.


LX-i <DanielJSNOSPAM@Knology.net> wrote in message news:<3ED22073.1010607@Knology.net>...
> Eric wrote:
> >>>I tried something like
…[41 more quoted lines elided]…
> Let me know if this works...  You've got my curiosity up now.  :)
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 8)_

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-27T01:34:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305270034.3102e000@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <3ED22073.1010607@Knology.net>`

```
Well it looks great but it does not compile.........       
I get this message :

 Message . . . . :   'WS-SEARCHITEM' in INSPECT must be      
   alphabetic, alphanumeric, or numeric display.  Statement  
   ignored.
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 9)_

- **From:** LX-i <DanielJSNOSPAM@Knology.net>
- **Date:** 2003-05-27T06:29:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ED34C2F.3090300@Knology.net>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <3ED22073.1010607@Knology.net> <d4075dc9.0305270034.3102e000@posting.google.com>`

```
Eric wrote:
> Well it looks great but it does not compile.........       
> I get this message :
…[3 more quoted lines elided]…
>    ignored.

Sheesh...  Oh well - at least there's no shortage of other ways to do 
it...  :)
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 8)_

- **From:** evanstaalduinen@chello.nl (Eric)
- **Date:** 2003-05-28T02:33:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4075dc9.0305280133.161abc56@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com> <3ED22073.1010607@Knology.net>`

```
Thanx for all the solutions
The problem was that I could not use reference modification in a
inspect statement or a FUNCTION in ANS cobol AS400
I changed my object type to CBLLE and now stuff starts to work...
This is my code :

MOVE 1 TO X                                    
MOVE 9 TO Y.                                   
PERFORM UNTIL SEARCHITEM(Y:1) NOT = SPACE      
        SUBTRACT 1 FROM Y                      
END-PERFORM.                                   
                                               
PERFORM VARYING Z FROM 1 BY 1                  
      UNTIL Z > (FUNCTION LENGTH(WS-TEXT)- Y)  
    IF WS-TEXT(Z:Y) = SEARCHITEM(X:Y)          
       ADD 1 TO IDX                            
    END-IF                                     
END-PERFORM.                                   
                                               

Regards

Eric
```

###### ↳ ↳ ↳ Re: Using reference modification in Inspect tallying command

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-05-26T11:53:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9qdnVOc1u4J20-jXTWJjA@giganews.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <8a2d426e.0305211540.3ecaca8b@posting.google.com> <d4075dc9.0305212327.3edef096@posting.google.com> <FL4za.199$Eg1.116814957@newssvr12.news.prodigy.com> <d4075dc9.0305230221.17ee5ab6@posting.google.com> <3ED0C58D.2020802@Knology.net> <d4075dc9.0305260226.5d592e62@posting.google.com>`

```

"Eric" <evanstaalduinen@chello.nl> wrote in message
news:d4075dc9.0305260226.5d592e62@posting.google.com...
> > >
> > > I tried something like
> > >
> > > INSPECT text TALLYING idx FOR ALL searchitem(x:y).
> >

Hmmm.

MOVE 0 TO idx
PERFORM VARYING z FROM 1 BY 1 UNTIL z > (FUNCTION LENG(text) - y)
    IF text(z:y) = searchitem(x:y) ADD 1 TO idx END-IF
END-PERFORM.
```

#### ↳ Re: Using reference modification in Inspect tallying command

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-05-26T19:04:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ed2650f.309260296@news.optonline.net>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com>`

```
evanstaalduinen@chello.nl (Eric) wrote:

>Hi !
>
…[6 more quoted lines elided]…
>searchitem(x:y).

Here's my solution:

01  search-key.
     05   key-byte occurs 1 to 99 depending on y pic x.

move searchitem(x:y) to search-key
move zero to idx
inspect text tallying idx for characters before initial search-key

- for higher speed -

move searchitem(x:y) to search-key
move 1 to idx
set x-text to 1
perform until idx > 999 or text(idx:y) = search-key
    search text-byte 
        when text-byte (x-text) = key-byte (1) set idx to x-text
    end-search
end-perform
subtract 1 from idx
```

##### ↳ ↳ Re: Using reference modification in Inspect tallying command

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-05-26T19:44:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0305261844.5af78aae@posting.google.com>`
- **References:** `<d4075dc9.0305202336.d82bd86@posting.google.com> <3ed2650f.309260296@news.optonline.net>`

```
Since we're swapping recipes, here's mine (the microwave version).

move +1 to idx
perform until  idx > (length of text - y) or item-found
   if text(idx:y) = searchitem(x:y)
      set item-found to true
   else
      add +1 to idx
   end-if
end-perform

if item-found
   display 'Item found at position ' idx ' of text'
else
   display 'Item not found in text' 
end-if

BTW Eric, 

What do you mean by "doesn't" work? I assume it compiles OK, but the
execution isn't to your liking.

What are you getting? Garbage data? Data you don't expect? An abend? A
loop? ?? If you told us, it may provide a clue.

Regards, Jack 



robert@wagner.net (Robert Wagner) wrote in message news:<3ed2650f.309260296@news.optonline.net>...
> evanstaalduinen@chello.nl (Eric) wrote:
> 
…[29 more quoted lines elided]…
> subtract 1 from idx
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
