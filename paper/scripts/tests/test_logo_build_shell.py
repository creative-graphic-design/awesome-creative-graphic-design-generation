"""Regression checks for institutional logo download/build shell script.

The source-PDF build must reject malformed shell code before it fetches any
external marks. This prevents an earlier duplicated Meituan archive block
from surviving until the costly LaTeX step.
"""

from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "prepare_affiliation_logos.sh"


class LogoBuildShellTests(unittest.TestCase):
    def test_logo_build_shell_parses(self) -> None:
        completed = subprocess.run(
            ["sh", "-n", str(SCRIPT)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_duplicate_broken_tail_fails_parsing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            broken_script = Path(directory) / "prepare_affiliation_logos.sh"
            broken_script.write_text(
                SCRIPT.read_text(encoding="utf-8") + '\n)"\n',
                encoding="utf-8",
            )
            completed = subprocess.run(
                ["sh", "-n", str(broken_script)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)

    def test_meituan_archive_extractor_is_unique_and_pinned(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertEqual(source.count('meituan_entry='), 1)
        self.assertEqual(source.count("if grep -Fq '}{pku}'"), 1)
        self.assertIn("grep -v '^__MACOSX/' | grep -Ei '\\.ai$'", source)
        self.assertIn("unzip -p \"$meituan_zip\" \"$meituan_entry\"", source)
        self.assertIn(
            "meituan_ai_sha=0df68fc2b3b25ddbeaa7f4046c0f74b3aae2fb05",
            source,
        )


if __name__ == "__main__":
    unittest.main()
