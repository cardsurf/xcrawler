# Changelog

### Version 1.3.0
Added setting HTTP session parameters such as: cookies, SSL certificates, proxies
Added setting HTTP request parameters such as: header, body, authentication
Added support for file download
Added requests library to project requirements
Modified type of the timeout attribute in the Config class to a tuple: (connect timeout, read timeout)
Added examples: file download, settings session parameters and setting requests parameters

### Version 1.2.0
Added support for Python 3  
Improved converting links to absolute urls  
Added a request attribute to the Page class  

### Version 1.1.0
Added support for CSS selectors  
Added examples of using CSS selectors  
Added support for writing non-string attributes to an output file  
Added support for safer extraction of incomplete data with a FallbackList  
Added examples of using a FallbackList to extract incomplete data from a web page  
Fixed bugs when converting ascii strings to unicode  

### Version 1.0.1
The crawler exits Main thread after visiting web pages

### Version 1.0.0
Initial release
