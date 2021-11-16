Title: @WIP Time handling is a real PITA
Date: 2021-11-11 11:58
Modified: 2021-11-11 11:58
Category: Tech
Tags: #javascript, #time, #date, #interval, #time-diff
Slug: time-handling-is-a-real-pita
Author: filipgorczynski
Status: draft
Summary: I hate date and time operations. Even with all those libraries available around it's still hard to understand.

I hate date and time operations. Even with all those libraries available around it's still hard to understand.

To fulfil my personal commitment about side projects (event if [I'm scared of them](https://blog.filipgorczynski.me/2021/10/i-m-afraid-of-side-projects/)), I'm working on a simple project - time logger.

And as it's a time logger it's nice to have some information about how long I've spent on something.

So every time entry has: hours, minutes and seconds. Sounds obvious. I also wanted to display simplified version of time spent on a task, like: `02h 34m`. Looks good as well.

So I've wrote some simple function to return that time I've spent doing a task by number of seconds:

```javascript
function formatTime(seconds) {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.ceil((seconds - hours * 3600) / 60);
  return `${hours}h ${minutes}m`;
}
```

My `addTimeEntry` callback function is an event handler to form submition:

```javascript
    addTimeEntry(event, data) {
        let currentTimer = this.state.timer;
        currentTimer = 231;
        let now = new Date();
        now.setSeconds(0);
        let time = now.toLocaleTimeString("en-EN", {
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
        });
        let today = now.toLocaleDateString("en-EN", { // you can use undefined as first argument
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
        });
        data['createdAt'] = format(now, 'yyyy-MM-dd HH:mm:ss');
        data['createDate'] = today;
        data['createTime'] = time;
        data['timestamp'] = +now; // TIL: shorter than .getTime()
        data['timeSpent'] = formatTime(currentTimer);
        data['inSeconds'] = currentTimer;

        const startDate = new Date(subSeconds(now, currentTimer));
        startDate.setSeconds(0);
        const startTime = format(startDate, 'HH:mm');
        const endTime = format(now, 'HH:mm');
        data['timeRange'] = `${startTime}-${endTime}`;
        let prevTimeEntries = [...this.state.timeEntries]
        this.setState({ timeEntries: [data, ...prevTimeEntries]});

        this.setState({
            timer: 0,
        });
    }
```

I also wanted to display simplified time range in format: `11:35-11:44`

The ~~problem~~ challenge was inconsistence between time I've spent (in seconds) and time displayed from start and end date, like below:

- startDate: 2021-11-11 11:35:58
- endDate: 2021-11-11 11:39:49
- converting seconds I've worked on something gives `0h 3m`
- difference in simplified time range, 11:35-11:39 gives `0h 4m`

After juggling a bit with time intervals, durations and so, the easiest way was actually setting 0 for seconds in every date, so:

```javascript
startDate.setSeconds(0);
endDate.setSeconds(0);
```

Now, the difference is always correct.
