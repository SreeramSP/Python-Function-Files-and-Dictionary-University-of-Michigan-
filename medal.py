#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.


top_three = []
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def top(key,d):
    return d[key]
top_three = sorted(medals.keys(), key = lambda x : top(x,medals), reverse = True)[:3]   