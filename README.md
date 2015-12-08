# Big-Data-Scripts
Miscellaneous Python Scripts for working with Big Data files that are new-line delimited JSON files

**popular-subreddits.py:**

This is a simple Python program to read a reddit comment dump and print out the most popular subreddits sorted by number of comments made within each subreddit.

Example usage: ```python popular-subreddits.py sample.bz2```

**popular-words.pl**

This is a Perl script to show the most popular words from a collection of comments.

Example usage: ```bzip2 -cd sample.bz2 | ./popular-words.pl```

**Linux command line Kung-Fu Examples**

The following commands will work on most Linux operating systems.  I am using Ubuntu 14.04 for these examples.

*Pretty print JSON and learn about the JSON object structure using Python*

    bzip2 -cd sample.bz2 | head -n1 | python -m json.tool

*Print the author from each JSON block using Perl*

Make sure Cpanel::JSON::XS is installed

    cpan Cpanel::JSON::XS

Now you can do:

    bzip2 -cd sample.bz2 | perl -MCpanel::JSON::XS -lne 'print decode_json($_)->{author}'

*Sort these authors by number of times they have made a comment*

    bzip2 -cd sample.bz2 | perl -MCpanel::JSON::XS -lne 'print decode_json($_)->{author}' | sort | uniq -c | sort -n

**Location of main Reddit Data**

You can download billions of Reddit comments from my main archive.  If you use this data for research, I would kindly ask that you attribute my efforts in your publication.  Thank you!

Location: http://pan.whatbox.ca:36975/reddit/comments/monthly/
