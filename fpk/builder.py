import subprocess
from typing import List


class Builder:
    env: str
    manifest: str

    def __init__(self, env: str, manifest: str) -> None:
        self.env = env
        self.manifest = manifest

    def validate(self):
        result = subprocess.run(["flatpak-builder", "--version"])
        if result.returncode != 0:
            raise Exception("flatpak-builder could not be found")

    def build(self):
        subprocess.run(
            ["flatpak-builder", "--ccache", "--force-clean", self.env, self.manifest],
            check=True,
        )

    def run(self, cmd: List[str]):
        subprocess.run(
            ["flatpak-builder", "--run", self.env, self.manifest, "--"] + cmd
        )
