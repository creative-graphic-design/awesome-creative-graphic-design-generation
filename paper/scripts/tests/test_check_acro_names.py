"""Regression tests for the acro-name source linter."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "check_acro_names.py"
spec = importlib.util.spec_from_file_location("check_acro_names", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AcroNamesTest(unittest.TestCase):
    def setUp(self):
        self.names = {"Vinci": "vinci", "COLE": "cole", "OpenCOLE": "opencole", "LayoutGAN": "layoutgan"}

    def check(self, text):
        return [(name, key) for _, name, key in module.find_bare_names(text, self.names)]

    def test_bare_names_fail(self):
        self.assertEqual(self.check("Vinci and OpenCOLE extend LayoutGAN."), [
            ("Vinci", "vinci"), ("OpenCOLE", "opencole"), ("LayoutGAN", "layoutgan")])

    def test_acro_and_citation_keys_are_safe(self):
        self.assertEqual(self.check(r"\ac{vinci} \citep{opencole2024} \ac{cole}"), [])

    def test_comment_and_command_are_safe(self):
        self.assertEqual(self.check("% Vinci\n" + r"\label{fig:COLE} \input{figs/LayoutGAN}"), [])

    def test_longest_name_and_possessive(self):
        self.assertEqual(self.check("OpenCOLE replaces COLE's backend."), [
            ("OpenCOLE", "opencole"), ("COLE", "cole")])

    def test_does_not_match_substring(self):
        self.assertEqual(self.check("OpenCOLExtended and BioVinciLab are unrelated."), [])

    def test_registry_filters_tags(self):
        raw = (
            "\\DeclareAcronym{vinci}{\n short = {Vinci},\n tag = {systems}\n}\n"
            "\\DeclareAcronym{svg}{\n short = {SVG},\n tag = {abbreviations}\n}\n"
        )
        self.assertEqual(module.registered_names(raw), {"Vinci": "vinci"})


if __name__ == "__main__":
    unittest.main()
