

OpenTrials README

What you need

- Computer
- Python 3.X
- Internet
- The BravadoClient package
  - To install:
    - Open your [command prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089)
    - Type in &#39;pip install bravado&#39;
    - Hit enter

What this script does

- It calls the OpenTrials API
  - An [API](https://en.wikipedia.org/wiki/Application_programming_interface) is something similar to a website for computers. They can go there and read data
  - The way OpenTrials shares their data should be regarded as best practice. It makes working with their data easy and offers countless opportunities. Thank you to them for offering such an awesome service!
- It performs your search
- It reads in the data from OpenTrials
- It writes it into an RIS file

How to use it

- Copy the code into your code editor
- Save the code as &#39;Call.py&#39; in an empty folder of your choice
- In line 4 the script reads &quot;search = &#39;Malaria AND Senegal&#39;&quot;. Change &quot;Malaria AND Senegal&quot; to the search term that you want to search for
  - OpenTrials enables complex searches through their API. For a full description of the syntax, take a look at [this](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) page

- Save the file
- Execute the file (through the command prompt or by double-clicking the file)
  - A small window executing Python should appear
  - It can take a while until the code is fully executed (depending on the amount of hits a few minutes or more)
- A file called &#39;RIS Formated OpenTrials Data.ris&#39; should appear in the same folder as Call.py. This should be your fully functional RIS file.

