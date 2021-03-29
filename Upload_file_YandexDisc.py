import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': self.token}

    def _get_upLoad_Link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        print(file_path)
        response = requests.get(upload_url, headers=self.headers, params=params)
        print(111, response.text)
        return response.json()

    def create_folder(self, folder_name):
        """метод создает папку на яндекс.диске с таким же именем как и в self.file_path"""
        URL = f"https://cloud-api.yandex.net/v1/disk/resources?path=%2F{folder_name}"
        put = requests.put(URL, headers=self.headers)
        try:
            return put.status_code, put.json()["message"]
        except KeyError:
            return put.status_code, put.json()["href"]

    def upload_file(self, file_path, file_name):
        href = self._get_upLoad_Link(file_name).get('href', '')

        if href:
            with open(file_path, 'rb') as f:
                response = requests.put(href, data=f)
                response.raise_for_status()
                if response.status_code == 201:
                    print('Файл успешно загружен на Яндекс.Диск')
                else:
                    print("Ошибка")


if __name__ == '__main__':
    uploader = YaUploader('AQAAAABTlNU_AAcEppordy9p5UgZvuaPa51uQG4')
    file_path = r'c:\my_folder\my_file.txt'
    result = uploader.upload_file(file_path, 'my_file.txt')
print()