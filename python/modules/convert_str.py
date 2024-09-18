def StringChallenge(strParam):
    # Helper function to convert time to minutes from midnight
    def to_minutes(time):
        # Extract the hour, minute, and period (am/pm) from the time string
        hours, minutes = map(int, time[:-2].split(':'))
        period = time[-2:]

        # Convert 12-hour format to 24-hour format
        if period == 'pm' and hours != 12:
            hours += 12
        elif period == 'am' and hours == 12:
            hours = 0
        
        # Return the total minutes from midnight
        return hours * 60 + minutes

    # Split the input string by the hyphen to separate the two times
    time1, time2 = strParam.split('-')

    # Convert both times to minutes from midnight
    minutes1 = to_minutes(time1)
    minutes2 = to_minutes(time2)

    # Calculate the difference, considering if the time crosses midnight
    if minutes2 >= minutes1:
        difference = minutes2 - minutes1
    else:
        # Add 1440 minutes (24 hours) if time crosses midnight
        difference = (1440 - minutes1) + minutes2

    # Proper return statement that replaces `return strParam`
    return difference

# Keep this function call here as per the template
print(StringChallenge(input()))
