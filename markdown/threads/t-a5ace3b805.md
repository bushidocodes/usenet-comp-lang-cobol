[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help

_3 messages · 3 participants · 1999-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help

- **From:** "Colin Lyons" <colin.r.lyons@btinternet.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7smak0$aos$1@plutonium.btinternet.com>`

```
I'm new to cobol and i am trying to figure out this problem:

The program logic below is supposed to read through a file and display all
the
odd numbered records (first record, third record, fifth, etc). I need help
to fill in the blanks..
any takers

OPEN INPUT TEST-FILE.
MOVE SPACES TO FILE-SWITCH.
PERFORM UNTIL FILE-SWITCH = 'EOF'
    READ TEST-FILE
       AT END
          MOVE EOF TO FILE-SWITCH
    ___________________
          DISPLAY TEST-RECORD
          READ TEST-FILE
            AT END
               MOVE 'EOF' TO FILE SWITCH
          _____________________
       ___________________________
END-PERFORM.
```

#### ↳ Re: Help

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF5F2B.3318E4ED@zip.com.au>`
- **References:** `<7smak0$aos$1@plutonium.btinternet.com>`

```
Colin Lyons wrote:
> 
> I'm new to cobol and i am trying to figure out this problem:
…[6 more quoted lines elided]…
> 

Here is a minor tidy up to get you on your way, not a complete
solution assumes you have a passably recent compiler:

 OPEN INPUT TEST-FILE.
 MOVE SPACES TO FILE-SWITCH.
 PERFORM UNTIL FILE-SWITCH = 'EOF'
     READ TEST-FILE
        AT END
           MOVE EOF TO FILE-SWITCH
        NOT AT END
           DISPLAY TEST-RECORD
           READ TEST-FILE
             AT END
                MOVE 'EOF' TO FILE SWITCH
           END-READ
     END-READ
 END-PERFORM.
```

##### ↳ ↳ Re: Help

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF9DA8.4B60459E@home.com>`
- **References:** `<7smak0$aos$1@plutonium.btinternet.com> <37EF5F2B.3318E4ED@zip.com.au>`

```
Ken Foskey wrote:
> 
> Colin Lyons wrote:
…[26 more quoted lines elided]…
>  END-PERFORM.

Ken's got you started; consider why he put in those end-reads. OK, you
are new at the game and you've probably got mental blockage about your
'odds' and 'evens' - Next Clue - go read your Programming text - look at
the syntax for the DIVIDE verb.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
