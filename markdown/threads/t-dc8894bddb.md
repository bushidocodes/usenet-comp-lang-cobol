[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about SORT-MERGE.

_2 messages · 2 participants · 1998-06_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Question about SORT-MERGE.

- **From:** "eagle_eye1" <ua-author-17075226@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6m0k51$fsj$1@news.yokota.attnet.or.jp>`

```

I recently purchased the book COBOL For dummies and
started reading through the book. I came to the First program at the end of
Chapter two and tried to compile the program. I compiled the program
exactly like the book specified and get numerous errors. I am using the
Fujitsu 85 Compiler (Starter Set) which came with the book. I managed to
fix all of the errors, except one.
Any help would be greatly appreciated. I have been up for what seems like
years. thank you

please reply to this is my real address.

Anyway here is my diagnostic message and the program I am working on.


** DIAGNOSTIC MESSAGE ** (SIMPLESORTERSAMPLE)


C:\DeCourses\fsm296\bnmenu.cob 28: JMN2896I-S
SORT-MERGE FILE CAN ONLY SPECIFY FILE-IDENTIFIER IN ASSIGN CLAUSE.




STATISTICS: HIGHEST SEVERITY CODE=S, PROGRAM UNIT=1



000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. SimpleSorterSample.
000030 AUTHOR. Bertha D Blues.
000040 DATE-WRITTEN. Long long ago.
000050 DATE-COMPILED.
000060 SECURITY. Blanket.
000070 ENVIRONMENT DIVISION.
000080 CONFIGURATION SECTION.
000090 SOURCE-COMPUTER. ThisOne.
000100 OBJECT-COMPUTER. ThisOne.
000110 SPECIAL-NAMES.
000120 CURRENCY-SYMBOL IS "$".
000130 INPUT-OUTPUT SECTION.
000140 FILE-CONTROL.
000150 SELECT BeanList ASSIGN TO "unsorted"
000160 ORGANIZATION IS SEQUENTIAL.
000170 SELECT Sorter ASSIGN TO "sortfile".
000180 SELECT SortedBeanList ASSIGN TO "sorted"
000190 ORGANIZATION IS SEQUENTIAL.
000200 SELECT PrintFile
000210 ASSIGN TO PRINTER ORGANIZATION IS SEQUENTIAL.
000230 DATA DIVISION.
000240 FILE SECTION.
000250 FD BeanList RECORD CONTAINS 16 CHARACTERS.
000260 01 BeanListData.
000270 05 BeanOwner PIC X(12).
000280 05 BeanCount PIC ZZZ9.
000290 SD Sorter
000291 RECORD CONTAINS 16 CHARACTERS.
000300 01 SorterData.
000310 05 BeanOwner PIC X(12).
000320 05 BeanCount PIC ZZZ9.
000330 FD SortedBeanList RECORD CONTAINS 16 CHARACTERS.
000340 01 SortedBeanListData.
000350 05 BeanOwner PIC X(12).
000360 05 BeanCount PIC ZZZ9.
000370 FD PrintFile.
000380 01 PrintLine PIC X(80).
000390 WORKING-STORAGE SECTION.
000400 77 Response PIC X VALUE " ".
000410 88 DisplayUnsorted VALUE "1".
000420 88 DisplayNameSorted VALUE "2".
000430 88 DisplayNumberSorted VALUE "3".
000440 88 PrintUnsorted VALUE "4".
000450 88 PrintNameSorted VALUE "5".
000460 88 PrintNumberSorted VALUE "6".
000470 88 QuitProgram VALUE "q", "Q".
000480 77 FileFlag PIC X.
000490 88 EndOfFile VALUE "E".
000500 01 Heads PIC X(80).
000510 PROCEDURE DIVISION.
000520 Mainline.
000530 PERFORM CreateList.
000540 PERFORM MenuLoop UNTIL QuitProgram.
000550 STOP RUN.
000560* Create a new file and write several records to it.
000570 CreateList.
000580 OPEN OUTPUT BeanList.
000590 MOVE "Alley" TO BeanOwner OF BeanListData.
000600 MOVE 87 TO BeanCount OF BeanListData.
000610 WRITE BeanListData.
000620 MOVE "Umpa" TO BeanOwner OF BeanListData.
000630 MOVE 341 TO BeanCount OF BeanListData.
000640 WRITE BeanListData.
000650 MOVE "Guz" TO BeanOwner OF BeanListData.
000660 MOVE 12 TO BeanCount OF BeanListData.
000670 WRITE BeanListData.
000680 MOVE "Foozy" TO BeanOwner OF BeanListData.
000690 MOVE 118 TO BeanCount OF BeanListData.
000700 WRITE BeanListData.
000710 MOVE "Ooola" TO BeanOwner OF BeanListData.
000720 MOVE 212 TO BeanCount OF BeanListData.
000730 WRITE BeanListData.
000740 MOVE "Wunmug" TO BeanOwner OF BeanListData.
000750 MOVE 88 TO BeanCount OF BeanListData.
000760 WRITE BeanListData.
000770 MOVE "Guz" TO BeanOwner OF BeanListData.
000780 MOVE 233 TO BeanCount OF BeanListData.
000790 WRITE BeanListData.
000800 MOVE "Oscar" TO BeanOwner OF BeanListData.
000810 MOVE 67 TO BeanCount OF BeanListData.
000820 WRITE BeanListData.
000830 MOVE "Dinny" TO BeanOwner OF BeanListData.
000840 MOVE 891 TO BeanCount OF BeanListData.
000850 WRITE BeanListData.
000860 CLOSE BeanList.
000870
000880*Display a menu and act on the request from the user.
000881 MenuLoop.
000882 DISPLAY " ".
000883 DISPLAY " 1 Display unsorted."
000884 DISPLAY " 2 Display sorted by name."
000885 DISPLAY " 3 Display sorted by number."
000886 DISPLAY " 4 Print unsorted."
000887 DISPLAY " 5 Print sorted by name."
000888 DISPLAY " 6 Print sorted by number."
000889 DISPLAY " Q Quit program."
000890 DISPLAY " " WITH NO ADVANCING.
000891 ACCEPT Response.
000892 IF DisplayUnsorted
000893 PERFORM ShowUnsortedList
000894 ELSE IF DisplayNameSorted
000895 PERFORM ShowSortedByName
000896 ELSE IF DisplayNumberSorted
000897 PERFORM ShowSortedByNumber
000898 ELSE IF PrintUnsorted
000899 PERFORM PrintUnsortedList
000900 ELSE IF PrintNameSorted
000901 PERFORM PrintSortedByName
000902 ELSE IF PrintNumberSorted
000903 PERFORM PrintSortedByNumber.
000904
000905* Read the list and display it without sorting.
000906 ShowUnsortedList.
000907 OPEN INPUT BeanList.
000908 MOVE SPACE TO FileFlag.
000909 PERFORM UNTIL EndOfFile
000910 READ BeanList
000911 AT END MOVE "E" TO FileFlag
000912 NOT AT END DISPLAY BeanOwner OF BeanListData
000913 BeanCount OF BeanListData
000914 END-READ
000915 END-PERFORM.
000916 CLOSE BeanList.
000917
000918* Read the list and print it without sorting.
000919 PrintUnsortedList.
000920 OPEN INPUT BeanList.
000921 OPEN OUTPUT PrintFile.
000922 MOVE SPACE TO FileFlag.
000923 PERFORM UNTIL EndOfFile
000924 READ BeanList
000925 AT END MOVE "E" TO FileFlag
000926 NOT AT END WRITE PrintLine FROM BeanListData
000927 END-READ
000928 END-PERFORM.
000929 CLOSE BeanList.
000930 CLOSE PrintFile.
000931
000932* Display the list sorted by the names.
000933 ShowSortedByName.
000934 PERFORM SortByName.
000935 PERFORM ShowSortedList.
000936
000937* Display the list sorted by the numbers.
000938 ShowSortedByNumber.
000939 PERFORM SortByNumber.
000940 PERFORM ShowSortedList.
000941
000942* Print the list sorted by the names.
000943 PrintSortedByName.
000944 PERFORM SortByName.
000945 MOVE "Sorted by name..." TO Heads.
000946 PERFORM PrintSortedList.
000947
000948* Print the list sorted by the numbers.
000949 PrintSortedByNumber.
000950 PERFORM SortByNumber.
000951 MOVE "Sorted by number..." TO Heads.
000952 PERFORM PrintSortedList.
000953
000954* Display the list from the sorted bean list
000955 ShowSortedList.
000956 OPEN INPUT SortedBeanList.
000957 MOVE SPACE TO FileFlag.
000958 PERFORM UNTIL EndOfFile
000959 READ SortedBeanList
000960 AT END MOVE "E" TO FileFlag
000961 NOT AT END DISPLAY
000962 BeanOwner OF SortedBeanListData
000963 BeanCount OF SortedBeanListData
000964 END-READ
000965 END-PERFORM.
000966 CLOSE SortedBeanList.
000967
000968* Print the list from the sorted bean list
000969 PrintSortedList.
000970 OPEN INPUT SortedBeanList.
000971 OPEN OUTPUT PrintFile.
000972 MOVE SPACE TO FileFlag.
000973 WRITE PrintLine FROM Heads.
000974 PERFORM UNTIL EndOfFile
000975 READ SortedBeanList
000976 AT END MOVE "E" TO FileFlag
000977 NOT AT END
000978 WRITE PrintLine FROM SortedBeanListData
000979 END-READ
000980 END-PERFORM.
000981 CLOSE PrintFile.
000982 CLOSE SortedBeanList.
000983
000984* Sort the list by the names
000985 SortByName.
000986 SORT Sorter
000987 ON ASCENDING KEY BeanOwner OF SorterData
000988 USING BeanList
000989 GIVING SortedBeanList.
000990
000991* Sort the list by the numbers
000992 SortByNumber.
000993 SORT Sorter
000994 ON ASCENDING KEY BeanCount OF SorterData
000995 USING BeanList
000996 GIVING SortedBeanList.
000997
000998
000999
001000
001001
001002

thank you once again, and please reply to
```

#### ↳ Re: Question about SORT-MERGE.

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-06-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc8894bddb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6m0k51$fsj$1@news.yokota.attnet.or.jp>`
- **References:** `<6m0k51$fsj$1@news.yokota.attnet.or.jp>`

```


I am not used to Fujitsu COBOL, but it looks like the message is saying that
you cannot use the "literal" form in the ASSIGN clause. In other words, you
should change,

SELECT Sorter ASSIGN TO "sortfile".

to

SELECT Sorter ASSIGN TO sortfile.


eagle_eye1 wrote in message <6m0k51$fsj$1.··.@new··r.jp>...
› I recently purchased the book COBOL For dummies and
› started reading through the book.  I came to the First program at the end
…[239 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
