from abc import ABC, abstractmethod
class DataParser(ABC):
    
    def _parse(self):
        self._open()
        # parse the data
        self._dataparser()
        self._close()

    def _open(self):
        print("opening the file")

    def _close(self):
        print("closing the file")

    @abstractmethod
    def _dataparser(self):
        pass

class CsvParser(DataParser):
    def _dataparser(self):
        print("it is parsing csv file")
        
class JSONParser(DataParser):
    def _dataparser(self):
        print("it is parsing json file")

    def _close(self):
        print("hey it is closing the json file manuallyt")
csv=CsvParser()
json=JSONParser()
csv._parse()
json._parse()