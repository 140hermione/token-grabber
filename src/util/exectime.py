import time

from discord import Embed, SyncWebhook


class ExecTime(object):
    def __init__(self):
        self._start = time.time()
        self._stop = None

    def stop(self):
        self._stop = time.time()

    def get_time(self):
        return round(self._stop - self._start, 2)

    def send(self, webhook: str):
        webhook = SyncWebhook.from_url(webhook)
        embed = Embed(title="Execution Time",
                      description=f"Execution time: {self.get_time()} seconds", color=10181046)
        webhook.send(embed=embed, username="Hermione",
                     avatar_url="https://media.discordapp.net/attachments/1017383195337039993/1021142830288207872/unknown.png")
