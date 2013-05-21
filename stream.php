<?php
require_once('lib/Phirehose.php');
/**
 * Example of using Phirehose to display a live filtered stream using track words 
 */
class FilterTrackConsumer extends Phirehose
{
  /**
   * Enqueue each status
   *
   * @param string $status
   */
  public function enqueueStatus($status)
  {
    /*
     * In this simple example, we will just display to STDOUT rather than enqueue.
     * NOTE: You should NOT be processing tweets at this point in a real application, instead they should be being
     *       enqueued and processed asyncronously from the collection process. 
     */
     file_put_contents('tweets.txt', $status, FILE_APPEND | LOCK_EX);
     //print $status > tweets.txt;	
     //system("mysql sopitz -e \"insert into twitter (id, data) values (null, '$status');\"");	
//     $data = json_decode($status, true);
//     if (is_array($data) && isset($data['user']['screen_name'])) {
    	
//       print $data['user']['screen_name'] . ': ' . urldecode($data['text']) . "\n";
//       mysql_query("SELECT * FROM twitter;");
//     }
  }
}
// Start streaming
$sc = new FilterTrackConsumer('filterapi', 'twitterbot', Phirehose::METHOD_FILTER);
$sc->setTrack(array(
		'#GOOG', '#SPY', '#GLD', '#DIA', '#QQQ', '#AAPL', '#MSFT', '#PG', '#KFT', '#AA',
		'$GOOG', '$SPY', '$GLD', '$DIA', '$QQQ', '$AAPL', '$MSFT', '$PG', '$KFT', '$AA'));
$sc->consume();
