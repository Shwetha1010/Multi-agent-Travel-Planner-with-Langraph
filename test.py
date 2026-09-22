from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = tavily_search("Best hotels in India")
#print(res)

#res1 = search_flights("Plan a 7 days Nepal trip from Bangladesh")
#print(res1)

user_input=input("Enter travel request:")

res2=run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)
print("\nFinal Respnse:\n")
print(res2["answer"])

