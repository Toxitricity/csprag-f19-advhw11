import tweepy as tp;

def main():
    
    """ Main entry point -- run script. """ 


    accessToken : str = "";
    accessSecret : str = "";

    consumerKey : str = ""; # Enter these in manually, found in the twitter
    consumerSecret : str = ""; # developer section.
    
    authentication = tp.OAuthHandler(consumerKey, consumerSecret);
    authentication.set_access_token(accessToken, accessSecret);
    
    api = tp.API(authentication);
    
