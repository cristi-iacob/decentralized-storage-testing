import random

INITIAL_LOGINS = 50
TOTAL_COMMANDS = 500
LOGOUT_PROBABILITY = 0.2
LOGIN_PROBABILITY = 0.6
UPLOAD_PROBABILITY = 0.7
DOWNLOAD_PROBABILITY = 0.8


class SimmulationGenerator:
    def __init__(self, name, probs=None):
        self.file = open(name, 'w')
        self.nr_commands = 0
        self.logged = set()
        self.user_files = dict()
        if probs is None:
            self.probs = [0.2, 0.1, 0.3, 0.4]
        else:
            self.probs = probs

    def write_login(self, user):
        self.file.write('li' + 2 * (',' + user) + '\n')

    def write_logout(self, user):
        self.file.write('lo,' + user + '\n')

    def write_upload(self, user):
        self.file.write('u,' + user + '\n')

    def write_download(self, user):
        self.file.write('d,' + user + '\n')

    def write_initial_logins(self):
        for i in range(INITIAL_LOGINS):
            nr = random.randint(1, 500)
            self.write_login('user' + str(nr))
            self.logged.add('user' + str(nr))

    def simulate(self):
        cnt = INITIAL_LOGINS
        self.write_initial_logins()

        for i in range(TOTAL_COMMANDS):
            rnd = random.random()
            if rnd < self.probs[0]:
                while True:
                    nr = random.randint(1, 500)
                    if 'user' + str(nr) not in self.logged:
                        self.logged.add('user' + str(nr))
                        self.write_login('user' + str(nr))
                        break
                cnt += 1
            elif rnd < sum(self.probs[0:2]):
                user = random.choice(tuple(self.logged))
                self.write_logout(user)
                self.logged.remove(user)
                cnt += 1
            elif rnd < sum(self.probs[0:3]):
                user = random.choice(tuple(self.logged))
                self.write_upload(user)
                cnt += 1
            else:
                user = random.choice(tuple(self.logged))
                self.write_download(user)
                cnt += 1
