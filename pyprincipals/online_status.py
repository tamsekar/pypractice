def online_count(dictionary):
    count = 0
    for values in dictionary:
        if dictionary[values] == 'online':
            count += 1
    return count


online_count({
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online", }
)
