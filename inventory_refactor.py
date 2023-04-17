from collections.abc import Iterable
from .inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        for dado in self.importer.import_data(path):
            self.data.append(dado)

        return (
            SimpleReport.generate(self.data)
            if type == "simples"
            else CompleteReport.generate(self.data)
        )

    def __iter__(self):
        return InventoryIterator(self.data)

