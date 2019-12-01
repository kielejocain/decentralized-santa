# Decentralized Santa

This repo is intended to help you run a secret santa over distance without
one person knowing who get everyone else (including who got them!).

**This doesn't work as intended yet!** You have to go to your [Google Security]
settings and turn on `Less secure app access`.  This is the first thing I aim
to change.

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

Next, you need to install a few Python packages.  I will be using conda
as a virtual environment manager, but do whatever it is you do to create a
virtual environment, then use pip to add the packages in the Guide.

    conda create --name santa
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Participants

In order to create a Secret Santa distribution, the program needs to know who
is participating and who lives in the same house (and therefore shouldn't get
each other).  This is done by creating a contacts.csv file with three columns:
name, email, and household.

The `name` column is how that participant will be addressed in emails.

The `email` column is the contact used to email.

The `household` column can be left blank if the person is not in a household;
otherwise it's treated as a text tag that doesn't allow two people with the
same tag to match.

Here is an example `contacts.csv` file:

    Kyle,me@gmail.com,MyHouse
    Wife,wife@gmail.com,MyHouse
    Sister,sister@hotmail.com,In-Law
    Bro-In-Law,bil@yahoo.com,In-Law
    LilSis,lilsis@gmail.com,

You can see that LilSis has no household; she doesn't live with anyone
participating in the process, so doesn't need a group label.

# Testing

Now we want to test that the process works.

# TODO

 - refactor script to use OAuth
 - add `smtpd` test framework for debugging
 - work on a better selection algorithm

[Google Security]: https://myaccount.google.com/u/1/security
[sending emails with Python]: https://realpython.com/python-send-email/
[Quickstart Guide]: https://developers.google.com/gmail/api/quickstart/python
