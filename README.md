# Decentralized Santa

This repo is intended to help you run a secret santa over distance without
one person knowing who get everyone else (including who got them!).

Broadly speaking, we will follow this guide for [sending emails with Python].

## Requirements

 - Python 2.6 or greater (and pip)
 - A Google account with Gmail enabled

## Setup

First, you need to follow the [Quickstart Guide] for Gmail's Python API. In
particular, click the `Enable the Gmail API` button.  You'll follow a couple
prompts to set up a Cloud Platform project, and in particular generate a
`credentials.json` file that will need to be put in this project directory.

**DO NOT UPLOAD THE CREDENTIALS FILE ANYWHERE.**



[sending emails with Python]: https://realpython.com/python-send-email/
[Quickstart Guide]: https://developers.google.com/gmail/api/quickstart/python
