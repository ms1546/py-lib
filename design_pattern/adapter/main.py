class LegacyPrinter:
    def print_document(self, document):
        return f"Legacy Printer: {document}"

class NewPrinter:
    def display_document(self, document):
        pass

class PrinterAdapter(NewPrinter):
    def __init__(self, legacy_printer):
        self.legacy_printer = legacy_printer

    def display_document(self, document):
        return self.legacy_printer.print_document(document)

def client_code(printer: NewPrinter):
    print(printer.display_document("Adapter Pattern Example"))

legacy_printer = LegacyPrinter()

adapter = PrinterAdapter(legacy_printer)

client_code(adapter)
