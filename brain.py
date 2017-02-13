from pyowm import OWM
import ConfigParser

cf=ConfigParser.ConfigParser()
cf.read('config.py')
_owm_api_key_ = cf.get('owm', 'API_KEY')

_twr_ck_ = cf.get('twitter', 'consumer_key')
_twr_cs_ = cf.get('twitter', 'consumer_secret')
_twr_ak_ = cf.get('twitter', "access_key")
_twr_as_ = cf.get('twitter', 'access_secret')

class brain:

    def get_weather(self):
        owm = OWM(API_key=_owm_api_key_)
        obs = owm.weather_at_place('Lawrence,US') # TODO: change hardcoded location
        print obs
        w = obs.get_weather()
        print w.get_temperature('fahrenheit')
        print w.get_detailed_status()
        stats = [w.get_temperature('fahrenheit'), w.get_detailed_status()]
        return stats

    def twitter(self, words):
        auth = tweepy.OAuthHandler(ck,cs)
        auth.set_access_token(ak,acs)
        api = tweepy.API(auth)
        tw = twitter.twitter(api)
