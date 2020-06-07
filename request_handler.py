import random

import requests
import media_selecter as media

URL = 'http://localhost:8080/'


class Requests:
    user_files = dict()
    logged = set()

    @staticmethod
    def send_login_request(username, password):
        if username in Requests.logged:
            return

        data = {
            'username': username,
            'password': password
        }

        requests.post(URL + 'login', data)
        Requests.logged.add(username)

    @staticmethod
    def send_logout_request(username):
        if username not in Requests.logged:
            return

        data = {
            'username': username
        }

        requests.post(URL + 'logout', data)
        Requests.logged.remove(username)

    @staticmethod
    def send_upload_request(username):
        if username not in Requests.logged:
            return

        path = media.select_random_photo_path()

        with open(path, 'rb') as img:
            files = {
                'file': open(path, 'rb'),
            }

        data = {
            'client': 'user1'
        }
        response = requests.post(URL + 'upload', files=files, data=data)

        if username not in Requests.user_files:
            Requests.user_files[username] = set()
        Requests.user_files[username].add(response.content.decode('utf-8'))

    @staticmethod
    def send_download_request(username):
        if username not in Requests.logged or username not in Requests.user_files:
            return
        try:
            data = {
                'client': username,
                'filename': random.choice(tuple(Requests.user_files[username]))
            }

            response = requests.get(URL + 'download', data)
            if response.content[:5] == b'There':
                return 'peers'
            f = open(username + '/poza.jpeg', 'wb')
            f.write(response.content)
            f.close()
        except Exception as e:
            pass

        return None

    @staticmethod
    def send_all_offline_request():
        requests.get(URL + 'alloffline')
