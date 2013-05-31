twitter
=======

correlation analysis
--------------------

The big question how do tweets correlate with stock price movements

Existing work has shown that tweets can be used to perdict the value
of a stock in the future. In [1] they use quite simple methods like a
set of words they associate with a stock and scan tweets for. I did not
yet got the point how they match the tweets to a specific stock value!
But they use a share of the available data a testing data. So it seems
there is some kind of learning algorithm involved.
A second approache presented is a mood analyzer. It searchs the tweets
associated to a stock for words that indicate happieness, anger and other
emotions, scales this finding somehow and - also currently magical - predict
a (future) value of the associated stock.
Overall the results are promising. Especially companies with a lot of
associated tweets (Google, Apple) and the more complex method gave good
results.

I didn't looked into [2] but it seems to present a similiar method.


[1] Modelling the Stock Market using Twitter, A. Wolfram, 2010, University of Edinburgh
[2] Twitter mood predicts the stock market., Johan Bollen. Huina Mao, Oct 2010, Indiana University-Bloomington

todos
-----

- find other papers, articles for the twitter predicts stock topic
- reread data mining techniques
- with enough time i really would like to throw stupid data mining at the data :)
- build a little python script that reads the twitter.txt file and ... well
  does a correlation analysis, just returns some data as csv so you can view it in libreoffice, something in between
