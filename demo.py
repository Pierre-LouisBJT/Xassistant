"""
To run a local demo in your terminal
"""
import ask

print("")
print("Welcome to the local demo of Xassistant.")
print("")
print("Pres Ctrl+C to quit")
print("")

while True :
    query = input("What is your question about the document : ")
    answer = ask.ask(query)
    print(answer)
    print("")

