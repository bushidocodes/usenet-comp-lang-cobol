[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using Rdb temporary tables for 3GL memory allocation

_1 message · 1 participant · 2005-01_

---

### Using Rdb temporary tables for 3GL memory allocation

- **From:** "Richard Maher" <maher_rj@hotspamnotmail.com>
- **Date:** 2005-01-23T19:18:20+00:00
- **Newsgroups:** comp.databases.rdb,comp.lang.cobol,comp.os.vms
- **Message-ID:** `<ct0t9q$1fb$1@sparta.btinternet.com>`

```
Hi,

I came across an idea the other day for scrolling through Rdb temporary
tables by using the ROWID as an offset to the dynamic memory allocated by
Rdb. I can't say it's the "right" way to do things but having knocked up an
example to see if it worked I now offer it here as just that.

Word of warning, If you give it a dodgy DBKEY then you could get a bugcheck
dump and image termination instead of NO_RECORD or NODBKEY.

Now if DEC/hp COBOL gave us that great (IBM? Standard?) syntax "SET ADDRESS
OF var TO pointer" then I'd be a lot happier.

Regards Richard Maher

PS. Obviously replace the  &s with spaces and the wrapping shouldn't be too
bad.

$!
$&on&warning&then&exit
$&set&verify
$!
$&create&pers_scroll.cob
identification&division.
program-id.&&&&pers_scroll.
data&division.
working-storage&section.
01&&ss$_abort&&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp&&&&value&&&external&ss$
_abort.
01&&ss$_normal&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp&&&&value&&&external&ss$
_normal.
01&&sys_status&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
*
01&&term_control_area&&&&&&&&&&&pic&x(12).
01&&term_control_area_size&&&&&&pic&9(9)&&&&&&&&comp&&&&value&&&12.
01&&workspace&&&&&&&&&&&&&&&&&&&pic&x(12).
01&&workspace_size&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp&&&&value&&&2000.
01&&fms_term_chan&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&terminator&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&dummy&&&&&&&&&&&&&&&&&&&&&&&pic&x(1).
*
01&&in_name_varchar.
&&&&03&&in_name_len&&&&&&&&&&&&&pic&9(4)&&&&&&&&comp.
&&&&03&&in_name&&&&&&&&&&&&&&&&&pic&x(14).
01&&row_cnt&&&&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&out_row_cnt&&&&&&&&&&&&&&&&&pic&9(10).
01&&target_dbkey.
&&&&03&&&&&&&&&&&&&&&&&&&&&&&&&&pic&x(2).
&&&&03&&target_row&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
&&&&03&&&&&&&&&&&&&&&&&&&&&&&&&&pic&x(2).
01&&row_offset&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
*
01&&cur_line&&&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&min_window&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&max_window&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
01&&num_lines_in_scroll&&&&&&&&&pic&9(9)&&&&&&&&comp&&&&value&&&12.
*
01&&last_name&&&&&&&&&&&&&&&&&&&pic&x(14).
01&&eof_msg&&&&&&&&&&&&&&&&&&&&&pic&x(33)&&&&&&&&&&&&&&&value
"No&more&records&in&that&direction".
*
01&rdb$message_vector&&&&&&&&&&&global&&&&&&&&&&external.
&&&&03&rdb$lu_num_arguments&&&&&pic&s9(9)&&&&&&&comp.
&&&&03&rdb$lu_status&&&&&&&&&&&&pic&s9(9)&&&&&&&comp.
&&&&03&rdb$alu_arguments&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&occurs&18&times.
&&&&&&&&05&rdb$lu_arguments&&&&&pic&s9(9)&&&&&&&comp.
01&&sqlcode&&&&&&&&&&&&&&&&&&&&&pic&9(9)&&&&&&&&comp.
*
copy&"fms$examples:fdvdef".
*
procedure&division.
kick_off&section.
00.
&&&&perform&form_setup.

&&&&call&"fdv$get"
&&&&&&&&using&&&by&descriptor&&&in_name
&&&&&&&&&&&&&&&&by&reference&&&&terminator
&&&&&&&&&&&&&&&&by&descriptor&&&"in_name".

&&&&perform&scroll_it&until&in_name&=&spaces.

&&&&call&"fdv$dterm"&using&by&descriptor&term_control_area.

&&&&stop&run.
*
form_setup&section.
00.
&&&&call&"fdv$fchan"&using&fms_term_chan&giving&sys_status.
&&&&if&sys_status&not&=&fdv$_suc&call&"lib$stop"&using&by&value&sys_status.

&&&&call&"fdv$aterm"&
&&&&&&&&using&&&by&descriptor&&&term_control_area
&&&&&&&&&&&&&&&&by&reference&&&&term_control_area_size
&&&&&&&&&&&&&&&&by&reference&&&&fms_term_chan
&&&&&&&&giving&&sys_status.
&&&&if&sys_status&not&=&fdv$_suc&call&"lib$stop"&using&by&value&sys_status.

&&&&call&"fdv$awksp"&
&&&&&&&&using&&&by&descriptor&&&workspace
&&&&&&&&&&&&&&&&by&reference&&&&workspace_size
&&&&&&&&giving&&sys_status.
&&&&if&sys_status&not&=&fdv$_suc&call&"lib$stop"&using&by&value&sys_status.
&&&&&&&&
&&&&call&"fdv$cdisp"&using&by&descriptor&"pers_form"&giving&sys_status.
&&&&if&sys_status&not&=&fdv$_suc&call&"lib$stop"&using&by&value&sys_status.
*
scroll_it&section.
00.
&&&&call&"str$trim"
&&&&&&&&using&&&by&descriptor&&&in_name,&in_name
&&&&&&&&&&&&&&&&by&reference&&&&in_name_len.

&&&&call&"scroll_name_load_tmp_table"&
&&&&&&&&using&&&sqlcode,&
&&&&&&&&&&&&&&&&in_name_varchar,
&&&&&&&&&&&&&&&&row_cnt,
&&&&&&&&&&&&&&&&target_dbkey.
&&&&if&rdb$lu_status&not&=&ss$_normal
&&&&&&&&call&"sys$putmsg"&using&rdb$message_vector
&&&&&&&&call&"lib$stop"&using&by&value&ss$_abort.

&&&&move&row_cnt&to&out_row_cnt.
&&&&call&"fdv$put"&using&by&descriptor&out_row_cnt,&"out_row_cnt"&.

&&&&if&row_cnt&=&zeros
&&&&&&&&call&"fdv$putl"&using&by&descriptor&"No&records&found&matching&your&
selection"
&&&&&&&&call&"fdv$sigop"
&&&&&&&&go&to&fini.

&&&&subtract&1&from&target_row&giving&row_offset.

&&&&perform&prime_window.

&&&&perform&with&test&after&until&terminator&=&fdv$k_ft_ntr&or&fdv$k_kp_per
&&&&&&&&call&"fdv$get"&
&&&&&&&&&&&&using&&&&&&&by&descriptor&&&dummy
&&&&&&&&&&&&&&&&&&&&&&&&by&reference&&&&terminator
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"dummy"

&&&&&&&&evaluate&&&&&&&&terminator
&&&&&&&&&&&&when&&&&&&&&fdv$k_ft_sbk
&&&&&&&&&&&&when&&&&&&&&fdv$k_ft_spr&&&&perform&scrbak
&&&&&&&&&&&&when&&&&&&&&fdv$k_ft_sfw
&&&&&&&&&&&&when&&&&&&&&fdv$k_ft_snx&&&&perform&scrfwd
&&&&&&&&end-evaluate
&&&&end-perform.

&&&&go&to&fini.
*
prime_window.
*
&&&&perform&with&test&after&varying&cur_line&from&1&by&1
&&&&&&&&until&cur_line&not&less&num_lines_in_scroll&or&cur_line&not&less&row
_cnt
&&&&&&&&if&cur_line&not&=&1
&&&&&&&&&&&&call&"fdv$pft"&
&&&&&&&&&&&&&&&&using&&&by&reference&&&&fdv$k_ft_sfw
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"scr_name"
&&&&&&&&end-if
&&&&&&&&perform&get_row
&&&&&&&&call&"fdv$putsc"&
&&&&&&&&&&&&using&&&&&&&by&descriptor&&&"scr_name"
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&last_name
&&&&end-perform.

&&&&move&1&to&min_window.
&&&&move&cur_line&to&max_window.
*
scrbak.
&&&&if&cur_line&=&1
&&&&&&&&call&"fdv$putl"&using&by&descriptor&eof_msg
&&&&else&&&&&&&&
&&&&&&&&if&cur_line&not&=&min_window
&&&&&&&&&&&&subtract&1&from&cur_line
&&&&&&&&&&&&call&"fdv$pft"&
&&&&&&&&&&&&&&&&using&&&by&reference&&&&fdv$k_ft_sbk&
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"scr_name"
&&&&&&&&else&&&&
&&&&&&&&&&&&subtract&1&from&min_window,&max_window,&cur_line
&&&&&&&&&&&&perform&get_row
&&&&&&&&&&&&call&"fdv$pft"&
&&&&&&&&&&&&&&&&using&&&by&reference&&&&fdv$k_ft_sbk&
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"scr_name",&last_name.
*
scrfwd.
&&&&if&cur_line&=&row_cnt
&&&&&&&&call&"fdv$putl"&using&by&descriptor&eof_msg
&&&&else&&&&&&&&
&&&&&&&&if&cur_line&not&=&max_window
&&&&&&&&&&&&add&1&to&cur_line
&&&&&&&&&&&&call&"fdv$pft"&
&&&&&&&&&&&&&&&&using&&&by&reference&&&&fdv$k_ft_sfw&
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"scr_name"
&&&&&&&&else&&&&
&&&&&&&&&&&&add&1&to&min_window,&max_window,&cur_line
&&&&&&&&&&&&perform&get_row
&&&&&&&&&&&&call&"fdv$pft"&
&&&&&&&&&&&&&&&&using&&&by&reference&&&&fdv$k_ft_sfw&
&&&&&&&&&&&&&&&&&&&&&&&&by&descriptor&&&"scr_name",&last_name.
*
get_row.
&&&&add&cur_line,&row_offset&giving&target_row.

&&&&call&"scroll_name_get_target"
&&&&&&&&using&&&sqlcode,
&&&&&&&&&&&&&&&&target_dbkey,
&&&&&&&&&&&&&&&&last_name.
&&&&if&rdb$lu_status&not&=&ss$_normal
&&&&&&&&call&"sys$putmsg"&using&rdb$message_vector
&&&&&&&&call&"lib$stop"&using&by&value&ss$_abort.
*
fini.
&&&&perform&reset_data.

&&&&call&"fdv$get"
&&&&&&&&using&&&by&descriptor&&&in_name
&&&&&&&&&&&&&&&&by&reference&&&&terminator
&&&&&&&&&&&&&&&&by&descriptor&&&"in_name".
*
reset_data&section.
00.
&&&&call&"scroll_name_set_trans"&using&sqlcode.
&&&&if&rdb$lu_status&not&=&ss$_normal
&&&&&&&&call&"sys$putmsg"&using&rdb$message_vector
&&&&&&&&call&"lib$stop"&using&by&value&ss$_abort.

&&&&call&"scroll_name_truncate"&using&sqlcode.
&&&&if&rdb$lu_status&not&=&ss$_normal
&&&&&&&&call&"sys$putmsg"&using&rdb$message_vector
&&&&&&&&call&"lib$stop"&using&by&value&ss$_abort.

&&&&call&"scroll_name_commit"&using&sqlcode.
&&&&if&rdb$lu_status&not&=&ss$_normal
&&&&&&&&call&"sys$putmsg"&using&rdb$message_vector
&&&&&&&&call&"lib$stop"&using&by&value&ss$_abort.

&&&&call&"fdv$putda".
*
end&program&pers_scroll.
$!
$&cobol/list&pers_scroll
$!
$&create&pers_form.flg
&
!&&&&&&&&&&FMS&Form&Description&Application&Aid&
!&&&&&&&&&&&&&&&&&&&&&Version&V2.5
&
FORM&NAME='PERS_FORM'
&&&&AREA_TO_CLEAR=1:23
&&&&WIDTH=80
&&&&BACKGROUND=CURRENT
&&&&CHARACTER_SET=UK
&&&&HIGHLIGHT=BOLD:REVERSE
&&&&DBLSIZ=1
&&&&;

SCROLL&BEGIN_WITH=10&&END_WITH=21&;

TEXT&(10,31)&'x'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(10,50)&'x'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(1,7)&'Temporary&Table&Scroll&Demo'
&&&&;
TEXT&(5,23)&'Last&Name:'
&&&&;
TEXT&(7,31)&'lqqqqqqqqqqqqqqqqqqk'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(8,31)&'x'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(8,32)&'&Rows:&'
&&&&REVERSE&
&&&&;
TEXT&(8,49)&'&'
&&&&REVERSE&
&&&&;
TEXT&(8,50)&'x'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(9,31)&'tqqqqqqqqqqqqqqqqqqu'
&&&&CHARACTER_SET=RULE
&&&&;
TEXT&(22,31)&'mqqqqqqqqqqqqqqqqqqj'
&&&&CHARACTER_SET=RULE
&&&&;

ATTRIBUTE_DEFAULTS&FIELD
&&&&CLEAR_CHARACTER='&'
&&&&NOAUTOTAB&BLANK_FILL&NOBLINKING&NOBOLD&NOREVERSE
&&&&NOUNDERLINE&NODISPLAY_ONLY&ECHO&NOFIXED_DECIMAL
&&&&LEFT_JUSTIFIED&NOSUPERVISOR_ONLY&NOSUPPRESS&NOUPPERCASE
&&&&;

FIELD&NAME='IN_NAME'&&(5,34)
&&&&PICTURE=14'X'
&&&&HELP='Enter&the&name&to&search&for,&or&spaces&to&exit'
&&&&UPPERCASE&
&&&&;
FIELD&NAME='OUT_ROW_CNT'&&(8,39)
&&&&PICTURE=10'9'
&&&&RIGHT_JUSTIFIED&ZERO_FILL&SUPPRESS&DISPLAY_ONLY&CLEAR_CHARACTER='0'&REVE
RSE&
&&&&;
FIELD&NAME='SCR_NAME'&&(10,34)
&&&&PICTURE=14'X'
&&&&DISPLAY_ONLY&
&&&&;
FIELD&NAME='DUMMY'&&(10,51)
&&&&PICTURE='X'
&&&&NOECHO&
&&&&;

ORDER&BEGIN_WITH&=&1
&&&&NAME='IN_NAME'&
&&&&NAME='OUT_ROW_CNT'&
&&&&NAME='SCR_NAME'&
&&&&NAME='DUMMY'&
&&&&;

&
END_OF_FORM&NAME='PERS_FORM'&;
$!
$&fms/translate&pers_form
$&fms/object&&&&pers_form
$!
$&create&pers_scroll.sql

attach&'file&mf_personnel';

drop&table&tmp_name&if&exists;

create&global&temporary&table&tmp_name&
(last_name&last_name_dom)&
on&commit&preserve&rows;

commit;

exit;
$!
$&sql:==$sql$
$&sql&@pers_scroll
$!
$&create&pers_scroll_sql.sqlmod
module&&&&pers_scroll_sql
language&&cobol
authorization&pers
parameter&colons

declare&external&pers&alias&filename&mf_personnel

procedure&scroll_name_load_tmp_table
&&&&&&&&sqlcode,
&&&&&&&&:in_name&&&&&&&&&&&&&&&&varchar(14),
&&&&&&&&:row_cnt&&&&&&&&&&&&&&&&integer,
&&&&&&&&:first_dbkey&&&&&&&&&&&&char(8)
&&&&&&&&;

&&&&&&&&begin

&&&&&&&&set&transaction&read&only&reserving&employees&for&shared&read;

&&&&&&&&insert&into&tmp_name&
&&&&&&&&&&&&&&&&(
&&&&&&&&&&&&&&&&select&&distinct
&&&&&&&&&&&&&&&&&&&&&&&&last_name
&&&&&&&&&&&&&&&&from
&&&&&&&&&&&&&&&&&&&&&&&&employees
&&&&&&&&&&&&&&&&where
&&&&&&&&&&&&&&&&&&&&&&&&last_name&starting&with&:in_name
&&&&&&&&&&&&&&&&)
&&&&&&&&;

&&&&&&&&get&diagnostics&:row_cnt&=&row_count;

&&&&&&&&if&:row_cnt&<>&0
&&&&&&&&then
&&&&&&&&&&&&&&&&select
&&&&&&&&&&&&&&&&&&&&&&&&dbkey
&&&&&&&&&&&&&&&&into
&&&&&&&&&&&&&&&&&&&&&&&&:first_dbkey
&&&&&&&&&&&&&&&&from
&&&&&&&&&&&&&&&&&&&&&&&&tmp_name
&&&&&&&&&&&&&&&&limit&to&
&&&&&&&&&&&&&&&&&&&&&&&&1&row;
&&&&&&&&end&if;

&&&&&&&&commit;

&&&&&&&&end;

procedure&scroll_name_set_trans
&&&&&&&&sqlcode
&&&&&&&&;

&&&&&&&&set&transaction&read&only;

procedure&scroll_name_truncate
&&&&&&&&sqlcode
&&&&&&&&;

&&&&&&&&truncate&table&tmp_name;

procedure&scroll_name_commit
&&&&&&&&sqlcode;

&&&&&&&&commit;

procedure&scroll_name_get_target
&&&&&&&&sqlcode,
&&&&&&&&:target_dbkey&&&&&&&&&&&char(8),
&&&&&&&&:last_name&&&&&&&&&&&&&&last_name_dom
&&&&&&&&;

&&&&&&&&begin

&&&&&&&&set&transaction&read&only;

&&&&&&&&select
&&&&&&&&&&&&&&&&last_name
&&&&&&&&into
&&&&&&&&&&&&&&&&:last_name
&&&&&&&&from
&&&&&&&&&&&&&&&&tmp_name
&&&&&&&&where
&&&&&&&&&&&&&&&&dbkey&=&:target_dbkey;

&&&&&&&&commit;

&&&&&&&&end;

$!
$&sqlmod:==$sql$mod
$&sqlmod/notransaction_default/rollback_on_exit&pers_scroll_sql
$!
$&link&pers_scroll,pers_form,pers_scroll_sql,sql$user/lib
$!
$&exit
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
