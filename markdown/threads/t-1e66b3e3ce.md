[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help

_9 messages · 5 participants · 1999-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help

- **From:** goble@kin.on.net (David. E. Goble)
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385dc67e@duster.adelaide.on.net>`

```
Hi all;

I need advise. Iam using Microfocus personal COBOL.

I have two indexed files;

01 comp
    05 key
	10 lic#      <--- Players lic# 
	10 match
	10 date  <--- date of match
   05 score

01 handicap
   05 key
	10 lic#
	10 match
	10 date
   05 score <--- handicap after latess match

Handicap is calculated after each match. Hadicap is calculated by
adding current match score with last two match scores, then dividing
by 3.

I want to be able to 

	1. enter a match date, match type, then several players match scores
	2. for this match, for each player create a new handicap record.

The problem is I am not sure how I should go about step 2.

Can anyone help me out with some ideas, advise. Thanks.
```

#### ↳ Re: Help

- **From:** nospam-dtfsdf@frontiernet.net (Douglas Flowers)
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385e3d2e.653058@News.frontiernet.net>`
- **References:** `<385dc67e@duster.adelaide.on.net>`

```
On Mon, 20 Dec 1999 06:49:04 GMT, goble@kin.on.net (David. E. Goble)
wrote:

>Hi all;
>
…[30 more quoted lines elided]…
>


Since you need to add up the last two match scores to calculate the
new handicap and you can't READ LAST on an indexed file, I would
suggest that you load all the records into a table which allows you to
get the two previous scored ...  comp-table-score(indx-2), 
comp-table-score(indx-1) and add them them to the latest score,
comp-table-score(indx). Then take this sum, divide by 3, move it to
handicap-score (along with the key for the player)  and write the
handicap record.

Your table might look like this:



77 iindx                     pic 9(3).



 01 comp-table.
     05 comp-table-record occurs 100 times,
          10 key
 	15 lic#      <--- Players lic# 
 	15 match
 	15  date  <--- date of match
           10 score




Hope thjs helps.....   Doug



- when replying via E-mail, remove "nospam-" from my address
```

#### ↳ Re: Help

- **From:** nospam-dtfsdf@frontiernet.net (Douglas Flowers)
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385e43e9.2375341@News.frontiernet.net>`
- **References:** `<385dc67e@duster.adelaide.on.net>`

```
On Mon, 20 Dec 1999 06:49:04 GMT, goble@kin.on.net (David. E. Goble)
wrote:

>Hi all;
>
…[30 more quoted lines elided]…
>


On follow-up to my previous response....  make sure you only load the
comp-records for a particular player into the table.  The do your
calculations, initialize the table and load in the next player.  The
latest score (indx) is actually the record count of the # of records
for a particular player as you load them into the array.


Doug



- when replying via E-mail, remove "nospam-" from my address
```

#### ↳ Re: Help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385DC9EF.1489D0E9@home.com>`
- **References:** `<385dc67e@duster.adelaide.on.net>`

```


"David. E. Goble" wrote:
> 
> Hi all;
> 
> I need advise. Iam using Microfocus personal COBOL.......

David,

Your request sounds suspiciously like homework. Post the code you've
written so far - and it wouldn't hurt to see the text of the original
test question.
```

#### ↳ Re: Help

- **From:** goble@kin.on.net (David. E. Goble)
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<38602c75@duster.adelaide.on.net>`
- **References:** `<385dc67e@duster.adelaide.on.net>`

```
Hi all;

I think I have found a way. Create another file to keep track of the
last three match dates.

01 track-matches
   05 key
	10 match
   05 first-date 
   05 second-date
   05 third-date

Then  to create a new comp rec...

	1. ask for the match date and match type
	5. ask for players, players scores
             	8. create new comp rec.

To create a new handicap rec...

	2. read track-matches
	3. move second-date to third-date
                 move first-date to second-date
                 move match date to first-date
	4. rewrite track-matches
             5. move score to temp
	6. read comp rec third-date
	   add third-date match score to temp
	7. read comp rec second-date
                 add second-date match score to temp
	6. create new handicap rec.

Does this solve the problem in the best way???

It looks as if it will work and is very simple code :> What do you
think?

Question should the file be an indexed or a sequential file.

If it is sequential I will need to load it into an array, then rewrite
the file at some point, But if the program crashes or the power goes,
then the array will be lost.

With an indexed file the records can be rewritren at the time of
change, but would the file parts of the indexed file be larger than a
sequential file or does it not matter either way???
```

##### ↳ ↳ Re: Help

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<83qgmv$8e6$1@news.igs.net>`
- **References:** `<385dc67e@duster.adelaide.on.net> <38602c75@duster.adelaide.on.net>`

```
This is quite a simple program.  I would just load a sequential file into
memory, do it, then write it back out.  An indexed file (I think) is
overkill.

What you say about power loss is true.  However, there is another aspect of
that.  Power loss with an open Isam file can also cause data loss.  While
there are ways around that as well, the sequential load at start and dump at
end ensures that you can only lose the current information, not historic
data.

If you are a beginner, there are some real advantages to sequential loads.
If you make the file line sequential, and place all the data in the file in
display format, you can check your data with your editor, for example.

In answer to your last question, yes, using an Indexed file would make the
file bigger, but probably not by a significant amount.  Disk is allocated on
a PC in fixed blocks, and with a tiny file such as this, you are probably
talking a single block difference.
David. E. Goble wrote in message <38602c75@duster.adelaide.on.net>...
>Hi all;
>
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3860DFEC.21D17F69@NOSPAMwebaccess.net>`
- **References:** `<385dc67e@duster.adelaide.on.net> <38602c75@duster.adelaide.on.net> <83qgmv$8e6$1@news.igs.net>`

```
donald tees wrote:
> 
> This is quite a simple program.  I would just load a sequential file into
…[7 more quoted lines elided]…
> data.

Of course, if you are creating a copy of the original file, and don't
delete the original file until everything's finished and closed - the
risks of damage due to power losses is diminished considerably.

I wonder if there will soon be a time where (virtual?) RAM is cheap and
plentiful enough that most all files will be read into memory before
they're processed.  The operating system would handle this, but will
need to have safety features.  We will simply find that old procedures
to become efficient by dropping I-O won't work the same anymore.
```

###### ↳ ↳ ↳ Re: Help

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<38613D38.D1612F7A@home.com>`
- **References:** `<385dc67e@duster.adelaide.on.net> <38602c75@duster.adelaide.on.net> <83qgmv$8e6$1@news.igs.net> <3860DFEC.21D17F69@NOSPAMwebaccess.net>`

```


Howard Brazee wrote:
> 
> donald tees wrote:
…[19 more quoted lines elided]…
> to become efficient by dropping I-O won't work the same anymore.

Slightly off topic, but to do with file crashes. If you use a timer to
close and re-open files, is there a severe penalty ?

Problem: my user is still plugging away at RM/COBOL (1980s) and if he
gets a file crash - it's horrible. He has to run a couple of programs to
compile source to run the rebuild, and sometimes records get dropped. At
his request I now use NetExpress to read in RM indexed files
sequentially, build ascii delimiteds, (which he can edit if necessary)
and re-feed to RM as ascii-delimiteds to re-create ISAMs.

Wouldn't take me much effort in NetExpress to include a timer and
close/re-open.

Currently he's working in his van, ultrasonic instruments and computer
buzzing away, entering data for 2-3 hours - and POW ! there's a
blackout. Somebody forgot to put gas in the generator sitting on the
road behind his van - of course, it's never his fault, always one of his
helpers <G>

And I like your memory resident files; un-technically it's what I refer
to as 'freeze-dried' - ideally at some stage, files could sit
'freeze-dried' in memory when the computer is shut off, to automatically
re-start when the machine is switched back on.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Help

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<83t3ha$kos$1@news.igs.net>`
- **References:** `<385dc67e@duster.adelaide.on.net> <38602c75@duster.adelaide.on.net> <83qgmv$8e6$1@news.igs.net> <3860DFEC.21D17F69@NOSPAMwebaccess.net> <38613D38.D1612F7A@home.com>`

```
I would think the "save file based on timer"(TM) method would work easiest
with simple sequential files. After all, that is what the typical modern
word processor does.

James J. Gavan wrote in message <38613D38.D1612F7A@home.com>...
>
>
…[4 more quoted lines elided]…
>> > This is quite a simple program.  I would just load a sequential file
into
>> > memory, do it, then write it back out.  An indexed file (I think) is
>> > overkill.
>> >
>> > What you say about power loss is true.  However, there is another
aspect of
>> > that.  Power loss with an open Isam file can also cause data loss.
While
>> > there are ways around that as well, the sequential load at start and
dump at
>> > end ensures that you can only lose the current information, not
historic
>> > data.
>>
…[34 more quoted lines elided]…
>Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
