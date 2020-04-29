"""
cventry{2007--2020}{Electronics Eng. Tech.}{PowerCore
  Engineering}{London, ON}{Automation specialist primarily assigned
  to Traction Motor Test Station support and design of new
  builds.}{}
"""

import re
import pyperclip as clipboard
from swissarmy import fmtEmpty

reCvEntry = re.compile(
    #    r"\\cventry"
    r"\s*\{(?P<when>[0-9]+)(?P<towhen>--[0-9]+)??\}"
    r"\s*\{(?P<what>[^}]*)?\}"
    r"\s*\{(?P<who>[^}]*)?\}"
    r"\s*\{(?P<where>[^}]*)?\}"
    r"\s*\{(?P<why>[^}]*)?\}"
    r"\s*\{(?P<last>[^}]*)?\}",
    re.MULTILINE,
)

a = """\cventry{2019--2020}{Alternator Test Station}{Progress Rail Services}{Winston-Salem, NC}{}{AC
  \& DC Alternator Test Station}
\cventry{2017--2018}{Traction Motor Test}{Progress Rail Services}{Redbank, QLD, Australia}{}{AC \& DC Traction Motor Test
      Station}"""

b = """\cventry{2007--2020}{Electronics Eng. Tech.}{PowerCore
  Engineering}{London, ON}{Automation specialist primarily assigned
  to Traction Motor Test Station support and design of new
  builds.}{}
\cventry{2009}{AC Traction Motor Test}{Electro-Motive Diesels}{Yongji,
  China}{}{AC Traction Motor Test Station}
"""


def cventry_to_rst(data=None):
    if data is None:
        data = clipboard.paste()
    data = re.sub(r"\s+", " ", data)
    rst = []
    for cv in data.split("\\cventry"):
        if (m := reCvEntry.match(cv)) is not None:
            entry = """{when}{towhen}
  {what}
    {who}, {where}
    {why}{last}
"""
            rst.append(
                fmtEmpty.format(
                    entry,
                    when=m.group("when"),
                    towhen=m.group("towhen"),
                    what=m.group("what"),
                    who=m.group("who"),
                    where=m.group("where"),
                    why=m.group("why"),
                    last=m.group("last"),
                )
            )

    if len(rst) > 0:
        clipboard.copy("".join(rst))
    return rst
