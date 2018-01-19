

Eldis README

What you need

- Computer
- Internet
- An IDS API Key
  - If you know me personally, just ask for my key (I just do not make it public, because the API is [rate limited](https://en.wikipedia.org/wiki/Rate_limiting) by this key)
  - Else, go to [https://api.ids.ac.uk/](https://api.ids.ac.uk/)
  - Make an account for free. When they ask for your website, just enter a random website
  - Go to &#39;Your Account&#39;
    - ![alt text](https://raw.githubusercontent.com/Haay2/RIS_Exporter/Beta/For_Presentation/IDS%20API%20Your%20Account%20Button.JPG)
  - Your API key are the random characters following &#39;Your access GUID is&#39;
    - ![alt text](https://raw.githubusercontent.com/Haay2/RIS_Exporter/Beta/For_Presentation/IDS%20API%20API%20Key%20site.JPG)
- The BeautifulSoup package
  - To install:
    - Open your [command prompt](https://www.lifewire.com/how-to-open-command-prompt-2618089)
    - Type in &#39;pip install beautifulsoup4&#39;
    - Hit enter

What these scripts do

- The first script (Call.py):
  - It goes to the [IDS API](https://api.ids.ac.uk/) for Eldis
  - It downloads the results for a general search
  - It writes those results into an SQLite database
- The second script (DBCall.py)
  - It queries the database generated with the first script with a second search
  - It takes the results from the second search and writes them into an RIS file

Comment

The documentation for the IDS API states that it allows for complex searches. I could not figure out how these have to be formulated. That is why a database is created as an intermediate step. If you know how to formulate complex queries for the IDS API (many truncated terms concatenated with Boolean operators and with braces), please let me know and I will update the script.

The first script is very inefficient. Ways to make it more efficient would be e.g. i) to make the database relational ii) to not download the full result sets for queries that are just made for metadata iii) to only write search-relevant fields into the database and include the remaining fields with the second script iv) to find out how to query the API with complex searches and write a new script v) to optimise the Python script for performance. In case you are good at programming, please do not hesitate to give it a try.

How to use it

- Copy the &#39;Call.py&#39; file into your code editor
- Save it as &#39;Call.py&#39; in an empty folder of your choice
- Go to line 98 in the script. It reads &quot;api\_key = &#39;YOUR-API-KEY-HERE&#39;&quot;. Replace &quot;YOUR-API-KEY-HERE&quot; with your API key (see section &#39;What your need&#39;)
- First you will have to formulate a general search. This search retrieves all documents regarding a topic and saves it for later. The second script later searches this saved set of documents and filters out the relevant ones. The fewer documents you are going to save, the quicker the script runs. However, you can query all saved documents. Therefore, if you are planning multiple searches, you might as well download all documents straight away. Right hand truncation is allowed. All terms will be concatenated with an OR term. Put all terms in single quotes, and then separate them with a comma.
For example, if you want to look for documents concerning Malaria in Senegal or Gambia, you can look here for all documents concerned with Senegal or Gambia by searching for &quot;&#39;Senegal\*&#39;, &#39;Gambi\*&#39;&quot;. In the second script, we will filter for documents that mention Malaria.
  - Go to line 99 and change the line &quot;InitSearch= [&#39;firm\*&#39;, &#39;enterpr\*&#39;, &#39;busines\*&#39;]&quot; to your search terms. E.g. &quot;InitSearch= [&#39;Senegal\*&#39;, &#39;Gambi\*&#39;]&quot;
- Save the script, again
- Execute the script (through the command prompt or by double-clicking the file)
  - A small window executing Python should appear
  - Depending on the breadth of your search, the speed or your internet connection and  the performance of your hardware, this may take a while (easily half an hour)
- In the meanwhile, copy the script &#39;DBCall.py&#39; into your code editor and save it in the same folder as &#39;Call.py&#39; as &#39;DBCall.py&#39;
- Line 9 reads &quot;search2 = &#39;SME\* OR MSME\*&#39;&quot;. Change &#39;SME\* OR MSME\*&#39; to your search. Complex searches are allowed for. Section 3 of [this website](https://www.sqlite.org/fts3.html) documents the syntax. Change it to what you want to narrow your results down to. If you do not want to narrow your result set, type in &#39;\*&#39;
- Check whether the first script, &#39;Call.py&#39;, is fully executed. The small window should show &#39;All entries added to the database. Well done!&#39; as the last prompt (and then possibly close itself). If this is the case, you can execute the second script, &#39;DBCall.py&#39;.
- The second script should only take a few seconds to execute. A file called &#39;RIS Formatted Eldis Data.ris&#39; should appear in the same folder as DBCall.py. This should be your fully functional RIS file.

