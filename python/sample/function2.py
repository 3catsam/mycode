def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"
        
read = raw_input("Shut down?")
print shut_down(read)
