import subprocess
from pathlib import Path
from typing import List


class Builder:
    env: Path
    manifest: Path

    def __init__(self, env: Path, manifest: Path) -> None:
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
