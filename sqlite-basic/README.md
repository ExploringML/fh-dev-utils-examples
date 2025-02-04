# SQLite Basic Example

This example implements an SQLite database and the [sqlite-web](https://github.com/coleifer/sqlite-web) database browser for viewing/editing data and running SQL queries etc. On startup you'll notice an additional link in the FastHTML terminal output. Something like `SQLite link: http://localhost:8035`.

```
$ python main.py
SQLite link: http://localhost:8035
Link: http://localhost:5001
INFO: Will watch for changes in these directories: ['/fh-dev-utils-examples/sqlite-basic']
INFO: Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO: Started reloader process [204906] using WatchFiles
INFO: Started server process [204909]
INFO: Waiting for application startup.
INFO: Application startup complete.
```

Click on the link to open the sqlite-web database browser.

<image src="./thumb.png" width="750">

<br>
The FastHTML app is a simple SQLite databse example, which uses Pico for the CSS styles.
<br><br>

<image src="./thumb2.png" width="750">
