<h1><center>CCLE_mRNA_gene_kallisto_Tatlow</center></h1>
<h2><center> Status: Failed </center></h2>
<center>Mar 15, 18 16:03PM MST</center>


### Testing Directory . . .

#### Results: PASS
---
### Testing Configuration File . . .

&#9989;	config.yaml contains all necessary configurations.

&#9989;	Title is less than 300 characters

&#9989;	description.md contains a description.

#### Results: PASS
---
### Running Install . . .

Executing install.sh: Success

#### Results: PASS
---

### Testing file paths:

&#9989;	test_data.tsv exists.

&#9989;	test_metadata.tsv exists.

&#9989;	download.sh exists.

&#9989;	install.sh exists.

&#9989;	parse.sh exists.

&#9989;	cleanup.sh exists.

&#9989;	description.md exists.

&#9989;	config.yaml exists.

*Running user code . . .*

Executing download.sh: Success

Executing parse.sh: 

&#10060;	parse.sh returned an error:
~~~bash
Traceback (most recent call last):
  File "parseMeta2.py", line 14, in <module>
    hugoIndex = inHeaderItems.index("Hugo_Symbol")
ValueError: 'Hugo_Symbol' is not in list
Traceback (most recent call last):
  File "parseMeta1.py", line 15, in <module>
    symbolIndex = inHeaderItems.index("SYMBOL")
ValueError: 'SYMBOL' is not in list
~~~

