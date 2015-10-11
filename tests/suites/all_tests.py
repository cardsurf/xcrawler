

import unittest
import fnmatch
import os
import imp


def get_all_modules(start_directory, filename_pattern): 
    modules = []
    
    for root, _, filenames in os.walk(start_directory):
        for filename in fnmatch.filter(filenames, filename_pattern):         
            path = os.path.join(root, filename)            
            filename_without_extension = os.path.splitext(filename)[0]
            module = imp.load_source(filename_without_extension, path)            
            modules.append(module)
            
    return modules


if __name__ == "__main__":
    
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_modules = get_all_modules("..", "test_*.py")
    for module in test_modules:
        suite.addTest(loader.loadTestsFromModule(module))

    #print suite.countTestCases()
    unittest.TextTestRunner(verbosity=2).run(suite)

