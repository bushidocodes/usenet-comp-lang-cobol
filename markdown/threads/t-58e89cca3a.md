[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC_FIND_DRIVES

_3 messages · 3 participants · 1995-10_

---

### PC_FIND_DRIVES

- **From:** "ya..." <ua-author-17087785@usenetarchives.gap>
- **Date:** 1995-10-04T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4513uf$tu@eagle.uis.edu>`

```
I have been trying to use the library routine PC_FIND_DRIVES to
determine what drive letters are used for a number of computers. I
seem to be calling the routine correctly, but I'm unable to determine
what drives are available by the returned data.

When I finally find out how to interperate the returned data, is it
possible to determine if a drive letter is networked, a floopy, or
cd-rom drive?

Any help would be appreciated.

Dan
```

#### ↳ Re: PC_FIND_DRIVES

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1995-10-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58e89cca3a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4513uf$tu@eagle.uis.edu>`
- **References:** `<4513uf$tu@eagle.uis.edu>`

```
In article <4513uf$t.··.@eag··s.edu>, ya··.@eag··s.edu says...
› 
› I have been trying to use the library routine PC_FIND_DRIVES to
› determine what drive letters are used for a number of computers.  I
› seem to be calling the routine correctly, but I'm unable to determine
› what drives are available by the returned data.

This is the routine I use (more or less) in the MFDIR2 GUI dialog used in the
product. It produces a table of drive letters and displays them at the end. As
you can see, you have to unpack the bytes returned from PC_FIND_DRIVES to work
out which drive is there.


special-names.
call-convention 4 is nrc
.
data division.
working-storage section.
78 pc-find-drives value "PC_FIND_DRIVES".
78 cbl-and value "CBL_AND".

01 drives5 pic x(4) comp-5.
01 drivesx pic x(4) comp-x.
01 char pic x.
01 char-x redefines char pic x comp-x.
01 special pic x(4) comp-5.
01 test-buffer5 pic 9(9) comp-5.
01 test-mask5 pic 9(9) comp-5.
01 stored-drive-char pic x occurs 26.
01 all-drive-chars redefines stored-drive-char
pic x(26).
procedure division.
main section.
call nrc pc-find-drives using drivesx end-call
move drivesx to drives5
move 1 to special
move "A" to char
perform until char-x > 91
move drives5 to test-mask5
move 1 to test-buffer5
perform test-routine
if test-buffer5 not = zero
move char to stored-drive-char (special)
add 1 to special
end-if
add 1 to char-x
divide 2 into drives5
end-perform
display all-drive-chars
stop run
.

test-routine section.
call nrc cbl-and using test-mask5
test-buffer5
by value 4
end-call
.

›
› When I finally find out how to interperate the returned data, is it
› possible to determine if a drive letter is networked, a floopy, or
› cd-rom drive?

Not that I know of using standard Micro Focus RTS routines. You may be able to
do it using DOS/Windows/Network API's I suppose but I've not had call to do
that yet.

›
› Any help would be appreciated.

Your welcome.

Shaun
```

#### ↳ Re: PC_FIND_DRIVES

- **From:** "david james" <ua-author-17271@usenetarchives.gap>
- **Date:** 1995-10-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58e89cca3a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4513uf$tu@eagle.uis.edu>`
- **References:** `<4513uf$tu@eagle.uis.edu>`

```
I assume you mean some kind of PC compiler such as Micro Focus. I looked
it up in Micro Focus, here is what they say to do:

call "PC_FIND_DRIVES" using drive-info
returning status-code

Parameters:

drive-info pic x(4) comp-x.
status-code See Key

On Exit:

drive-info The 26 least-significant bits correspond to drives A:
through Z:, with A: represented by bit 0 (the least
significant bit) and Z:represented by bit 25. The
corresponding bit is set for each drive that is
present.

So after the call drive-info contains the drive letters like this:

31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 09 08
Z Y X W V U T S R Q P O N M L K J I

07 06 05 04 03 02 01 00
H G F E D C B A

To check for existence of a drive you have to know the corresponding
character that would represent your bit pattern. It might be easier to
take the bytes one at a time. Some kind of table would help.

This doesn't look like it provides information on networked, floppy, or
CD-Rom. Typically, networked drives go from F thru Z, and CDs are D or
E.

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
