import os
import sys
import glob

from utils.parser import FileParser
from processing.dataset import Dataset, Data


class ImageProcessor:

    def __init__(self, fileParser):
        self.dataset = []
        self.data = []
        self.debug = fileParser.debug
        self.verbose = fileParser.verbose

        self._set_dataset_paths(fileParser)


    def _set_dataset_paths(self, fileParser):
        paths_nuclei = sorted(glob.glob("%s/*%s*.tif" % (fileParser.input_directory, fileParser.COLOUR_NUCLEI)))
        paths_cells  = sorted(glob.glob("%s/*%s*.tif" % (fileParser.input_directory, fileParser.COLOUR_CELLS)))
        paths_agg    = sorted(glob.glob("%s/*%s*.tif" % (fileParser.input_directory, fileParser.COLOUR_AGGREGATES)))

        self.dataset = Dataset(paths_nuclei, paths_cells, paths_agg, fileParser.input_directory)


    def _make_output_directories(self):
        self.dataset.output_folder_nuclei = "%s/nuclei" % self.dataset.output_folder_main
        if not os.path.exists(self.dataset.output_folder_nuclei):
            os.makedirs(self.dataset.output_folder_nuclei)

        self.dataset.output_folder_cells = "%s/cells" % self.dataset.output_folder_main
        if not os.path.exists(self.dataset.output_folder_cells):
            os.makedirs(self.dataset.output_folder_cells)

        self.dataset.output_folder_aggregates = "%s/aggregates" % self.dataset.output_folder_main
        if not os.path.exists(self.dataset.output_folder_aggregates):
            os.makedirs(self.dataset.output_folder_aggregates)


    def _set_data_paths(self, file_n, file_c, file_a):
        if not os.path.isfile(file_n):
            print("File %s does NOT exist!", file_n)
            sys.exit()
        if not os.path.isfile(file_c):
            print("File %s does NOT exist!", file_c)
            sys.exit()
        if not os.path.isfile(file_a):
            print("File %s does NOT exist!", file_a)
            sys.exit()
        self.data = Data(file_n, file_c, file_a)


#    def _segment(self):
#


    def segment(self):

        self._make_output_directories()

        for file_n, file_c, file_a in zip(self.dataset.paths_nuclei, self.dataset.paths_cells, self.dataset.paths_aggregates):

            self._set_data_paths(file_n, file_c, file_a)

            #self._segment()

