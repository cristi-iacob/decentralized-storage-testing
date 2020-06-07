from request_handler import Requests as req


class Executor:
    def __init__(self, name):
        req.logged = set()
        req.user_files = dict()
        self.name = name
        self.file = open(name, 'r')
        self.bad_downloads = 0
        self.good_downloads = 0
        self.uploads = 0

    def execute_commands(self):
        for line in self.file:
            words = line.split(',')

            if words[0] == 'li':
                req.send_login_request(words[1], words[2][:-1])
            elif words[0] == 'lo':
                req.send_logout_request(words[1][:-1])
            elif words[0] == 'u':
                req.send_upload_request(words[1][:-1])
                self.uploads += 1
            elif words[0] == 'd':
                ret = req.send_download_request(words[1][:-1])
                if ret == 'peers':
                    self.bad_downloads += 1
                else:
                    self.good_downloads += 1

    def reload(self):
        self.file.close()
        self.file = open(self.name, 'r')
