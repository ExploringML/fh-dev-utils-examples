# Jupyter Basic Example

This example implements a Jupyter server alongside your FastHTML app. On startup you'll notice an additional link in the FastHTML terminal output. Something like `Jupyter Lab link: http://localhost:8036/lab`.

```
$ python main.py
Jupyter Lab link: http://localhost:8036/lab
Link: http://localhost:5001
INFO: Will watch for changes in these directories: ['/fh-dev-utils-examples/jupyter-basic']
INFO: Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO: Started reloader process [198400] using WatchFiles
INFO: Started server process [198428]
INFO: Waiting for application startup.
INFO: Application startup complete.
```

Click on the link to open a full Jupyter Lab server in the browser.

<image src="./thumb2.png" width="750">

<br>
As this example focuses on adding a Jupyter server, the FastHTML app itself is just the basic minimal 'Hello World' example from the docs, which uses Pico styles rather than TailwindCSS.
<br><br>

<image src="./thumb.png" width="750">
