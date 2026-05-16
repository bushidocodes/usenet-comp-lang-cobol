[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus

_6 messages · 5 participants · 2010-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus

- **From:** Hugh Porter <shug.porter@googlemail.com>
- **Date:** 2010-10-21T04:50:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com>`

```
Hello,

Has anyone been involved in migrating legacy COBOL applications from a
mainframe using Micro Focus and would like to give their verdict? I
understand that MF probably own this area, but are they decent
solutions and support?

Many thanks.
```

#### ↳ Re: Micro Focus

- **From:** HansJ <hans.igel@googlemail.com>
- **Date:** 2010-10-21T09:00:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bb79e63-4eaf-494a-93d1-c5334bf0ecb7@a36g2000yqc.googlegroups.com>`
- **References:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com>`

```
On 21 Okt., 13:50, Hugh Porter <shug.por...@googlemail.com> wrote:
> Hello,
>
…[5 more quoted lines elided]…
> Many thanks.

Hugh, what source and target platform are you talking about?

Micro Focus does certainly not "own" this area, they have solutions to
help, but others do as well.
```

#### ↳ Re: Micro Focus

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-10-21T09:25:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dc296845-4cc7-4f6d-8c35-48c13ada3ef6@c10g2000yqh.googlegroups.com>`
- **References:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com>`

```
On Oct 21, 12:50 pm, Hugh Porter <shug.por...@googlemail.com> wrote:
> Hello,
>
…[5 more quoted lines elided]…
> Many thanks.

I know of one UK company which has decided to ditch it's MF licences
as they were either not prepared to make the effort to set up PC based
test environments or found it to be too difficult. I have no problem
with MF Cobol except for that it wants to encompass everything in to
discrete projects.
```

##### ↳ ↳ Re: Micro Focus

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-10-23T12:30:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UQFwo.14$kS.3@newsfe17.iad>`
- **In-Reply-To:** `<dc296845-4cc7-4f6d-8c35-48c13ada3ef6@c10g2000yqh.googlegroups.com>`
- **References:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com> <dc296845-4cc7-4f6d-8c35-48c13ada3ef6@c10g2000yqh.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 21, 12:50 pm, Hugh Porter <shug.por...@googlemail.com> wrote:
> 
…[14 more quoted lines elided]…
> discrete projects.

You have already expanded on your above statement about the UK company 
and Bill has also indicated reasons for any lack of success.

I'm concentrating on the last sentence - discrete projects. I get the 
impression that you are not too excited about IDEs; you're not the only 
one, I can recall at least two others have expressed that opinion over 
the years.

Yes, if you have a project Accounts Payable/Bought Ledger, then you have 
a customized project, but when you go into real-time production mode you 
have various DLLs, some specific to M/F utilities and those which you 
may build from your own source.

I'm almost there on a OO version of 'Rosetta - Bottles of Beer', using 
the guts of what Bruce and Pete posted - it would be difficult to fault 
the logic they used, with Pete enhancing it by using the indices to get 
at the entries in the Name tables. Yes, it will include a recursive 
invoke of a method.

Nevertheless I sympathize with your complaint that "It's a drag to go 
through output of all the permutations". Pete offered 'scripting' as a 
'quickie' solution. But bearing your comments in mind the OO version 
will allow for (a) display to screen, (b) write to a LineSequential file 
and (c) I'll include a dialog containing just a Listbox that you can 
happily whizz through using the horizontal scroll bar. (I'm using N/E V 
3.1 and I don't think you will have any problems compiling it in your 
Personal Edition).

Firstly I'm not working to produce DLLs or EXEs, just the source to be 
run in Animator mode. That being said, how is the project constructed.

1.  Naturally I have BottlesOfBeer.cbl and a Trigger.cbl to kick start 
the project.

2. However, both options (b) and (c) above require additional source 
code. I want to reuse my own generic classes which already exist. Just 
take '(b) write to a LineSequential file'; I need the following 
additional sources (classes) :-

- LineSequentialFile
- MyErrors
- ErrorMessages

To get around this I have two directories/folders :-

c:\Cobol\Examples\BottlesOfBeer
c:\Copylib

\Copylib contains the source of File, Errors and Messages above, 
including any copyfiles those sources also use. I do compile in \Copylib 
but can't run from that project because the sources are invariably 
invoked elsewhere.

The source for the three above appear in \BottlesOfBeer - using
- LineSequentialFile - the source is in \Copylib but it also appears in 
the BottlesOfBeer project as follows, with its own reference in the 
Bottles project IDE :-

*>---------------------- LineSequentialFile.cbl ------------------------
copy "\Copylib\LineSequentialFile.cbl".
*>----------------------------------------------------------------------

No reference to the Disk in the above - it assumes you are using the 
same drive for \Copylib and \BottlesOfBeer. Within the Bottles project 
use ALT+F2 on the copy line and you display the source for 
LineSequentialFile, which can be edited in either \Copylib, (if within 
that project) or in \BottlesOfBeer, as indicated. Should you edit within 
\BottlesOfBeer - you re-compile in that Folder which outputs IDY and INT 
files into \BottlesOfBeer\DEBUGg. At some stage you should also 
re-compile within \Copylib, (has its own DEBUG sub-folder), because the 
editing changes are reflected in the only source which is in \Copylib. 
Within either of the projects, when you bring up an amended source, M/F 
gives you a warning message that the source has been changed - so 
re-compile within that project.

Now given that I may reach some 30 demo projects, it follows that if I 
change a copyfile or source in \Copylib it is highly likely it will 
affect more than one of my demo projects. That means I have to recompile 
or REBULD ALL for some projects - but bear in mind I'm not in 
'Production mode' and in the real-world, it is highly unlikely you would 
be dealing with some 30 separate projects at one time.

May not be the only way of getting around an IDEs limitations for a 
project, but it works fine for me.

At the current time \Copylib is a 'grab-bag' of diverse sources which 
currently are :-

xxx.cbl - some 55
xxx.cpy - currently 19

I anticipate the above numbers will grow, but wouldn't guesstimate at 
this stage.

It follows that when you go live with a RELEASE compile, either EXEs or 
DLLs, then you may want to extract all, or selective sources from 
\Copylib and put them into logical groupings for separate DLLs.

This is not programming, but systems design - gotta think outside of the 
box, Alistair.

Jimmy
```

###### ↳ ↳ ↳ Re: Micro Focus

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-10-24T13:28:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ihctiFpc0U1@mid.individual.net>`
- **References:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com> <dc296845-4cc7-4f6d-8c35-48c13ada3ef6@c10g2000yqh.googlegroups.com> <UQFwo.14$kS.3@newsfe17.iad>`

```
James Gavan wrote:
> Alistair Maclean wrote:
>> On Oct 21, 12:50 pm, Hugh Porter <shug.por...@googlemail.com> wrote:
…[119 more quoted lines elided]…
> Jimmy

Very interesting, Jimmy. Look forward to seeing your code.

You have raised something that is really important to many people and I've 
started a new thread to cover it. See "Dealing with Projects".

Pete.
```

#### ↳ Re: Micro Focus

- **From:** HansJ <hans.igel@googlemail.com>
- **Date:** 2010-10-26T01:44:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a80023e-460b-4e53-a5d3-87df45ed0c2f@p26g2000yqb.googlegroups.com>`
- **References:** `<fdc83baa-1c4b-485e-8420-f189e9a73ce3@h7g2000yqn.googlegroups.com>`

```
On 21 Okt., 13:50, Hugh Porter <shug.por...@googlemail.com> wrote:
> Hello,
>
…[5 more quoted lines elided]…
> Many thanks.

Hugh, are you going to give us any additional information, or are you
ignoring the folks that try to help?

Regards Hans
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
