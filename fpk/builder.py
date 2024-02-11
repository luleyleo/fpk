import subprocess
from typing import List


class Builder:
    env: str
    manifest: str

    def __init__(self, env: str, manifest: str) -> None:
        self.env = env
        self.manifest = manifest

    def validate(self):
        result = subprocess.run(["flatpak-builder", "--version"], capture_output=True)
        if result.returncode != 0:
            raise Exception("flatpak-builder could not be found")

    def install_deps(self) -> bool:
        result = subprocess.run(
            [
                "flatpak-builder",
                "--install-deps-from=flathub",
                "--install-deps-only",
                self.env,
                self.manifest,
            ],
            capture_output=True,
        )
        if result.returncode != 0:
            print("Failed to install dependencies:")
            print("> ", result.stderr.decode())
            return False

        return True

    def build(self) -> bool:
        if not self.install_deps():
            return False

        result = subprocess.run(
            [
                "flatpak-builder",
                "--ccache",
                "--force-clean",
                self.env,
                self.manifest,
            ],
            capture_output=True,
        )
        if result.returncode != 0:
            print("Failed run flatpak-builder:")
            print("> ", result.stderr.decode())
            return False

        return True

    def run(self, cmd: List[str]):
        subprocess.run(
            ["flatpak-builder", "--run", self.env, self.manifest, "--"] + cmd
        )
