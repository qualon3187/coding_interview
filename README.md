# Background

Most calendar applications provide some kind of "meet with" feature where the user
can input a list of coworkers with whom they want to meet, and the calendar will
output a list of times where all the coworkers are available.

For example, say that we want to schedule a meeting with Jane, John, and Mary on Monday.

- Jane is busy from 9am - 10am, 12pm - 1pm, and 4pm - 5pm.
- John is busy from 9:30am - 11:00am and 3pm - 4pm
- Mary is busy from 3:30pm - 5pm.

Based on that information, our calendar app should tell us that everyone is available:
- 11:00am - 12:00pm
- 1pm - 3pm

We can then schedule a meeting during any of those available times.


# Instructions

Given the data in `events.json` and `users.json`, build a script that displays available times
for a given set of users. For example, your script might be executed like this:

```
python availability.py Maggie,Joe,Jordan
```

and would output something like this:

```
2021-07-05 13:30 - 16:00
2021-07-05 17:00 - 19:00
2021-07-05 20:00 - 21:00

2021-07-06 14:30 - 15:00
2021-07-06 16:00 - 18:00
2021-07-06 19:00 - 19:30
2021-07-06 20:00 - 20:30

2021-07-07 14:00 - 15:00
2021-07-07 16:00 - 16:15
```


For the purposes of this exercise, you should restrict your search between `2021-07-05` and `2021-07-07`,
which are the three days covered in the `events.json` file. You can also assume working hours between
`13:00` and `21:00` UTC, which is 9-5 Eastern (don't worry about any time zone conversion, just work in
UTC). Optionally, you could make your program support configured working hours, but this is not necessary.


## Data files

### `users.json`

A list of users that our system is aware of. You can assume all the names are unique (in the real world, maybe
they would be input as email addresses).

`id`: An integer unique to the user

`name`: The display name of the user - your program should accept these names as input.

### `events.json`

A dataset of all events on the calendars of all our users.

`id`: An integer unique to the event

`user_id`: A foreign key reference to a user

`start_time`: The time the event begins

`end_time`: The time the event ends


# Notes

- Feel free to use whatever language you feel most comfortable working with
- Please provide instructions for execution of your program
	-- download zip file from github
	-- unzip main.py  and json files to same folder location
	-- open command and cd to location
	-- in command prompt type python main.py Maggie Joe Jordan
	--Libraries needed for script:
		-  json
		-  sys
		-  datetime


- Please include a description of your approach to the problem, as well as any documentation about
  key parts of your code.
	-- My approach was to create dictionaries and return datetime values use date to string function. Starting 
	   by creating functions for storing user.json and events.json. The function used in correlation with sys.args to create the 
	   relations between files, so only correct values would appear per person. Calendar function was create using 15 min intervals
	   for time purpose. The calendar was used with the scheduleDay to create a pattern inside the dictionary created in the calendar
	   function. Using the final workDay calendar, we had more patterns and insert into seperate dictionaries using the pattern logic. 
	   Once the three seperate dictionaries are populated, each dictionary is loop through and returns available time frames using logic 
	   consists of the keys and values. All the printing and logic are contained inside the main user loop. 
	   Loop structure = Person name-> finds person id from user.json-> id is matched to user_id in events.json 
	   - used to get start_time and end_time which starts is used to logic of script

	   --Calendar can be changed to 1 min to account for times not in 15 min increments


- You'll notice that all our events start and end on 15 minute blocks. However, this is not a strict
  requirement. Events may start or end on any minute (for example, you may have an event from 13:26 - 13:54).
