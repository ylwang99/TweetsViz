Introduction
------------
This is a tool for visualizing tweets given a list of tweet ids and also the relevance of each tweet given the qrels of a certain topic, where a non-relevant tweet is denoted with red background color, light green color for relevant tweet and green color for hightly relevant tweet.

=====================Pre-requisite==============
Two files: tweetIds.txt and qrels.txt in /data folder, where tweetIds.txt is a list of tweetIds, separated by newline and qrels.txt is from the original qrels text file but with only one topic.
You can also have json files for tweet ids and qrels stored in /json folder (sample files in /json folder), in which case, you can skip the first step in "How to use" section below.Introduction
------------

This is a tool for visualizing tweets given a list of tweet ids and also the relevance of each tweet given the qrels of a certain topic, where a non-relevant tweet is denoted with red background color, light green color for relevant tweet and green color for hightly relevant tweet.

Pre-requisite
-------------

Two files: tweetIds.txt and qrels.txt in /data folder, where tweetIds.txt is a list of tweetIds, separated by newline and qrels.txt is from the original qrels text file but with only one topic.

You can also have json files for tweet ids and qrels stored in /json folder (sample files in /json folder), in which case, you can skip the first step in "Getting Started" section below.

Getting Started
---------------

(1) Run /script/build.sh to generate the corresponding json files stored in /json folder:
```
$ sh ./script/build.sh
```

(2) Open the tweetsViz.html in a browser(Firefox or Safari, but not Chrome), the visaulization would display, and it's pretty self-explanatory.

====================How to use=================
Step:
(1) Run /script/build.sh to generate the corresponding json files stored in /json folder.
(2) Open the tweetsViz.html in a browser(firefox or safari, but not chrome), the visaulization would display, and it's pretty self-explanatory.