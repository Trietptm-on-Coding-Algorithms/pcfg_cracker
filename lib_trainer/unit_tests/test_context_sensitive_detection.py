#!/usr/bin/env python3


#######################################################
# Unit tests for context_sensitive_detection
#
#######################################################


import unittest
import unittest.mock


## Functions and classes to tests
#
from ..context_sensitive_detection import context_sensitive_detection


## Responsible for testing the context sensitive string detection
#
# Note:
# + = positive test, (valid input handling)
# - = stress test, (invalid input handling) 
#
# ==Current Tests==
# + Test whole password is a context sensitive string
# + Test #1 followed by <3
# + Test <3 followed by #1
#
class Test_Context_Sensitive_Checks(unittest.TestCase):


    ## Test whole password being a context sensitive replacement
    #
    def test_whole_password_is_context_sensitive(self):
    
        section_list = [('#1',None)]
        found_cs = context_sensitive_detection(section_list)
        
        assert found_cs == ['#1']
        assert section_list == [('#1','X')]
        
        
    ## Test #1 followed by <3
    #
    def test_number_one_followed_by_heart(self):
    
        section_list = [('#1<3',None)]
        found_cs = context_sensitive_detection(section_list)
        
        assert found_cs == ['<3','#1']
        assert section_list == [('#1','X'),('<3','X')]
        
    
    ## Test <3 followed by #1
    #
    def test_number_one_followed_by_heart(self):
    
        section_list = [('<3#1',None)]
        found_cs = context_sensitive_detection(section_list)
        
        assert found_cs == ['<3','#1']
        assert section_list == [('<3','X'),('#1','X')]