# main.py
#
# Copyright 2024 Leopold Luley
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import click
from fpk.builder import Builder


@click.command()
@click.option("--target", default=".build")
@click.argument("manifest")
def build(target, manifest):
    builder = Builder(target, manifest)
    builder.build()


@click.command()
def run():
    print("run")


@click.command()
def shell():
    print("shell")


@click.group()
def main():
    pass


main.add_command(build)
main.add_command(run)
main.add_command(shell)