

WHO ICTRP README

What you need

- Computer
- Python 3.X
- Internet

What this script does

- It takes an XML file from the WHO ICTRP database
- It restructures the data and writes corresponding parts of it into an RIS file (WHO ICTRP provides more data than what you end up with. For the full records, consult the WHO ICTRP database through the link in the RIS files or the XML files)

How to use it

- Go to the [WHO ICTRP website](http://apps.who.int/trialsearch/)
- Perform your search
- Click on &#39;Export results to XML&#39;
  -![alt text](https://raw.githubusercontent.com/Haay2/RIS_Exporter/Beta/For_Presentation/Export%20Field%20WHO%20website.JPG)
- If you agree with the terms and conditions, click &#39;I agree&#39;
- Click on &#39;Export all trials to XML&#39; in the pop-up window
  -![alt text](https://raw.githubusercontent.com/Haay2/RIS_Exporter/Beta/For_Presentation/Export%20Field%202%20WHO%20website.JPG)
- Save the resulting &#39;ICTRP-Results.xml&#39; file
- Create an empty folder of your choice
- Copy the code into your code editor
- Save the code as &#39;Call.py&#39; in the empty folder you created
- Move the downloaded &#39;ICTRP-Results.xml&#39; into the same formerly empty folder
- Execute the file (through the command prompt or by double-clicking the file)
  - A small window executing Python should briefly appear
- A file called &#39;RIS Formatted WHO ICTRP Data.ris&#39; should appear in the same folder as Call.py. This should be your fully functional RIS file.

