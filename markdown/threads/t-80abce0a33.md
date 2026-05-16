[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interesting bugtrap

_2 messages · 2 participants · 2004-07_

---

### Interesting bugtrap

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-07-16T00:33:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40f71ee2.360687752@news.optonline.net>`

```
I have a a called program that sends emails to employees. I want to enhance it
to send emails to outsiders, with the email address supplied by the calling
program. To avoid re-testing existing callers, I add an extra parameter not
supplied by existing callers. Existing programs should work exactly as they did
before the change. 

The result is the new program works, but existing programs display "parm4
absent" and then abend with an address error. See whether you can figure out why
before scrolling down, where the answer is revealed.

WORKING-STORAGE SECTION.

01  EMAIL-IND     PIC X(01).

LINKAGE SECTION.
01  USER_NAME PIC X(10).
01  EMAIL-SUBJECT PIC X(54).
01  EMAIL-BODY PIC X(1000).
01  EMAIL-TO   PIC X(80).

PROCEDURE DIVISION USING
    USER_NAME
    EMAIL-SUBJECT
    EMAIL-BODY
    EMAIL-TO.   *> this parm is optional, usually absent.

    IF  ADDRESS OF EMAIL-TO EQUAL TO NULL OR
        EMAIL-TO   EQUAL TO SPACES
        MOVE 'N' TO EMAIL-IND
        display 'parm4 absent'
    ELSE
        MOVE 'Y' TO EMAIL-IND
        display 'parm4 present'
    END-IF.

    EXEC SQL EXECUTE
        declare
            smtp_recipient varchar2(80);

            cursor email_cursor is
                select EMAIL_ADDRESS from USERS
                    where USER_NAME =
                    rtrim(:USER_NAME, ' ');

        begin
             for email_rec in email_cursor loop

                -- Pickup email address(s)
                if  :EMAIL-IND = 'N' then
                    smtp_recipient := email_rec.EMAIL_ADDRESS;
                else
                    smtp_recipient := rtrim(:EMAIL-TO);
                end if;

                -- logic to send email snipped
            end loop;
        end;
    END-EXEC.
    GOBACK.

How can it abend when EMAIL-TO is never referenced? My first thought was that
PL/SQL was executing both sides of the IF in parallel, in multiple threads. The
correct answer is simpler and less esoteric. Here is the corrected version.

WORKING-STORAGE SECTION.

01  EMAIL-IND       PIC X(01).
01  WS-EMAIL-TO     PIC X(80).

LINKAGE SECTION.
01  USER_NAME PIC X(10).
01  EMAIL-SUBJECT PIC X(54).
01  EMAIL-BODY PIC X(1000).
01  EMAIL-TO   PIC X(80).

PROCEDURE DIVISION USING
    USER_NAME
    EMAIL-SUBJECT
    EMAIL-BODY
    EMAIL-TO.   *> this parm is optional, usually absent.

    IF  ADDRESS OF EMAIL-TO EQUAL TO NULL OR
        EMAIL-TO   EQUAL TO SPACES
        MOVE 'N' TO EMAIL-IND
        MOVE SPACES TO WS-EMAIL-TO
        display 'parm4 absent'
    ELSE
        MOVE 'Y' TO EMAIL-IND
        MOVE EMAIL-TO   TO WS-EMAIL-TO
        display 'parm4 present'
    END-IF.

    EXEC SQL EXECUTE
        declare
            smtp_recipient varchar2(80);

            cursor email_cursor is
                select EMAIL_ADDRESS from USERS
                    where USER_NAME =
                    rtrim(:USER_NAME);

        begin
             for email_rec in email_cursor loop

                -- Pickup email address(s)
                -- CAUTION: At execution time, preprocesser
                -- code replaces host variables with values,
                -- then does an EXECUTE IMMEDIATE on the
                -- PL/SQL program. If EMAIL-TO has a null
                -- pointer, that causes an abend, even
                -- though EMAIL-TO will not be referenced.
                if  :EMAIL-IND = 'N' then
                    smtp_recipient := email_rec.EMAIL_ADDRESS;
                else
                    smtp_recipient := rtrim(:WS-EMAIL-TO);
                end if;

                -- logic to send email snipped
            end loop;
        end;
    END-EXEC.
    GOBACK.
```

#### ↳ Re: Interesting bugtrap

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-07-15T21:15:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97WdnVKvF8C7p2rdRVn_iw@giganews.com>`
- **References:** `<40f71ee2.360687752@news.optonline.net>`

```
Robert Wagner wrote:
> I have a a called program that sends emails to employees. I want to
> enhance it to send emails to outsiders, with the email address
…[9 more quoted lines elided]…
> WORKING-STORAGE SECTION.

[...]

The program doesn't use enough pointers?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
