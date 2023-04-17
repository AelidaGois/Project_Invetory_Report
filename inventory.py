from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    importers = {
        ".csv": CsvImporter,
        ".json": JsonImporter,
        ".xml": XmlImporter,
    }

    reports = {
        "completo": CompleteReport,
        "simples": SimpleReport,
    }

    @staticmethod
    def import_data(path, version):
        extension = path[path.rfind("."):]

        if extension not in Inventory.importers:
            raise ValueError("Formato de arquivo inválido.")

        data = Inventory.importers[extension].import_data(path)
        return Inventory.generate_report(data, version)

    @staticmethod
    def generate_report(data, version):
        if version not in Inventory.reports:
            raise ValueError("Versão de relatório inválida.")

        report_class = Inventory.reports[version]
        return report_class.generate(data)
