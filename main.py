import tweepy as tp;

def getUserTweets(user, api):
  tweets = api.user_timeline(user);
  return [tweets[0].text, tweets[1].text, tweets[2].text]

def main():
    
    """ Main entry point -- run script. """ 


    accessToken : str = "";
    accessSecret : str = "";

    consumerKey : str = ""; # Enter these in manually, found in the twitter
    consumerSecret : str = ""; # developer section.
    
    authentication = tp.OAuthHandler(consumerKey, consumerSecret);
    authentication.set_access_token(accessToken, accessSecret);
    
    api = tp.API(authentication);
    recentTweets = getUserTweets("KrazyBonesTV", api);
    for tweet in range(recentTweets):
      print(tweet);

main();