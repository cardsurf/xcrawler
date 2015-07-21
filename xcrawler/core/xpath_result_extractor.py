

class XPathResultExtractor(object):
    """Extracts data from XPath expression result.

    """
    @classmethod
    def extract(cls, result, index = None, default_value = None, strip = False, split_pattern = None):
        if(index != None):
            result = cls.xpath_result_get_index(result, index, default_value)
        if(strip == True):
            result = cls.xpath_result_strip(result)
        if(split_pattern != None):
            result = cls.xpath_result_split(result, split_pattern)
            
        return result

    @classmethod
    def xpath_result_get_index(self, result, index, default_value):   
        try:
            result = result[index]
        except IndexError:
            result = default_value
        return result

    @classmethod  
    def xpath_result_strip(self, result, strip_pattern):
        try:
            result = result.strip(strip_pattern)
        except AttributeError:
            pass
        return result

    @classmethod  
    def xpath_result_split(self, result, split_pattern):
        try:
            result = result.split(split_pattern)
        except AttributeError:
            pass
        return result
    

        