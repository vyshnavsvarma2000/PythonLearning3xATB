#Fixture -> Concept in Python
# You can use the fixture
# Context to the test
# Similar - precondition, post-condition

#Setup and Teardown -> Pre and Post condition


import pytest

@pytest.fixture()
def sample_data():
    data = [1,2,3,4,5]
    return data
@pytest.fixture()
def sample_data_2():
    return True

def test_sample_1_2(sample_data,sample_data_2):
    print(sample_data, sample_data_2)