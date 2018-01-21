<p>
    README
</p>
<p>
    <strong>Purpose of this project </strong>
</p>
<p>
    The purpose of this project is to create RIS files from citation or trial
    databases that do not offer the service to export those files. The focus is
    to create files that can be imported into
    <a
        href="https://eppi.ioe.ac.uk/CMS/Default.aspx?alias=eppi.ioe.ac.uk/cms/er4&amp;"
    >
        EPPI reviewer
    </a>
    , a software solution for systematic reviews.
</p>
<p>
    Additionally, I try to offer guidance here for people not experienced with
    coding. Therefore, if you have no experience with coding in Python, please
    do not hesitate to go ahead. Read all README files carefully and you should
    be able to execute the code.
</p>
<p>
    <strong>Databases covered </strong>
</p>
<p>
    At the moment, you can find code for the following databases:
</p>
<ul>
    <li>
        <a href="https://www.socialscienceregistry.org/">AEA RCT registry</a>
    </li>
    <li>
        <a href="https://opentrials.net/">OpenTrials </a>
    </li>
    <li>
        <a href="https://clinicaltrials.gov/">Clinicaltrials.gov</a>
    </li>
    <li>
        <a href="http://www.who.int/ictrp/en/">WHO ICTRP</a>
    </li>
    <li> 
        <a href="http://www.eldis.org/">ELDIS</a>
    </li>
</ul>
<p>
    I am currently developing code for
</p>
<ul>
    <li>
        <a href="http://www.bridge.ids.ac.uk/">BRIDGE </a>
    </li>
    <li>
        <a href="https://www.povertyactionlab.org/evaluations">JPAL</a>
        Evaluations
    </li>
</ul>
<p>
    On my wish-list that I am going to work on, if I find time are
</p>
<ul>
    <li>
        <a href="https://www.ssrn.com/en/">SSRN</a>
    </li>
    <li>
        <a href="https://ideas.repec.org/">IDEAS (RePec)</a>
    </li>
    <li>
        <a href="https://labordoc.ilo.org/">LaborDoc</a>
    </li>
</ul>
<p>
    Please feel free to suggest more or to adapt my code to more databases (and
    ideally post it here)
</p>
<p>
    <strong>Legal Matters </strong>
</p>
<p>
    I take no responsibility for what you do with my code. Some of the
    databases mentioned here actively encourage to freely download and use
    their data, as long as you attribute it. Others try to guard their data
    against being read by machines and I tricked the websites into telling me
    their secrets. I do not have the resources to make sure that all scripts
    are fully legal to execute or even make agreements with the database
    providers (see next point). However, neither does Google (which technically 
    does very similar things). Please judge yourself.
</p>
<p>
    <strong>Professionalism </strong>
</p>
<p>
    The scripts here are &#8216;Quick and Dirty&#8217;. They do not comply with
    programming conventions and are not specifically quick or beautiful. I am
    an economist and not a professional programmer. I made them for my own
    systematic reviews and optimised them to the point where they work fine for
    me. Please make sure yourself whether the scripts return what you expected.
</p>
<p>
    Furthermore, all scripts are currently in an early stage of development. If
    you find issues with the code, please do not hesitate to contact me. I do
    not have the expertise for some of them (e.g. which field in a trials
    database conventionally corresponds with which field in a citation record)
    and I would be happy to be pointed at them.
</p>
<p>
    <strong>What you need </strong>
</p>
<p>
    You will need a computer and an internet connection. All scripts are in the
    Python programming language, which is free. Therefore, please make sure
    Python 3.X is installed on your computer. The internet offers hundreds of
    good
    <a href="http://lmgtfy.com/?q=Installing+Python">
        guides how to install it
    </a>
    . Additionally, a code editor might be useful. You could edit the code
    presented here in the Windows editor or the like. However, a real code
    editor will help you to keep track and is very useful for searching
    literature, anyway (try it out and you will never make a bracing or
quotation-mark error in your search strings, again!). I use<a href="https://atom.io/">Atom</a>, but other code editors, such as    <a href="https://notepad-plus-plus.org/">Notepad++</a> do an excellent job,
    as well.
</p>
<p>
    Some of the scripts will need some additional &#8216;packages&#8217;.
    Packages are additions to Python that take care of common tasks. How to get
    hold of them will be explained for each script in its README.
</p>
<p>
    I use Windows. Python runs on Linux and iOS, as well. I suspect that most
    scripts will run on them, as well, but I am not sure. If you have
    cross-platform issues, please notify me and I will try to solve them.
</p>
