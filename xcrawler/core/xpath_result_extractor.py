

class XPathResultExtractor(object):
    """Extracts data from a result of XPath expression.

    """

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
    

        