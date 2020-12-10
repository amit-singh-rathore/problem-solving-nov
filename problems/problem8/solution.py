class ContextManagerExample:
    def __init__(self):
        print("Initialization of context")
    def __enter__(self):
        print("Entering Context")
    def __exit__(self, *args):
        print("Cleanup Done")
        
with ContextManagerExample():
    print("Example running of Context Manager")
    raise Exception("Error Encounterd")