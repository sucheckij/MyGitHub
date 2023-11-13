import pytest

#Example of fixture without parametrizing
# @pytest.fixture(params=['c', 'd'])
# def print_input_data(request):
#     try:
#
#         a = 2
#         b = 2
#         print(f"\nAdding {a} to {b}")
#         print(f"Adding {request.param}")
#     except:
#         pass
#     yield  # in that place test is executed
#     try:
#         pass
#     except:
#         pass
#     finally:  # that part of code is always executed even is failed status
#         print("Something")

#Example of fixture with Parametrizing
@pytest.fixture(params=[1,2]) #here parameters should be as list of variable ex. ['c','d']
def print_input_data(request):
    try:

        a=2
        b=2
        print(f"\nAdding {a} to {b}")
        print(f"Adding {request.param}")
    except:
        pass
    yield #in that place test is executed
    try:
        pass
    except:
        pass
    finally: #that part of code is always executed even is failed status
        print("Something")

#Example of fixture with Parametrizing - second mathod


