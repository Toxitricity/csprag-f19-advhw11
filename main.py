import tweepy as tp;

def getUserTweets(user, api, num_desired=20):
  """ Grab text of most recent user tweets """
  tweets = api.user_timeline(user, count=num_desired);
  return [tweet.text.lower() for tweet in tweets][0:num_desired]

def main():
    
    """ Main entry point -- run script. """ 

    accessToken : str = ""
    accessSecret : str = ""
    consumerKey : str = ""
    consumerSecret : str = ""
    
    authentication = tp.OAuthHandler(consumerKey, consumerSecret);
    authentication.set_access_token(accessToken, accessSecret);
    
    api = tp.API(authentication);
    recentTweets = getUserTweets("KrazyBonesTV", api);
    for tweet in recentTweets:
      if "commission" in tweet and ("slot" in tweet or "open" in tweet):
        print("Commissions Opened!");
        api.send_direct_message("kemolek", 
        """ Hello Kemolek, 
        
        """
        )
    
    print("Application Closed");

main();