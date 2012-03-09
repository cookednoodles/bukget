import threading
import time
import bukget.log
from hashlib import md5
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

class BaseParser(threading.Thread):
    _timer = 0
    _delay = 2
    _verbose = False
    _log = bukget.log.log
    
    def _get_page(self, url):
        '''get_page url
        
        Returns a BeautifulSoup object of the HTML page in the URL specified.
        '''
        while (time.time() - self._timer) < self._delay:
            time.sleep(0.1)
        self._timer = time.time()
        return BeautifulSoup(self._get_url(url))
    
    
    def _get_url(self, url):
        '''get_url
        
        Return the contents of the URL specified.
        '''
        self._log.debug('Fetching: %s' % url)
        return urlopen(url).read()
    
    
    def _hash(self, string):
        '''hash string
        
        Returns a md5sum of the string variable.
        '''
        h = md5()
        h.update(string)
        return h.hexdigest()