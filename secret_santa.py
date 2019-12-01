import getpass
import random
import smtplib, ssl


class Person:
    """Someone that can be purchased for."""
    def __init__(self, name, email, household):
        self.name = name
        self.email = email
        self.household = household
        self.choice = None
        self.possible_choices = set()

    def __str__(self):
        return "{0} (email: {1})".format(self.name, self.email)

    def consider(self, other):
        self.possible_choices.add(other)

    def choose(self):
        if len(self.possible_choices) == 0:
            return (False, None)

        choice = random.choice(list(self.possible_choices))
        self.choice = choice
        return (True, choice)

    def drop(self, other):
        self.possible_choices.discard(other)

    def count(self):
        return len(self.possible_choices)

    def is_same_household(self, other):
        if self.household is None or other.household is None:
            return False
        else:
            return self.household == other.household


class Pool:
    """The full selection of Persons to be chosen"""
    def __init__(self):
        self.people = []

    def add(self, name, email, household=None):
        new_person = Person(name, email, household)
        for person in self.people:
            if not person.is_same_household(new_person):
                person.consider(new_person)
                new_person.consider(person)
        self.people.append(new_person)

    def email(self):
        print("A selection has been found; now to email.")
        gmail_user = input("Enter your gmail address: ")
        gmail_password = getpass.getpass("Enter your password: ")
        email_text = "\n".join([
            "From: {}".format(gmail_user),
            "To: {email}",
            "Subject: Secret Santa",
            "\nDear {name},",
            "\nThis is an automated email from Kyle's Python script.",
            "You were given {choice} to buy a present for.",
            "\nHave fun!"
            ])
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            for person in self.people:
                smtp.login(gmail_user, gmail_password)
                smtp.sendmail(gmail_user,person.email,email_text.format(
                    email=person.email, name=person.name, choice=person.choice.name
                    ))

    def select_for(self, member):
        succeeded, choice = member.choose()
        if not succeeded:
            return False
        else:
            for p in self.people:
                p.drop(choice)
            return True


if __name__ == '__main__':
    import sys

    filename = sys.argv[1]

    family = Pool()
    with open(filename, 'r') as f:
        people = f.readlines()
        for person in people:
            family.add(*person.split(","))

    for _ in range(len(family.people)):
        fewest = min([p.count() for p in family.people if p.choice is None])
        options = [p for p in family.people if p.choice is None and p.count() == fewest]
        succeeded = family.select_for(random.choice(options))
        if not succeeded:
            print("failed to properly select.")
            sys.exit(1)

    family.email()
